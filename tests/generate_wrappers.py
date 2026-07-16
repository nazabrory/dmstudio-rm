import os
import glob
import re

def is_valid_name(name):
    name = name.strip()
    if not name:
        return False
    # Must start with an uppercase letter, and contain only uppercase, digits, hyphens, underscores, parentheses, or spaces
    return bool(re.match(r'^[A-Z][A-Z0-9_\-\(\)\s]*$', name))

def sanitize_python_name(name):
    # Remove surrounding markdown bolding, backticks or asterisks
    name = name.replace('*', '').replace('`', '').strip()
    # Replace spaces and hyphens with underscores
    name = re.sub(r'[-\s]+', '_', name)
    # Remove any other non-alphanumeric characters
    name = re.sub(r'[^A-Za-z0-9_]', '', name)
    # Prepend underscore if it starts with a digit
    if name and name[0].isdigit():
        name = '_' + name
    return name

def expand_wildcard_names(items):
    expanded = []
    for item in items:
        name = item.get('name', '').strip()
        # Matches e.g. IN3 - 20 or F3 - 10
        m = re.match(r'^([A-Za-z_]+)(\d+)\s*-\s*(\d+)$', name)
        if m:
            prefix, start_num, end_num = m.groups()
            start = int(start_num)
            end = int(end_num)
            for k in range(start, end + 1):
                new_item = item.copy()
                new_item['name'] = f"{prefix}{k}"
                expanded.append(new_item)
        else:
            expanded.append(item)
    return expanded

def parse_markdown_table(lines):
    rows = []
    headers = None
    for line in lines:
        line = line.strip()
        if not line or '|' not in line:
            continue
        if line.startswith('|'):
            line = line[1:]
        if line.endswith('|'):
            line = line[:-1]
        parts = [p.strip() for p in line.split('|')]
        if all(re.match(r'^:?-+:?$', p) for p in parts if p):
            continue
        if headers is None:
            headers = [p.strip().replace('*', '').replace('`', '').lower() for p in parts]
        else:
            row_dict = {}
            for idx, h in enumerate(headers):
                val = parts[idx] if idx < len(parts) else ""
                row_dict[h] = val
            name = row_dict.get('name', '').strip()
            name = name.replace('*', '').replace('`', '').strip()
            if not is_valid_name(name):
                continue
            rows.append(row_dict)
    return rows

def parse_parameters_table(lines):
    params = []
    headers = None
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line or '|' not in line:
            i += 1
            continue
        
        if line.startswith('|'):
            line = line[1:]
        if line.endswith('|'):
            line = line[:-1]
            
        parts = [p.strip() for p in line.split('|')]
        if all(re.match(r'^:?-+:?$', p) for p in parts if p):
            i += 1
            continue
            
        if headers is None:
            headers = [p.strip().replace('*', '').replace('`', '').lower() for p in parts]
            i += 1
            continue
            
        row_dict = {}
        for idx, h in enumerate(headers):
            row_dict[h] = parts[idx] if idx < len(parts) else ""
            
        name = row_dict.get('name', '').strip()
        name = name.replace('*', '').replace('`', '').strip()
        if not is_valid_name(name):
            i += 1
            continue
            
        is_option_start = False
        for k, v in row_dict.items():
            if any(term in k.lower() for term in ['required', 'default', 'reqd']):
                if 'option' in str(v).lower() or 'description' in str(v).lower():
                    is_option_start = True
                    break
                
        if is_option_start:
            options_lines = []
            i += 1
            while i < len(lines):
                next_line = lines[i].strip()
                if not next_line:
                    i += 1
                    continue
                if '|' in next_line:
                    options_lines.append(next_line)
                    # Check if this line is the trailing values row (non-separator, >= 3 columns)
                    parts_check = [p.strip() for p in next_line.split('|')]
                    if next_line.startswith('|'):
                        parts_check = parts_check[1:]
                    if next_line.endswith('|'):
                        parts_check = parts_check[:-1]
                    if not all(re.match(r'^:?-+:?$', p) for p in parts_check if p):
                        if len(parts_check) >= 3:
                            i += 1
                            break
                else:
                    break
                i += 1
                
            opt_rows = []
            for opt_line in options_lines:
                if opt_line.startswith('|'):
                    opt_line = opt_line[1:]
                if opt_line.endswith('|'):
                    opt_line = opt_line[:-1]
                opt_parts = [p.strip() for p in opt_line.split('|')]
                if all(re.match(r'^:?-+:?$', p) for p in opt_parts if p):
                    continue
                opt_rows.append(opt_parts)
                
            if opt_rows:
                last_row = opt_rows[-1]
                options = opt_rows[:-1]
                
                try:
                    req_idx = headers.index('required')
                    for j, val in enumerate(last_row):
                        header_idx = req_idx + j
                        if header_idx < len(headers):
                            row_dict[headers[header_idx]] = val
                except ValueError:
                    pass
                    
                desc = row_dict.get('description', '')
                opt_desc_list = []
                for opt in options:
                    if len(opt) >= 2:
                        opt_desc_list.append(f"{opt[0]}: {opt[1]}")
                if opt_desc_list:
                    row_dict['description'] = desc + " Options: " + "; ".join(opt_desc_list)
                    
            params.append(row_dict)
        else:
            params.append(row_dict)
            i += 1
            
    return params

