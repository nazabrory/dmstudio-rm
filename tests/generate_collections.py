import os
import sys
import shutil
import inspect
import re

# Add parent directory to path so dmstudio is importable when run from tests/
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dmstudio import agent, dmcommands, dmfiles
from dmstudio.command_registry import VERIFIED_COMMANDS
from dmstudio.notebook_builder import NotebookBuilder

def format_doc_to_markdown(doc_text):
    lines = doc_text.split('\n')
    formatted_lines = []
    
    for line in lines:
        stripped = line.strip()
        
        # Section headers
        if stripped in ('Input Files:', 'Output Files:', 'Fields:', 'Parameters:'):
            formatted_lines.append(f"\n### {stripped}\n")
            continue
            
        # Divider lines
        if re.match(r'^[-=]+$', stripped):
            continue
            
        # Command name/title header
        if stripped.isupper() and len(stripped) > 2 and not stripped.endswith(':'):
            formatted_lines.append(f"\n## {stripped}\n")
            continue
            
        # Parameter/file/field items: name: details
        match = re.match(r'^([a-zA-Z0-9_]+)\s*:\s*(.+)$', stripped)
        if match:
            name, details = match.groups()
            formatted_lines.append(f"\n* **{name}** ({details.strip()}):")
            continue
        elif re.match(r'^([a-zA-Z0-9_]+)\s*:$', stripped):
            name = stripped[:-1]
            formatted_lines.append(f"\n* **{name}**:")
            continue
            
        # Regular text lines
        if not stripped:
            formatted_lines.append("")
        else:
            indentation = len(line) - len(line.lstrip())
            if indentation >= 12:
                formatted_lines.append("  " + stripped)
            else:
                formatted_lines.append(stripped)
                
    result = '\n'.join(formatted_lines)
    result = re.sub(r'\n{3,}', '\n\n', result)
    return result.strip()

def is_param_required_in_doc(p_name, docstring):
    clean_name = p_name.lower()
    for suffix in ('_i', '_o', '_f', '_p'):
        if clean_name.endswith(suffix):
            clean_name = clean_name[:-2]
            break
            
    search_names = [clean_name]
    if clean_name.endswith('mods'):
        base = clean_name[:-4]
        search_names.append(base)
        search_names.append(base + '1')
    elif clean_name.endswith('files'):
        base = clean_name[:-5]
        search_names.append(base)
        search_names.append(base + '1')
    elif clean_name.endswith('s'):
        base = clean_name[:-1]
        search_names.append(base)
        search_names.append(base + '1')
        
    for name in search_names:
        pattern = r'\b' + re.escape(name) + r'\s*:'
        for match in re.finditer(pattern, docstring, re.IGNORECASE):
            start_idx = match.start()
            look_ahead = docstring[start_idx : start_idx + 4000]
            # Settle parameter block end to avoid matching down the docstring
            next_param_match = re.search(r'\n\s*[a-zA-Z0-9_]+\s*:', look_ahead[1:])
            if next_param_match:
                look_ahead = look_ahead[:next_param_match.start() + 1]
            if re.search(r'Required\s*=\s*Yes', look_ahead, re.IGNORECASE):
                return True
                
    return False

