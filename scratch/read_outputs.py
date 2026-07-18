import json

with open('run_tests.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Find the cell that executes the verified core commands
for cell in nb.get('cells', []):
    if cell.get('cell_type') == 'code':
        source_str = "".join(cell.get('source', []))
        if "accmlt,append,cokrig" in source_str:
            for out in cell.get('outputs', []):
                if out.get('output_type') == 'stream':
                    print("".join(out.get('text', [])))