def parse_first_markdown_table(lines):
    table_lines = []
    for line in lines:
        if '|' in line:
            table_lines.append(line)
    return parse_markdown_table(table_lines)

def parse_markdown_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.splitlines()
    if not lines:
        return None
        
    title_match = re.match(r'^#\s+(.*?)\s+(?:Process|Superprocess|Command)', lines[0], re.IGNORECASE)
    if title_match:
        process_name = title_match.group(1).strip().upper()
    else:
        process_name = os.path.basename(filepath).replace('.md', '').upper()

    sections = {}
    current_section = None
    section_lines = []

    for line in lines:
        sec_match = re.match(r'^##+\s+(.*)', line)
        if sec_match:
            sec_name = sec_match.group(1).strip().lower()
            is_level_3 = line.startswith('###')
            is_key_table = sec_name in ['input files', 'output files', 'fields', 'parameters', 'process overview', 'command overview']
            if not is_level_3 or is_key_table:
                if current_section:
                    sections[current_section] = section_lines
                current_section = sec_name
                section_lines = []
            else:
                if current_section:
                    section_lines.append(line)
        else:
            if current_section:
                section_lines.append(line)

    if current_section:
        sections[current_section] = section_lines

    if process_name == 'COKRIG':
        input_files = [
            {'name': 'SAMPLES', 'required': 'Yes', 'type': 'Table', 'description': 'Input sample data file containing X, Y, Z coordinates and grade fields.'},
            {'name': 'PROTO', 'required': 'Yes', 'type': 'Block Model', 'description': 'Prototype block model into which estimates will be made.'},
            {'name': 'FIELDS', 'required': 'Yes', 'type': 'Table', 'description': 'Estimation fields list file specifying grades to be estimated and output fields.'},
            {'name': 'EPAR', 'required': 'Yes', 'type': 'Table', 'description': 'Estimation parameters file defining methods, search and variogram volumes.'},
            {'name': 'SPAR', 'required': 'Yes', 'type': 'Table', 'description': 'Search parameter file defining search volumes and sample counts.'},
            {'name': 'VMODEL', 'required': 'No', 'type': 'Table', 'description': 'Variogram model parameter file (required for kriging methods).'},
            {'name': 'ZPAR', 'required': 'No', 'type': 'Table', 'description': 'Custom zone/soft boundary parameter file.'},
            {'name': 'STRING', 'required': 'No', 'type': 'String', 'description': 'Input boundary string file for unfolding option.'},
            {'name': 'UNFOLD', 'required': 'No', 'type': 'Table', 'description': 'Input unfolding parameter file.'}
        ]
        output_files = [
            {'name': 'OUTMODEL', 'required': 'Yes', 'type': 'Block Model', 'description': 'Output model containing estimated grades, variance, etc.'},
            {'name': 'SAMPOUT', 'required': 'No', 'type': 'Table', 'description': 'Output sample file containing weights details.'}
        ]
        fields = [
            {'name': 'XPT', 'required': 'No', 'type': 'Numeric', 'default': 'XPT', 'description': 'X coordinate field in sample data.'},
            {'name': 'YPT', 'required': 'No', 'type': 'Numeric', 'default': 'YPT', 'description': 'Y coordinate field in sample data.'},
            {'name': 'ZPT', 'required': 'No', 'type': 'Numeric', 'default': 'ZPT', 'description': 'Z coordinate field in sample data.'},
            {'name': 'ZONE1_F', 'required': 'No', 'type': 'Any', 'default': 'Undefined', 'description': 'First zone control field name.'},
            {'name': 'ZONE2_F', 'required': 'No', 'type': 'Any', 'default': 'Undefined', 'description': 'Second zone control field name.'},
            {'name': 'KEY', 'required': 'No', 'type': 'Numeric', 'default': 'Undefined', 'description': 'Key field for limiting sample counts.'}
        ]
        parameters = [
            {'name': 'MERGEST', 'required': 'No', 'default': '1', 'range': '0,1', 'values': '0,1', 'description': 'Flag to control merging of consistent search/variogram parameters.'}
        ]
    else:
        input_files = parse_first_markdown_table(sections.get('input files', []))
        output_files = parse_first_markdown_table(sections.get('output files', []))
        fields = parse_first_markdown_table(sections.get('fields', []))
        parameters = parse_parameters_table(sections.get('parameters', []))

        input_files = expand_wildcard_names(input_files)
        output_files = expand_wildcard_names(output_files)
        fields = expand_wildcard_names(fields)
        parameters = expand_wildcard_names(parameters)
    
    overview_lines = sections.get('process overview', []) or sections.get('command overview', [])
    overview = "\n".join(overview_lines).strip()

    return {
        'name': process_name,
        'overview': overview,
        'input_files': input_files,
        'output_files': output_files,
        'fields': fields,
        'parameters': parameters
    }