def parse_valid_value_from_docstring(p_name, docstring):
    if not docstring:
        return None
    # Remove suffixes
    clean_name = p_name.lower()
    for suffix in ('_i', '_o', '_f', '_p'):
        if clean_name.endswith(suffix):
            clean_name = clean_name[:-2]
            break

    # Look for clean_name block in docstring
    # The block starts with clean_name followed by optional spaces and colon
    pattern = r'\b' + re.escape(clean_name) + r'\s*:\s*\n'
    match = re.search(pattern, docstring, re.IGNORECASE)
    if not match:
        # Try finding clean_name: on a line
        pattern = r'^\s*' + re.escape(clean_name) + r'\s*:\s*$'
        match = re.search(pattern, docstring, re.IGNORECASE | re.MULTILINE)
        
    if not match:
        return None

    start_idx = match.start()
    look_ahead = docstring[start_idx : start_idx + 4000]
    # Settle block end
    next_param_match = re.search(r'\n\s*[a-zA-Z0-9_]+\s*:', look_ahead[1:])
    if next_param_match:
        look_ahead = look_ahead[:next_param_match.start() + 1]

    # Parse Default
    default_match = re.search(r'Default\s*=[ \t]*([^\n\r]+)', look_ahead, re.IGNORECASE)
    if default_match:
        val = default_match.group(1).strip()
        if val and val.lower() != 'undefined':
            return val

    # Parse Values
    values_match = re.search(r'Values\s*=[ \t]*([^\n\r]+)', look_ahead, re.IGNORECASE)
    if values_match:
        val = values_match.group(1).strip()
        if val and val.lower() != 'undefined':
            parts = [p.strip() for p in val.split(',')]
            if parts and parts[0]:
                return parts[0]

    # Parse Range
    range_match = re.search(r'Range\s*=[ \t]*([^\n\r]+)', look_ahead, re.IGNORECASE)
    if range_match:
        val = range_match.group(1).strip()
        if val and val.lower() != 'undefined':
            parts = [p.strip() for p in val.split(',')]
            if parts and parts[0]:
                return parts[0]

    return None

def wrap_in_quotes_if_needed(default_str):
    if default_str is None:
        return 'None'
    # If it is already quoted, or is a list, or is a number, return as is
    if default_str.startswith('[') or (default_str.startswith("'") and default_str.endswith("'")) or (default_str.startswith('"') and default_str.endswith('"')):
        return default_str
    if default_str in ('True', 'False', 'None'):
        return default_str
    # Check if it is a number (integer or float)
    try:
        float(default_str)
        return default_str
    except ValueError:
        pass
    # Otherwise, wrap it in single quotes and escape any internal single quotes
    escaped = default_str.replace("'", "\\'")
    return f"'{escaped}'"

def get_real_field_val(name):
    name_lower = name.lower()
    if name_lower == 'bhid_f':
        return "'BHID'"
    elif name_lower == 'xcollar_f':
        return "'XCOLLAR'"
    elif name_lower == 'ycollar_f':
        return "'YCOLLAR'"
    elif name_lower == 'zcollar_f':
        return "'ZCOLLAR'"
    elif name_lower == 'from_f':
        return "'FROM'"
    elif name_lower == 'to_f':
        return "'TO'"
    elif name_lower == 'at_f':
        return "'AT'"
    elif name_lower == 'brg_f':
        return "'BRG'"
    elif name_lower == 'dip_f':
        return "'DIP'"
    elif name_lower in ('x_f', 'xcoord_f'):
        return "'X'"
    elif name_lower in ('y_f', 'ycoord_f'):
        return "'Y'"
    elif name_lower in ('z_f', 'zcoord_f'):
        return "'Z'"
    elif name_lower == 'keys_f':
        return "['BHID']"
    elif name_lower == 'key_f':
        return "'BHID'"
    elif name_lower == 'fields_f':
        return "['AU']"
    elif 'nfield' in name_lower:
        return "'NFIELD'"
    elif 'field' in name_lower:
        return "'AU'"
    return None

def get_real_param_val(name):
    name_lower = name.lower()
    if name_lower == 'inverse_p':
        return '0'
    elif name_lower == 'tripts_p':
        return '1'
    elif name_lower == 'addsymb_p':
        return '0'
    elif name_lower == 'flat_p':
        return '0'
    elif name_lower == 'planmode_p':
        return '1'
    elif name_lower == 'sectmode_p':
        return '1'
    elif 'inverse' in name_lower:
        return '0'
    elif 'mode' in name_lower:
        return '1'
    elif 'type' in name_lower:
        return '1'
    elif 'option' in name_lower:
        return '1'
    elif 'flag' in name_lower:
        return '1'
    elif 'power' in name_lower:
        return '2'
    elif 'radius' in name_lower:
        return '50'
    elif 'dist' in name_lower:
        return '50'
    elif 'resolution' in name_lower:
        return '10'
    elif 'interval' in name_lower:
        return '10'
    elif 'cutoff' in name_lower:
        return '0.5'
    elif 'num' in name_lower:
        return '1'
    elif 'count' in name_lower:
        return '1'
    elif 'max' in name_lower:
        return '100'
    elif 'min' in name_lower:
        return '0'
    return '0'

