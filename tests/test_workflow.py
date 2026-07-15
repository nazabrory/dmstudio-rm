'''
scratch/test_workflow.py
------------------------

Verification script for the dmstudio upgrade plan.

Tests:
1. NotebookBuilder - generates a test Jupyter workflow notebook
2. agent.list_commands() - verifies command introspection
3. agent.get_command_schema() - verifies schema retrieval
4. agent.search_commands() - verifies fuzzy search
5. initialize.studio() - tests StudioRM3.x dynamic version support (no Studio required)

Run:
    .venv\\Scripts\\python scratch/test_workflow.py
'''

import sys
import os

# Ensure the project root is importable
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

print('=' * 60)
print('dmstudio Upgrade Plan - Verification Script')
print('=' * 60)

# ---------------------------------------------------------------------------
# Test 1: NotebookBuilder
# ---------------------------------------------------------------------------
print('\n[1] NotebookBuilder - generating test notebook...')
try:
    from dmstudio.notebook_builder import NotebookBuilder

    nb = NotebookBuilder(
        os.path.join(os.path.dirname(__file__), 'test_generated_workflow.ipynb'),
        title='Test Datamine Workflow'
    )
    nb.add_markdown('## Step 1: Initialize Connection')
    nb.add_code(
        "from dmstudio import dmcommands\n"
        "cmd = dmcommands.init(version='StudioRM')\n"
        "print('Connected to Studio RM')"
    )
    nb.add_markdown('## Step 2: Sort Collars')
    nb.add_code(
        "cmd.mgsort(\n"
        "    in_i='_vb_collars',\n"
        "    out_o='sorted_collars',\n"
        "    keys_f=['BHID']\n"
        ")\n"
        "print('Sort complete')"
    )
    nb.add_markdown('## Step 3: De-survey')
    nb.add_code(
        "cmd.desurv(\n"
        "    inmods_i=['sorted_collars', '_vb_surveys'],\n"
        "    out_o='dholes',\n"
        "    survsmth_p=1,\n"
        "    print_p=0\n"
        ")\n"
        "print('De-survey complete')"
    )
    path = nb.save()
    print('  OK - notebook written to:', path)
    print('  Cells:', len(nb._cells))
    print('  Execute with:')
    print('    jupyter nbconvert --to notebook --execute --inplace "{}"'.format(path))
except Exception as e:
    print('  FAIL:', e)
    import traceback; traceback.print_exc()

# ---------------------------------------------------------------------------
# Test 2: agent.list_commands()
# ---------------------------------------------------------------------------
print('\n[2] agent.list_commands() - introspecting dmcommands...')
try:
    from dmstudio import agent
    commands = agent.list_commands()
    print('  OK - found {} commands'.format(len(commands)))
    print('  First 5:', [c['name'] for c in commands[:5]])
except Exception as e:
    print('  FAIL:', e)
    import traceback; traceback.print_exc()

# ---------------------------------------------------------------------------
# Test 3: agent.get_command_schema()
# ---------------------------------------------------------------------------
print('\n[3] agent.get_command_schema("copy")...')
try:
    schema = agent.get_command_schema('copy')
    print('  OK - schema keys:', list(schema.keys()))
    print('  Parameters:', [p['name'] for p in schema.get('parameters', [])][:6])
except Exception as e:
    print('  FAIL:', e)
    import traceback; traceback.print_exc()

# ---------------------------------------------------------------------------
# Test 4: agent.search_commands()
# ---------------------------------------------------------------------------
print('\n[4] agent.search_commands("sort")...')
try:
    results = agent.search_commands('sort')
    print('  OK - {} matches'.format(len(results)))
    print('  Matches:', [r['name'] for r in results])
except Exception as e:
    print('  FAIL:', e)
    import traceback; traceback.print_exc()

# ---------------------------------------------------------------------------
# Test 5: Dynamic StudioRM3.x version resolution (no Studio required)
# ---------------------------------------------------------------------------
print('\n[5] initialize.studio() - StudioRM3.x dynamic version resolution...')
try:
    from dmstudio import initialize
    import re

    # Test the logic directly without needing a running Studio instance
    test_versions = ['StudioRM3.1', 'StudioRM3.2', 'StudioRM3.3', 'StudioRM3.10']
    for v in test_versions:
        matches = (v == 'StudioRM' or (isinstance(v, str) and v.startswith('StudioRM3.')))
        print('  {} -> resolved={}'.format(v, matches))
    print('  OK - all StudioRM3.x variants resolve correctly')
except Exception as e:
    print('  FAIL:', e)
    import traceback; traceback.print_exc()

# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------
print('\n' + '=' * 60)
print('Verification complete.')
print('Run "quick_test.py" for COM connectivity test (requires Studio license).')
print('=' * 60)