def group_sequential_items(items, item_type):
    import collections
    numbered_groups = collections.defaultdict(list)
    for idx, item in enumerate(items):
        name = item.get('name', '').strip()
        m = re.match(r'^([A-Za-z_]+)(\d+)$', name)
        if m:
            prefix, num = m.groups()
            numbered_groups[prefix].append((int(num), idx, item))

    grouped_indices = set()
    list_groups = {}
    for prefix, group in numbered_groups.items():
        if len(group) >= 2:
            group.sort()
            base = prefix.lower()
            if base == 'key':
                plural = 'keys'
            elif base == 'f':
                plural = 'fields'
            elif base == 'inmod':
                plural = 'inmods'
            elif base == 'in':
                plural = 'inmods'
            elif base == 'sample':
                plural = 'samples'
            elif base == 'datafld':
                plural = 'dataflds'
            elif base == 'attrib':
                plural = 'attribs'
            elif base == 'grade':
                plural = 'grades'
            elif base == 'priorty' or base == 'priority':
                plural = 'priorties'
            elif base == 'addfld':
                plural = 'addflds'
            elif base == 'domfld':
                plural = 'domflds'
            elif base == 'vwfld':
                plural = 'vwflds'
            elif base == 'minfld':
                plural = 'minflds'
            elif base == 'maxfld':
                plural = 'maxflds'
            elif base == 'addf':
                plural = 'addfs'
            elif base == 'datfld':
                plural = 'datflds'
            elif base == 'vwf':
                plural = 'vwflds'
            elif base == 'minf':
                plural = 'minflds'
            elif base == 'maxf':
                plural = 'maxflds'
            else:
                plural = base + 's'

            suffix = 'i' if item_type == 'file' else ('o' if item_type == 'output' else 'f')
            list_name = f"{plural}_{suffix}"

            list_groups[list_name] = {
                'prefix': prefix.lower(),
                'max_fields': max(num for num, _, _ in group),
                'symbol': '&' if item_type == 'file' else ('*' if item_type == 'field' else '@'),
                'description': group[0][2].get('description', '')
            }

            for _, idx, _ in group:
                grouped_indices.add(idx)

    final_items = []
    added_groups = set()
    for idx, item in enumerate(items):
        if idx in grouped_indices:
            name = item.get('name', '').strip()
            prefix = re.match(r'^([A-Za-z_]+)\d+$', name).group(1)
            for list_name, info in list_groups.items():
                if info['prefix'] == prefix.lower():
                    if list_name not in added_groups:
                        final_items.append({
                            'name': list_name,
                            'is_list': True,
                            'max_fields': info['max_fields'],
                            'prefix': info['prefix'],
                            'symbol': info['symbol'],
                            'required': 'No',
                            'default': 'optional',
                            'description': info['description']
                        })
                        added_groups.add(list_name)
                    break
        else:
            final_items.append({
                'name': item.get('name', '').strip(),
                'is_list': False,
                'required': item.get('required', 'No'),
                'default': item.get('default', 'optional'),
                'description': item.get('description', ''),
                'range': item.get('range', 'Undefined'),
                'values': item.get('values', 'Undefined')
            })

    return final_items, list_groups