def get_real_output_val(name, cmd_name_lower, is_list):
    val = f"t_{cmd_name_lower}_out"
    if 'smry' in name.lower() or 'summary' in name.lower():
        val = f"t_{cmd_name_lower}_summary"
    elif 'err' in name.lower() or 'error' in name.lower():
        val = f"t_{cmd_name_lower}_errors"
    elif 'report' in name.lower():
        val = f"t_{cmd_name_lower}_report"
        
    return f"['{val}']" if is_list else f"'{val}'"

def get_real_input_name(name, is_list, cmd_name_lower=''):
    name_lower = name.lower()
    
    # Ensure this is actually an input file parameter
    if not (name_lower.endswith('_i') or name_lower.endswith('mods_i') or name_lower.endswith('files_i') or name_lower in ('in1', 'in2')):
        return None
        
    val = None
    if cmd_name_lower == 'compdh' and name_lower in ('in_i', 'infile_i'):
        val = "'t_dholes'"
    elif 'inmods' in name_lower or 'infiles' in name_lower:
        val = "'t_assays'"
    elif 'collar' in name_lower:
        val = "'t_collars'"
    elif 'survey' in name_lower:
        val = "'t_surveys'"
    elif 'assay' in name_lower:
        val = "'t_assays'"
    elif 'lith' in name_lower or 'lithology' in name_lower:
        val = "'t_lithology'"
    elif 'model' in name_lower or 'proto' in name_lower or 'mod' in name_lower:
        val = "'t_mod1'"
    elif 'wirept' in name_lower or 'wpt' in name_lower:
        val = "'t_SurfacePointsPt'"
    elif 'wiretr' in name_lower or 'wtr' in name_lower:
        val = "'t_SurfaceTriangles'"
    elif 'point' in name_lower or 'pts' in name_lower:
        val = "'t_SurfacePointsPt'"
    elif 'tri' in name_lower or 'wire' in name_lower:
        val = "'t_SurfaceTriangles'"
    elif name_lower == 'estparm_i':
        val = "'t_epar'"
    elif name_lower == 'srcparm_i':
        val = "'t_spar'"
    elif name_lower == 'vmodparm_i':
        val = "'t_vpar'"
    elif name_lower in ('in_i', 'infile_i', 'table_i'):
        val = "'t_assays'"
    elif 'sample' in name_lower:
        val = "'t_assays'"
        
    if val:
        return f"[{val}]" if is_list else val
    return None

def format_param_val(name, default_str, cmd_name_lower, docstring=""):
    is_list = default_str.startswith('[')
    
    # Check if docstring has a valid default/value
    parsed_val = parse_valid_value_from_docstring(name, docstring)
    
    if default_str == 'required':
        if name.endswith('_o') or name.endswith('mods_o') or name.endswith('files_o'):
            val = get_real_output_val(name, cmd_name_lower, is_list)
        else:
            real_input = get_real_input_name(name, is_list, cmd_name_lower)
            if real_input:
                val = real_input
            else:
                if name.endswith('_i') or name.endswith('mods_i') or name.endswith('files_i'):
                    val = "['t_assays']" if is_list else "'t_assays'"
                elif name.endswith('_f'):
                    val = get_real_field_val(name) or ("['FIELD']" if is_list else "'FIELD'")
                else:
                    val = wrap_in_quotes_if_needed(parsed_val) if parsed_val else get_real_param_val(name)
        return val, True
    else:
        # It is optional
        real_input = get_real_input_name(name, is_list, cmd_name_lower)
        if real_input:
            val = real_input
        else:
            real_field = get_real_field_val(name)
            if real_field:
                val = real_field
            elif name.endswith('_o') or name.endswith('mods_o') or name.endswith('files_o'):
                val = get_real_output_val(name, cmd_name_lower, is_list)
            else:
                if default_str == 'optional':
                    if is_list and name.endswith('_f'):
                        val = "['optional_field']"
                    else:
                        val = wrap_in_quotes_if_needed(parsed_val) if parsed_val else "'optional'"
                else:
                    val = wrap_in_quotes_if_needed(default_str)
        return val, False

