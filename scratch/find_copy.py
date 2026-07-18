import json

with open('run_tests.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for idx, cell in enumerate(nb.get('cells', [])):
    if cell.get('cell_type') == 'code':
        source_str = "".join(cell.get('source', []))
        if "copy_notebook_files" in source_str:
            print(f"Cell {idx} contains 'copy_notebook_files':")
            print(source_str)