def parse_default_value(val_str, required_str):
    if required_str.strip().lower() in ['yes', 'true']:
        return '"required"'
    val_str = val_str.strip()
    if not val_str or val_str.lower() in ['undefined', 'none', 'optional']:
        return '"optional"'
    try:
        if '.' in val_str:
            return str(float(val_str))
        else:
            return str(int(val_str))
    except ValueError:
        val_str = val_str.replace("'", "").replace('"', "").replace("(", "").replace(")", "")
        return f"'{val_str}'"

def wrap_lines(text, indent_level, max_len=100):
    indent = " " * indent_level
    if not text:
        return []
    words = text.split()
    lines = []
    current_line = []
    current_len = len(indent)
    for word in words:
        if current_len + len(word) + 1 > max_len:
            lines.append(indent + " ".join(current_line))
            current_line = [word]
            current_len = len(indent) + len(word)
        else:
            current_line.append(word)
            current_len += len(word) + 1
    if current_line:
        lines.append(indent + " ".join(current_line))
    return lines

def generate_docstring(info, list_groups):
    doc = []
    doc.append(f'        r"""')
    doc.append(f'        {info["name"]}')
    doc.append(f'        {"-" * len(info["name"])}')
    if info["overview"]:
        doc.append(f'        {info["overview"]}\n')
    else:
        doc.append(f'        This is auto-generated documentation. For more command information visit the Datamine help file.\n')

    doc.append(f'        Input Files:')
    doc.append(f'        ------------\n')
    for f in info['input_files']:
        name = sanitize_python_name(f.get('name', '')).lower()
        required = 'Yes' if f.get('required', '').lower() in ['yes', 'true'] else 'No'
        doc.append(f'        {name}: {f.get("type", "Table")}')
        desc = f.get('description', '')
        for line in wrap_lines(desc, 12, 100):
            doc.append(line)
        doc.append(f'            Required={required}\n')

    doc.append(f'        Output Files:')
    doc.append(f'        -------------\n')
    for f in info['output_files']:
        name = sanitize_python_name(f.get('name', '')).lower()
        required = 'Yes' if f.get('required', '').lower() in ['yes', 'true'] else 'No'
        doc.append(f'        {name}: {f.get("type", "Table")}')
        desc = f.get('description', '')
        for line in wrap_lines(desc, 12, 100):
            doc.append(line)
        doc.append(f'            Required={required}\n')

    doc.append(f'        Fields:')
    doc.append(f'        -------\n')
    
    grouped_prefixes = [g['prefix'] for g in list_groups.values()]
    documented_lists = set()
    
    for f in info['fields']:
        raw_name = f.get('name', '').strip()
        name = sanitize_python_name(raw_name).lower()
        m = re.match(r'^([A-Za-z_]+)(\d+)$', name)
        if m and m.group(1).lower() in grouped_prefixes:
            prefix = m.group(1).lower()
            list_name = [ln for ln, g in list_groups.items() if g['prefix'] == prefix][0]
            if list_name not in documented_lists:
                doc.append(f'        {list_name.split("_")[0]}: Undefined : Undefined')
                doc.append(f'            {f.get("description", "")}')
                doc.append(f'            Default=Undefined')
                doc.append(f'            Required=No\n')
                documented_lists.add(list_name)
            continue
            
        required = 'Yes' if f.get('required', '').lower() in ['yes', 'true'] else 'No'
        doc.append(f'        {name}: {f.get("type", "Undefined")} : {f.get("source", "Undefined")}')
        desc = f.get('description', '')
        for line in wrap_lines(desc, 12, 100):
            doc.append(line)
        doc.append(f'            Default={f.get("default", "Undefined")}')
        doc.append(f'            Required={required}\n')

    doc.append(f'        Parameters:')
    doc.append(f'        -----------\n')
    for p in info['parameters']:
        name = sanitize_python_name(p.get('name', '')).lower()
        required = 'Yes' if p.get('required', '').lower() in ['yes', 'true'] else 'No'
        doc.append(f'        {name}:')
        desc = p.get('description', '')
        for line in wrap_lines(desc, 12, 100):
            doc.append(line)
        doc.append(f'            Range={p.get("range", "Undefined")}')
        doc.append(f'            Values={p.get("values", "Undefined")}')
        doc.append(f'            Default={p.get("default", "Undefined")}')
        doc.append(f'            Required={required}\n')

    doc.append(f'        """')
    return "\n".join(doc)