def generate_notebooks():
    print("Starting process example collection generation...")
    import json
    
    # 1. Get all commands
    commands = agent.list_commands()
    print(f"Found {len(commands)} commands to process.")
    
    # Define directories
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    collections_dir = os.path.join(base_dir, 'tutorials', 'collections')
    
    os.makedirs(collections_dir, exist_ok=True)
    
    # Identify which commands are in dmfiles.init
    cls_file = dmfiles.init
    dmfiles_methods = set()
    for name in dir(cls_file):
        if not name.startswith('_') and callable(getattr(cls_file, name)):
            dmfiles_methods.add(name.lower())
            
    skipped = ['protom', 'estima', 'cokrig', 'extra']
    generated_count = 0
    
    for cmd_info in commands:
        cmd_name = cmd_info['name']
        cmd_name_lower = cmd_name.lower()
        
        if cmd_name_lower not in VERIFIED_COMMANDS:
            continue
            
        # Determine module/wrapper prefix
        is_dmfile = cmd_name_lower in dmfiles_methods
        wrapper_var = "dm_fil" if is_dmfile else "dm_cmd"
        
        # Determine target folder path directly as collections_dir (flat structure)
        folder_path = collections_dir
        
        if cmd_name_lower in skipped:
            print(f"Skipping custom-built example (lives permanently in collections): {cmd_name}")
            generated_count += 1
            continue

        # 2. Get command schema
        try:
            schema = agent.get_command_schema(cmd_name)
        except Exception as e:
            print(f"Error getting schema for {cmd_name}: {e}")
            continue
            
        # 5. Generate notebook
        notebook_filename = os.path.join(folder_path, f"{cmd_name_lower}_example.ipynb")
        
        # Format documentation/description
        docstring = schema.get('doc', '')
        doc_text_markdown = format_doc_to_markdown(docstring)
        
        nb = NotebookBuilder(notebook_filename)
        
        # Cell 1: Title and Header (Beautifully rendered markdown!)
        nb.add_markdown(
            f"# Datamine {cmd_name.upper()} Process Example\n\n"
            f"This notebook demonstrates how to configure and run the **`{cmd_name_lower}`** process wrapper in `dmstudio`.\n\n"
            f"## Process Description\n\n"
            f"{doc_text_markdown}"
        )
        
        # Cell 2: Import & Project Verification (Initialize Sandbox)
        cell2_code = (
            "# Step 1: Connect to Datamine and Initialize Sandbox\n"
            "import os\n"
            "import shutil\n"
            "import glob\n"
            "\n"
            "import pandas as pd\n"
            "\n"
            "from dmstudio import dmcommands, dmfiles, initialize, agent\n\n"
            "# Connect to running Studio RM instance\n"
            "dm_cmd = dmcommands.init(version='StudioRM')\n"
            "dm_fil = dmfiles.init(version='StudioRM')\n"
            "oScript = initialize.studio('StudioRM')\n"
            "print(f\"Connected to: {oScript.Caption}\")\n\n"
            "# Initialize active project sandbox using the shared test_sandbox project\n"
            "notebook_folder = os.path.normpath(os.path.dirname(os.path.abspath('__file__'))).lower()\n"
            "agent.initialize_sandbox(notebook_folder)"
        )
        nb.add_code(cell2_code)
        
        # Cell 3: Introspect Schema
        nb.add_markdown(
            "## Step 2: Introspect Schema\n"
            "Always inspect the parameter schema for the process wrapper to see the expected input and output files, fields, and parameters."
        )
        cell3_code = (
            f"schema = agent.get_command_schema('{cmd_name_lower}')\n"
            "print(f\"Process: {schema['name']}\")\n"
            "print(\"Parameters:\")\n"
            "for p in schema['parameters']:\n"
            "    print(f\"  - {p['name']}: default={p['default']}, annotation={p['annotation']}\")"
        )
        nb.add_code(cell3_code)
        
        # Cell 4: Prepare Inputs (Copy VBOP datasets dynamically)
        nb.add_markdown(
            "## Step 3: Prepare Inputs\n"
            "We initialize the example project by copying the relevant standard datasets from the Datamine database "
            "locally to this sandbox folder using a `t_` prefix."
        )
        cell4_code = (
            "# Step 3: Copy VBOP datasets dynamically from Database to test_sandbox\n"
            "files_to_copy = [\n"
            "    \"_vb_assays.dmx\",\n"
            "    \"_vb_collars.dmx\",\n"
            "    \"_vb_surveys.dmx\",\n"
            "    \"_vb_lithology.dmx\",\n"
            "    \"_vb_epar.dmx\",\n"
            "    \"_vb_spar.dmx\",\n"
            "    \"_vb_vpar.dmx\",\n"
            "    \"_vb_mod1.dmx\",\n"
            "    \"_vb_SurfacePointsPt.dmx\",\n"
            "    \"_vb_SurfaceTriangles.dmx\"\n"
            "]\n\n"
            "agent.copy_database_files(files_to_copy)"
        )
        if cmd_name_lower == 'bhcount':
            cell4_code += (
                "\n\n# Patch t_assays with XC, YC, ZC coordinates required by bhcount\n"
                "df_assays = agent.read_datamine('t_assays.dmx')\n"
                "df_assays['XC'] = 6000.0\n"
                "df_assays['YC'] = 5000.0\n"
                "df_assays['ZC'] = 0.0\n"
                "agent.to_datamine(df_assays, 't_assays.dmx')"
            )
        elif cmd_name_lower == 'compdh':
            cell4_code += (
                "\n\n# Desurvey drillholes using holes3d to create standard sample format required by compdh\n"
                "print(\"Desurveying drillholes with holes3d...\")\n"
                "dm_cmd.holes3d(\n"
                "    collar_i='t_collars',\n"
                "    survey_i='t_surveys',\n"
                "    samples_i=['t_assays'],\n"
                "    out_o='t_dholes'\n"
                ")"
            )
        nb.add_code(cell4_code)
        
        # Cell 5: Execute Process
        nb.add_markdown(
            "## Step 4: Execute Process\n"
            "Call the wrapper method with appropriate arguments. Below is the generated template execution call. "
            "Required parameters are active, and optional parameters are commented out."
        )
        
        # Build command call signature code
        call_lines = []
        call_lines.append(f"# Execute {cmd_name_lower}")
        call_lines.append(f"print(\"Running {cmd_name_lower}...\")")
        call_lines.append(f"{wrapper_var}.{cmd_name_lower}(")
        
        params = schema.get('parameters', [])
        required_params = []
        optional_params = []
        
        for p in params:
            p_name = p['name']
            p_def = p['default']
            formatted_val, is_req = format_param_val(p_name, p_def, cmd_name_lower, docstring)
            if not is_req:
                is_req = is_param_required_in_doc(p_name, docstring)
            if cmd_name_lower == 'anisoang' and p_name in ('wiretr_i', 'wirept_i'):
                is_req = True
            if cmd_name_lower == 'chart' and p_name in ('x_f', 'y_f'):
                is_req = True
            if cmd_name_lower == 'copymod' and p_name == 'modtype_p':
                is_req = True
                formatted_val = '1'
            if cmd_name_lower == 'count' and p_name == 'keys_f':
                is_req = True
            # Force primary input parameters to be required
            if p_name in ('in_i', 'infile_i', 'in1_i', 'table_i', 'inmods_i', 'infiles_i'):
                is_req = True
            if is_req:
                required_params.append(f"    {p_name}={formatted_val},  # required")
            else:
                optional_params.append(f"    # {p_name}={formatted_val},  # optional")
                
        # Combine required and optional
        all_param_lines = required_params + optional_params
        for line in all_param_lines:
            call_lines.append(line)
            
        call_lines.append(")")
        call_lines.append(f"print(\"{cmd_name_lower} execution completed.\")")
        
        cell5_code = '\n'.join(call_lines)
        nb.add_code(cell5_code)
        
        # Cell 6: Verify Results (Functional verification!)
        if cmd_name_lower == 'delete':
            nb.add_markdown(
                "## Step 5: Verify Results\n"
                "Verify that the input file has been successfully deleted from disk."
            )
            cell6_code = (
                "# Step 5: Verify results\n"
                "# The delete process should remove the input file from disk.\n"
                "deleted = True\n"
                "for ext in ['.dmx', '.dm']:\n"
                "    target = f't_assays{ext}'\n"
                "    if os.path.exists(target):\n"
                "        deleted = False\n"
                "        print(f\"Verification Failed: '{target}' still exists on disk.\")\n\n"
                "if deleted:\n"
                "    print(\"Verification Passed: 't_assays' has been successfully deleted from disk.\")"
            )
        else:
            nb.add_markdown(
                "## Step 5: Verify Results\n"
                "Check that output files exist on disk and read them using pandas to verify the outputs."
            )
            cell6_code = (
                "# Step 5: Verify results\n"
                f"output_file = 't_{cmd_name_lower}_out.dmx'\n"
                "if os.path.exists(output_file):\n"
                "    df = agent.read_datamine(output_file)\n"
                "    print(f\"Output file loaded successfully. Rows: {len(df)}\")\n"
                "    print(df.head())\n"
                "else:\n"
                "    print(\"Output file not found (run Step 4 first)\")"
            )
        nb.add_code(cell6_code)
        
        # Cell 7: Cleanup
        nb.add_markdown(
            "## Step 6: Clean up Project Folder\n"
            "Always clean up generated temporary files to keep the directory clean."
        )
        cell7_code = (
            "# Step 6: Clean up temporary files and generated artifacts\n"
            "# 1. Clean up temporary files matching t_*.*\n"
            "temp_files = glob.glob(\"t_*.*\")\n"
            "for f in temp_files:\n"
            "    try:\n"
            "        os.remove(f)\n"
            "        print(f\"Removed {os.path.basename(f)}\")\n"
            "    except Exception as e:\n"
            "        print(f\"Failed to remove {os.path.basename(f)}: {e}\")\n\n"
            "# 2. Clean up dynamic python initialization files (dmdir.py, __init__.py)\n"
            "extra_files = ['dmdir.py', '__init__.py']\n"
            "for f in extra_files:\n"
            "    if os.path.exists(f):\n"
            "        try:\n"
            "            os.remove(f)\n"
            "            print(f\"Removed {f}\")\n"
            "        except Exception as e:\n"
            "            print(f\"Failed to remove {f}: {e}\")\n\n"
            "# 3. Clean up cache directories (__pycache__)\n"
            "pycache = '__pycache__'\n"
            "if os.path.exists(pycache):\n"
            "    try:\n"
            "        shutil.rmtree(pycache)\n"
            "        print(\"Removed __pycache__\")\n"
            "    except Exception as e:\n"
            "        print(f\"Failed to remove __pycache__: {e}\")"
        )
        nb.add_code(cell7_code)
        
        nb.save()
        generated_count += 1
        
    # Clean up old or unverified collection directories/files under tutorials/collections/
    for item in os.listdir(collections_dir):
        item_path = os.path.join(collections_dir, item)
        if os.path.isdir(item_path):
            print(f"Cleaning up old subfolder: {item_path}")
            try:
                shutil.rmtree(item_path, ignore_errors=True)
            except Exception as e:
                print(f"Error removing old subfolder {item}: {e}")
        elif os.path.isfile(item_path):
            if item.endswith('_example.ipynb'):
                cmd_part = item.replace('_example.ipynb', '').lower()
                if cmd_part not in VERIFIED_COMMANDS:
                    print(f"Cleaning up unverified notebook: {item_path}")
                    try:
                        os.remove(item_path)
                    except Exception as e:
                        print(f"Error removing unverified notebook {item}: {e}")
                        
    print(f"Successfully generated/moved {generated_count} process/file example folders and notebooks.")

if __name__ == '__main__':
    generate_notebooks()
