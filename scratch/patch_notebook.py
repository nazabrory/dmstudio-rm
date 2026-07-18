import json

notebook_path = 'run_tests.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

target_found = False
for cell in nb.get('cells', []):
    if cell.get('cell_type') == 'code':
        source = cell.get('source', [])
        source_str = "".join(source)
        if "copy_notebook_files(src_dir, sandbox_dir)" in source_str:
            new_source = []
            for line in source:
                if "copy_notebook_files(src_dir, sandbox_dir)" in line:
                    indent = line[:line.find("copy_notebook_files")]
                    new_source.append(f"{indent}shutil.copy2(os.path.join(src_dir, nb_file), os.path.join(sandbox_dir, nb_file))\n")
                else:
                    new_source.append(line)
            cell['source'] = new_source
            target_found = True
            break

if target_found:
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)
    print("Successfully patched run_tests.ipynb to copy only the target notebook")
else:
    print("Could not find the target code line to patch")