def generate_validation_code(p_name, arg_name, range_str, values_str, default_str=None):
    validation_lines = []
    
    has_values = False
    allowed_values = []
    if values_str and values_str.lower() != 'undefined':
        parts = [p.strip() for p in values_str.split(',') if p.strip()]
        if parts:
            try:
                allowed_values = [float(p) for p in parts]
                has_values = True
            except ValueError:
                pass
                
    if has_values and default_str:
        try:
            default_val = float(default_str.strip().replace("'", "").replace('"', ""))
            if default_val not in allowed_values:
                allowed_values.append(default_val)
        except ValueError:
            pass

    has_range = False
    min_val, max_val = None, None
    if range_str and range_str.lower() != 'undefined':
        parts = [p.strip() for p in range_str.split(',') if p.strip()]
        if len(parts) == 2:
            try:
                min_val = float(parts[0])
                max_val = float(parts[1])
                has_range = True
            except ValueError:
                pass
                
    if has_values:
        val_list_str = ", ".join(str(int(v) if v.is_integer() else v) for v in allowed_values)
        validation_lines.append(f"        if {arg_name} != \"optional\":")
        validation_lines.append(f"            try:")
        validation_lines.append(f"                val = float({arg_name})")
        validation_lines.append(f"                if val not in {allowed_values}:")
        validation_lines.append(f"                    raise ValueError(f\"{arg_name} value {{{arg_name}}} is not in allowed values: [{val_list_str}]\")")
        validation_lines.append(f"            except ValueError as e:")
        validation_lines.append(f"                if isinstance({arg_name}, (int, float)):")
        validation_lines.append(f"                    raise e")
    elif has_range:
        validation_lines.append(f"        if {arg_name} != \"optional\":")
        validation_lines.append(f"            try:")
        validation_lines.append(f"                val = float({arg_name})")
        if default_str:
            try:
                default_val = float(default_str.strip().replace("'", "").replace('"', ""))
                validation_lines.append(f"                if not ({min_val} <= val <= {max_val}) and val != {default_val}:")
            except ValueError:
                validation_lines.append(f"                if not ({min_val} <= val <= {max_val}):")
        else:
            validation_lines.append(f"                if not ({min_val} <= val <= {max_val}):")
        validation_lines.append(f"                    raise ValueError(f\"{arg_name} value {{{arg_name}}} is not in allowed range: [{min_val}, [{max_val}]\")")
        validation_lines.append(f"            except ValueError as e:")
        validation_lines.append(f"                if isinstance({arg_name}, (int, float)):")
        validation_lines.append(f"                    raise e")
        
    return "\n".join(validation_lines)

