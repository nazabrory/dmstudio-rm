import os
import sys
import shutil
import inspect
import re

# Add parent directory to path so dmstudio is importable when run from tests/
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dmstudio import agent, dmcommands, dmfiles
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
            look_ahead = docstring[start_idx : start_idx + 600]
            if re.search(r'Required\s*=\s*Yes', look_ahead, re.IGNORECASE):
                return True
                
    return False

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
    elif name_lower in ('keys_f', 'key_f'):
        return "['BHID']"
    elif name_lower == 'fields_f':
        return "['AU']"
    return None

def get_real_output_val(name, cmd_name_lower):
    is_list = name.endswith('s_o') or name.endswith('mods_o') or name.endswith('files_o')
    val = f"t_{cmd_name_lower}_out"
    if 'smry' in name.lower() or 'summary' in name.lower():
        val = f"t_{cmd_name_lower}_summary"
    elif 'err' in name.lower() or 'error' in name.lower():
        val = f"t_{cmd_name_lower}_errors"
    elif 'report' in name.lower():
        val = f"t_{cmd_name_lower}_report"
        
    return f"['{val}']" if is_list else f"'{val}'"

def get_real_input_name(name):
    name_lower = name.lower()
    
    # Ensure this is actually an input file parameter
    if not (name_lower.endswith('_i') or name_lower.endswith('mods_i') or name_lower.endswith('files_i') or name_lower in ('in1', 'in2')):
        return None
        
    is_list = name_lower.endswith('s_i') or name_lower.endswith('mods_i') or name_lower.endswith('files_i')
    
    val = None
    if 'collar' in name_lower:
        val = "'t_collars'"
    elif 'survey' in name_lower:
        val = "'t_surveys'"
    elif 'assay' in name_lower:
        val = "'t_assays'"
    elif 'lith' in name_lower or 'lithology' in name_lower:
        val = "'t_lithology'"
    elif 'model' in name_lower or 'proto' in name_lower:
        val = "'t_mod1'"
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

def format_param_val(name, default_str, cmd_name_lower):
    is_list = default_str.startswith('[') or name.endswith('s_i') or name.endswith('s_o') or name.endswith('s_f') or name.endswith('s_p')
    
    if default_str == 'required':
        if name.endswith('_o') or name.endswith('mods_o') or name.endswith('files_o'):
            val = get_real_output_val(name, cmd_name_lower)
        else:
            real_input = get_real_input_name(name)
            if real_input:
                val = real_input
            else:
                if name.endswith('_i') or name.endswith('mods_i') or name.endswith('files_i'):
                    val = "['t_input_file']" if is_list else "'t_input_file'"
                elif name.endswith('_f'):
                    val = get_real_field_val(name) or ("['FIELD']" if is_list else "'FIELD'")
                else:
                    val = "'required_val'"
        return val, True
    else:
        # It is optional
        real_input = get_real_input_name(name)
        if real_input:
            val = real_input
        else:
            real_field = get_real_field_val(name)
            if real_field:
                val = real_field
            elif name.endswith('_o') or name.endswith('mods_o') or name.endswith('files_o'):
                val = get_real_output_val(name, cmd_name_lower)
            else:
                if default_str == 'optional':
                    val = "['optional_field']" if is_list and name.endswith('_f') else "'optional'"
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
    project_template = os.path.join(base_dir, 'tutorials', 'Project.rmproj')
    
    if not os.path.exists(project_template):
        raise FileNotFoundError(f"Project template not found at: {project_template}")
        
    os.makedirs(collections_dir, exist_ok=True)
    
    # Identify which commands are in dmfiles.init
    cls_file = dmfiles.init
    dmfiles_methods = set()
    for name in dir(cls_file):
        if not name.startswith('_') and callable(getattr(cls_file, name)):
            dmfiles_methods.add(name.lower())
            
    skipped = ['protom', 'estima', 'cokrig']
    generated_count = 0
    
    for cmd_info in commands:
        cmd_name = cmd_info['name']
        cmd_name_lower = cmd_name.lower()
        
        # Determine module/wrapper prefix
        is_dmfile = cmd_name_lower in dmfiles_methods
        wrapper_var = "dm_fil" if is_dmfile else "dm_cmd"
        
        # Determine target folder path based on whether it is a process or file command
        target_subfolder = 'files' if is_dmfile else 'processes'
        folder_path = os.path.join(collections_dir, target_subfolder, cmd_name_lower)
        os.makedirs(folder_path, exist_ok=True)
        
        if cmd_name_lower in skipped:
            print(f"Handling custom-built example: {cmd_name}")
            dest_notebook = os.path.join(folder_path, f"{cmd_name_lower}_example.ipynb")
            src_notebook = os.path.join(base_dir, 'tutorials', 'custom_notebooks', f"{cmd_name_lower}_example.ipynb")
            if os.path.exists(src_notebook):
                with open(src_notebook, 'r', encoding='utf-8') as f_in:
                    nb_data = json.load(f_in)
                with open(dest_notebook, 'w', encoding='utf-8') as f_out:
                    json.dump(nb_data, f_out, indent=2)
                print(f"Copied custom notebook: {dest_notebook}")
                generated_count += 1
            else:
                print(f"Warning: Custom notebook not found at: {src_notebook}")
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
            "import pandas as pd\n"
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
            "agent.initialize_sandbox(notebook_folder, files_to_copy=files_to_copy)"
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
            formatted_val, is_req = format_param_val(p_name, p_def, cmd_name_lower)
            if not is_req:
                is_req = is_param_required_in_doc(p_name, docstring)
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
        
    # Clean up old collections directories (anything in tutorials/collections/ that is not 'processes' or 'files')
    for item in os.listdir(collections_dir):
        item_path = os.path.join(collections_dir, item)
        if os.path.isdir(item_path) and item not in ('processes', 'files'):
            print(f"Cleaning up old folder: {item}")
            try:
                shutil.rmtree(item_path)
            except Exception as e:
                print(f"Error removing old folder {item}: {e}")
                
    print(f"Successfully generated/moved {generated_count} process/file example folders and notebooks.")

if __name__ == '__main__':
    generate_notebooks()