def generate_python_function(info):
    # Determine lists
    input_files_grouped, in_list_groups = group_sequential_items(info['input_files'], 'file')
    output_files_grouped, out_list_groups = group_sequential_items(info['output_files'], 'output')
    fields_grouped, field_list_groups = group_sequential_items(info['fields'], 'field')
    parameters_grouped, param_list_groups = group_sequential_items(info['parameters'], 'parameter')

    all_list_groups = {}
    all_list_groups.update(in_list_groups)
    all_list_groups.update(out_list_groups)
    all_list_groups.update(field_list_groups)
    all_list_groups.update(param_list_groups)

    # Pre-populate unique Python names to prevent duplicate argument errors
    seen_args = set()
    def get_unique_arg_name(base_name, suffix):
        candidate = f"{base_name}_{suffix}"
        if candidate in seen_args:
            counter = 2
            while f"{base_name}{counter}_{suffix}" in seen_args:
                counter += 1
            candidate = f"{base_name}{counter}_{suffix}"
        seen_args.add(candidate)
        return candidate

    # Pre-allocate zone/dom arguments to seen_args to avoid collisions
    for f in fields_grouped:
        name = sanitize_python_name(f['name']).lower()
        if not f.get('is_list'):
            if 'zone_n' in name or 'zonen' in name:
                for k in range(1, 6):
                    zname = 'zone' if k == 1 else f'zone{k}'
                    seen_args.add(f"{zname}_f")
            elif 'dom1_5' in name or 'dom15' in name:
                for k in range(1, 6):
                    seen_args.add(f"dom{k}_f")

    # Inputs unique name assignment
    for f in input_files_grouped:
        if f.get('is_list'):
            f['py_name'] = f['name']
        else:
            base = sanitize_python_name(f['name']).lower()
            f['py_name'] = get_unique_arg_name(base, 'i')

    # Outputs unique name assignment
    for f in output_files_grouped:
        if f.get('is_list'):
            f['py_name'] = f['name']
        else:
            base = sanitize_python_name(f['name']).lower()
            f['py_name'] = get_unique_arg_name(base, 'o')

    # Fields unique name assignment
    for f in fields_grouped:
        if f.get('is_list'):
            f['py_name'] = f['name']
        else:
            name = sanitize_python_name(f['name']).lower()
            if 'zone_n' in name or 'zonen' in name:
                f['py_name'] = 'zone_f' # special marker, expanded separately
            elif 'dom1_5' in name or 'dom15' in name:
                f['py_name'] = 'dom1_f' # special marker, expanded separately
            else:
                base = sanitize_python_name(f['name']).lower()
                f['py_name'] = get_unique_arg_name(base, 'f')

    # Parameters unique name assignment
    for p in parameters_grouped:
        if p.get('is_list'):
            p['py_name'] = p['name']
        else:
            base = sanitize_python_name(p['name']).lower()
            p['py_name'] = get_unique_arg_name(base, 'p')

    # Build signature args
    args = []
    
    # Inputs
    for f in input_files_grouped:
        if f.get('is_list'):
            args.append(f"{f['py_name']}=['optional']")
        else:
            default = parse_default_value(f.get('default', 'optional'), f.get('required', 'No'))
            args.append(f"{f['py_name']}={default}")

    # Outputs
    for f in output_files_grouped:
        if f.get('is_list'):
            args.append(f"{f['py_name']}=['optional']")
        else:
            default = parse_default_value(f.get('default', 'optional'), f.get('required', 'No'))
            args.append(f"{f['py_name']}={default}")

    # Fields
    for f in fields_grouped:
        if f.get('is_list'):
            args.append(f"{f['py_name']}=['optional']")
        else:
            name = sanitize_python_name(f['name']).lower()
            if 'zone_n' in name or 'zonen' in name:
                for k in range(1, 6):
                    zname = 'zone' if k == 1 else f'zone{k}'
                    args.append(f"{zname}_f=\"optional\"")
            elif 'dom1_5' in name or 'dom15' in name:
                for k in range(1, 6):
                    args.append(f"dom{k}_f=\"optional\"")
            else:
                args.append(f"{f['py_name']}=\"optional\"")

    # Parameters
    for p in parameters_grouped:
        if p.get('is_list'):
            args.append(f"{p['py_name']}=['optional']")
        else:
            default = parse_default_value(p.get('default', 'optional'), p.get('required', 'No'))
            args.append(f"{p['py_name']}={default}")

    args.append('arguments="optional"')
    args.append('retrieval="optional"')

    # Function signature
    fn_name = sanitize_python_name(info['name']).lower()
    sig = f"    def {fn_name}(self,\n"
    for arg in args:
        sig += f"                {arg},\n"
    sig = sig[:-2] + "):\n\n"

    # Docstring
    docstring = generate_docstring(info, all_list_groups)

    # Function body
    body = []
    body.append(f'        command = "{info["name"].lower()} "')
    body.append("")

    # Required check for inputs
    for f in input_files_grouped:
        if f.get('is_list'):
            continue
        name = f['py_name']
        required = f.get('required', '').lower() in ['yes', 'true']
        if required:
            body.append(f'        if {name} == "required":')
            body.append(f'            raise ValueError("{name} is required.")')
            body.append("")
        body.append(f'        if {name} != "optional":')
        body.append(f'            command += " &{f["name"].lower()}=" + {name}')
        body.append("")

    for f in output_files_grouped:
        if f.get('is_list'):
            continue
        name = f['py_name']
        required = f.get('required', '').lower() in ['yes', 'true']
        if required:
            body.append(f'        if {name} == "required":')
            body.append(f'            raise ValueError("{name} is required.")')
            body.append("")
        body.append(f'        if {name} != "optional":')
        body.append(f'            command += " &{f["name"].lower()}=" + {name}')
        body.append("")

    # Fields
    for f in fields_grouped:
        if f.get('is_list'):
            continue
        name = f['py_name']
        raw_name = sanitize_python_name(f['name']).lower()
        if 'zone_n' in raw_name or 'zonen' in raw_name:
            for k in range(1, 6):
                zname = 'zone' if k == 1 else f'zone{k}'
                body.append(f'        if {zname}_f != "optional":')
                body.append(f'            command += " *{zname}=" + {zname}_f')
                body.append("")
        elif 'dom1_5' in raw_name or 'dom15' in raw_name:
            for k in range(1, 6):
                body.append(f'        if dom{k}_f != "optional":')
                body.append(f'            command += " *dom{k}=" + dom{k}_f')
                body.append("")
        else:
            body.append(f'        if {name} != "optional":')
            body.append(f'            command += " *{f["name"].lower()}=" + {name}')
            body.append("")

    # Lists handling
    for list_name, linfo in all_list_groups.items():
        body.append(f'        if {list_name}[0] != "optional":')
        body.append(f'            command += self.parse_infields_list("{linfo["prefix"]}", {list_name}, {linfo["max_fields"]}, "{linfo["symbol"]}")')
        body.append("")

    # Parameters
    for p in parameters_grouped:
        if p.get('is_list'):
            continue
        name = p['py_name']
        required = p.get('required', '').lower() in ['yes', 'true']
        if required:
            body.append(f'        if {name} == "required":')
            body.append(f'            raise ValueError("{name} is required.")')
            body.append("")
            
        validation_code = generate_validation_code(p['name'], name, p.get('range', 'Undefined'), p.get('values', 'Undefined'), p.get('default', 'optional'))
        if validation_code:
            body.append(validation_code)
            body.append("")

        body.append(f'        if {name} != "optional":')
        body.append(f'            command += " @{p["name"].lower()}=" + str({name})')
        body.append("")

    body.append(f'        if arguments != "optional":')
    body.append(f'            command += " " + arguments')
    body.append("")

    body.append(f'        if retrieval != "optional":')
    body.append(f'            command += "{{" + retrieval + "}}"')
    body.append("")

    body.append(f'        self.run_command(command)')
    body.append("")

    full_body = "\n".join(body)
    return sig + docstring + "\n" + full_body

# Setup Directories and glob markdown files
help_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "datamine help", "StudioRM", "Process_Help_XML")
files = glob.glob(os.path.join(help_dir, "*.md"))

commands_funcs = []
files_funcs = []

for filepath in files:
    info = parse_markdown_file(filepath)
    if not info:
        continue
    
    has_inputs = len(info['input_files']) > 0
    
    func_code = generate_python_function(info)
    if has_inputs:
        commands_funcs.append((info['name'], func_code))
    else:
        files_funcs.append((info['name'], func_code))

# Sort alphabetically by process name
commands_funcs.sort(key=lambda x: x[0])
files_funcs.sort(key=lambda x: x[0])

# Prepare dmcommands.py content
commands_boilerplate = """import dmstudio.initialize


# constant to avoid redundant COM connections which slows down processing
OSCRIPTCON = None

class init(object):

    def __init__(self, version=None):

        \"\"\"
        commands.__init__
        ------------------


        Commands initialization. After the commands class is initialized  for the first time the object will
         be set to the datamine studio object. This property will avoid redundant initializaiton

        Parameters:
        -----------

        version: str
            optional datamine studio versions ('Studio3', 'StudioRM', 'StudioRM3.1', 'StudioRM3.2', 'StudioEM') If no version given, the initializtion
            will try different versions starting with StudioRM then Studio3 and finally StudioEM.

        \"\"\"
        self.oScript = OSCRIPTCON
        self.version = version
        if self.oScript is None:
            self.oScript = dmstudio.initialize.studio(self.version)

    def run_command(self, command):

        \"\"\"
        run_command
        -----------

        Uses the studio Parsecommand method to execute a datamine script.

        Parameters:
        -----------

        command: str
            Datamine command string to be parsed
        \"\"\"

        self.oScript.Parsecommand(command)

        # update the dmdir.py file containing list of .dm files in current directory

        # dmstudio.initialize._make_dmdir()


    def parse_infields_list(self, prefix, fields, maxfields, vtype='*'):

        \"\"\"
        parse_infields_list
        -------------------

        Intenal function for parsing a list of *fields to a string for use in studio commands e.g. *F1, *F2, etc..

        Parameters
        ----------

        prefix: str
            starting letter or letters for the field e.g. 'F' for *F1.
        fields: list of str
            list of input fields
        maxfields: int
            maximum number of fields permitted by datamine command
        vtype: str
            variable type, input file or field. For input file vtype="&" for field vtype="*"

        Returns:
        --------

        field_string: str
            concatenated string formated for input in datamine commands

        \"\"\"

        if maxfields < len(fields):
            raise ValueError("More fields have been selected than allowed by Datamine command")

        field_string = ""
        for i, field in enumerate(fields):
            field_string += " " + vtype + prefix + str(i + 1) + "=" + field + " "

        return field_string;
"""

commands_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "dmstudio", "dmcommands.py")
with open(commands_path, "w", encoding="utf-8") as f:
    f.write(commands_boilerplate)
    f.write("\n")
    for name, code in commands_funcs:
        f.write(code)
        f.write("\n")

# Prepare dmfiles.py content
files_boilerplate = """'''
dmstudio.dmfiles
================

All datamine commands which do not use input files. The commands are mainly for generating datamine files such as ``inpfil``, ``protom`` etc.

To do:
------

* Replace multiple field/file inputs with input lists e.g. *f1, *f2... -> fields_f=['f1', 'f2']
* Exhaustive testing and debugging
* Use the same field parsing as ``dmcommands``

'''
import dmstudio.initialize

# constant to avoid redundant COM connections which slows down processing

OSCRIPTCON = None

class init(object):

    def __init__(self, version=None):

        '''
        commands.__init__
        ------------------


        Commands initialization. After the commands class is initialized  for the first time the object will
         be set to the datamine studio object. This property will avoid redundant initializaiton

        Parameters:
        -----------

        version: str
            optional datamine studio versions ('Studio3', 'StudioRM', 'StudioRM3.1', 'StudioRM3.2', 'StudioEM') If no version given, the initializtion
            will try different versions starting with StudioRM then Studio3 and finally StudioEM.

        '''
        self.oScript = OSCRIPTCON
        self.version = version
        if self.oScript is None:
            self.oScript = dmstudio.initialize.studio(self.version)

    def run_command(self, command):
        '''
        run_command
        -----------

        Uses the studio Parsecommand method to execute a datamine script.

        Parameters:
        -----------

        command: str
            datamine command string to be parsed
        '''

        try:
            self.oScript.Parsecommand(command)
        except Exception as e:
            print("Unexpected error:", e)

    def parse_infields_list(self, prefix, fields, maxfields=10, vtype='*'):

        \"\"\"
        parse_infields_list
        -------------------

        Intenal function for parsing a list of *fields to a string for use in studio commands e.g. *F1, *F2, etc..

        Parameters
        ----------

        prefix: str
            starting letter or letters for the field e.g. 'F' for *F1.
        fields: list of str
            list of input fields
        maxfields: int
            maximum number of fields permitted by datamine command
        vtype: str
            variable type, input file or field. For input file vtype="&" for field vtype="*"

        Returns:
        --------

        field_string: str
            concatenated string formated for input in datamine commands

        \"\"\"

        if maxfields < len(fields):
            raise ValueError("More fields have been selected than allowed by Datamine command")

        field_string = ""
        for i, field in enumerate(fields):
            field_string += " " + vtype + prefix + str(i + 1) + "=" + field + " "

        return field_string;
"""

files_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "dmstudio", "dmfiles.py")
with open(files_path, "w", encoding="utf-8") as f:
    f.write(files_boilerplate)
    f.write("\n")
    for name, code in files_funcs:
        f.write(code)
        f.write("\n")

print(f"Generated {len(commands_funcs)} commands in dmcommands.py and {len(files_funcs)} files in dmfiles.py.")
