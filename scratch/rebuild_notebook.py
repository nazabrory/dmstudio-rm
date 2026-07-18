import json

notebook_path = 'run_tests.ipynb'

helper_code = """import os
import sys
import shutil
import glob
import time
import datetime
import traceback
import argparse
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor, CellExecutionError
from dmstudio import agent, initialize
from dmstudio.command_registry import VERIFIED_COMMANDS

def reset_com_state(oScript):
    try:
        if oScript is not None:
            try:
                oScript.Parsecommand("can")
            except Exception:
                pass
            hwnd = getattr(oScript, 'WindowHandle', None)
            if hwnd:
                import win32con, win32api
                win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_ESCAPE, 0)
                win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_ESCAPE, 0)
    except Exception as e:
        print(f"  [Warning] Failed to reset COM state: {e}")

def clear_sandbox(sandbox_dir):
    print(f"Clearing sandbox: {sandbox_dir}")
    for item in os.listdir(sandbox_dir):
        item_lower = item.lower()
        if item_lower == 'project.rmproj' or item_lower.startswith('project.rmproj.'):
            continue
        item_path = os.path.join(sandbox_dir, item)
        try:
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
            else:
                os.remove(item_path)
        except Exception as e:
            print(f"  [Warning] Failed to remove {item} from sandbox: {e}")

def patch_notebook_paths(nb_path, repo_root_abs):
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    modified = False
    for cell in nb.cells:
        if cell.cell_type == 'code':
            lines = cell.source.splitlines()
            new_lines = []
            for line in lines:
                if 'repo_root = os.path.abspath(os.path.join(' in line:
                    indent = line[:line.find('repo_root')]
                    new_lines.append(f'{indent}repo_root = r"{repo_root_abs}"')
                    modified = True
                else:
                    new_lines.append(line)
            cell.source = '\\n'.join(new_lines)
    if modified:
        with open(nb_path, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
        print("  Patched repo_root path to absolute.")

def run_test_suite(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('--all', action='store_true')
    parser.add_argument('--workflows', action='store_true')
    parser.add_argument('--processes', action='store_true')
    parser.add_argument('--files', action='store_true')
    parser.add_argument('--only', type=str)
    parser.add_argument('--start', type=str)
    parser.add_argument('--end', type=str)
    parser.add_argument('--timeout', type=int, default=60)
    
    args = [a for a in args if a]
    parsed_args = parser.parse_args(args)

    repo_root = os.path.abspath(os.getcwd())
    sandbox_dir = os.path.join(repo_root, 'tutorials', 'test_sandbox')
    expected_project_path = os.path.join(sandbox_dir, 'Project.rmproj')

    existing_pp = os.environ.get('PYTHONPATH', '')
    if repo_root not in existing_pp:
        os.environ['PYTHONPATH'] = os.path.pathsep.join([repo_root, existing_pp]) if existing_pp else repo_root

    print("Connecting to running Datamine Studio RM instance...")
    try:
        oScript = initialize.studio('StudioRM')
        print(f"Connected to: {oScript.Caption}")
    except Exception as e:
        print(f"[ERROR] Could not connect to Datamine Studio RM: {e}")
        return

    project = oScript.ActiveProject
    if project is None:
        print("No active project detected. Attempting to open test sandbox project...")
        try:
            oScript.OpenProject(expected_project_path)
            time.sleep(2.0)
            project = oScript.ActiveProject
        except Exception as e:
            print(f"Failed to open sandbox project: {e}")
            
    if project is None:
        print("[ERROR] No active project in Studio RM!")
        return

    active_folder = os.path.normpath(project.Folder).lower()
    expected_folder = os.path.normpath(sandbox_dir).lower()
    if active_folder != expected_folder:
        print(f"[ERROR] Active project folder mismatch! Active: {active_folder}, Expected: {expected_folder}")
        return

    notebook_queue = []
    
    # 1. Workflows
    if parsed_args.all or parsed_args.workflows or (not parsed_args.processes and not parsed_args.files and not parsed_args.only):
        workflows_dir = os.path.join(repo_root, 'tutorials', 'workflows')
        for folder in os.listdir(workflows_dir):
            folder_path = os.path.join(workflows_dir, folder)
            if os.path.isdir(folder_path):
                for f in os.listdir(folder_path):
                    if f.endswith('.ipynb'):
                        notebook_queue.append({
                            'name': f.replace('.ipynb', ''),
                            'type': 'workflow',
                            'dir': folder_path,
                            'file': f
                        })

    # 2. Collections (Processes and Files)
    if parsed_args.all or parsed_args.processes or parsed_args.files or (parsed_args.only and not parsed_args.workflows):
        try:
            from dmstudio import dmfiles
            cls_file = dmfiles.init
            dmfiles_methods = {name.lower() for name in dir(cls_file) if not name.startswith('_') and callable(getattr(cls_file, name))}
        except Exception:
            dmfiles_methods = {'inpfil'}
            
        collections_dir = os.path.join(repo_root, 'tutorials', 'collections')
        if os.path.exists(collections_dir):
            for item in os.listdir(collections_dir):
                item_path = os.path.join(collections_dir, item)
                if os.path.isfile(item_path) and item.endswith('_example.ipynb'):
                    cmd_name = item.replace('_example.ipynb', '').lower()
                    if cmd_name in VERIFIED_COMMANDS:
                        is_dmfile = cmd_name in dmfiles_methods
                        if parsed_args.processes and not parsed_args.all and not parsed_args.files and is_dmfile:
                            continue
                        if parsed_args.files and not parsed_args.all and not parsed_args.processes and not is_dmfile:
                            continue
                        notebook_queue.append({
                            'name': cmd_name,
                            'type': 'file' if is_dmfile else 'process',
                            'dir': collections_dir,
                            'file': item
                        })

    if parsed_args.start or parsed_args.end:
        start_char = parsed_args.start.lower() if parsed_args.start else 'a'
        end_char = parsed_args.end.lower() if parsed_args.end else 'z'
        notebook_queue = [nb for nb in notebook_queue if start_char <= nb['name'].lower()[0] <= end_char]

    if parsed_args.only:
        names_to_keep = [n.strip().lower() for n in parsed_args.only.split(',')]
        notebook_queue = [nb for nb in notebook_queue if nb['name'].lower() in names_to_keep]

    if not notebook_queue:
        print("No notebooks found matching the criteria.")
        return

    print(f"Queued {len(notebook_queue)} notebooks for validation.")
    print("=" * 60)

    test_results_root = os.path.join(repo_root, 'tutorials', 'test_results')
    run_id = datetime.datetime.now().strftime("run_%Y%m%d_%H%M%S")
    results_dir = os.path.join(test_results_root, run_id)
    os.makedirs(results_dir, exist_ok=True)

    results = []

    for idx, nb_info in enumerate(notebook_queue, start=1):
        name = nb_info['name']
        nb_type = nb_info['type']
        src_dir = nb_info['dir']
        nb_file = nb_info['file']
        
        print(f"[{idx}/{len(notebook_queue)}] Running {nb_type.upper()}: {name}...")
        try:
            with agent.dialog_dismiss_context(title='Studio RM'):
                if oScript.ActiveProject is not None:
                    oScript.ActiveProject.CloseNoSave()
                    time.sleep(1.0)
                oScript.OpenProject(expected_project_path)
                time.sleep(1.5)
        except Exception as e:
            print(f'  [Warning] Failed to re-open project: {e}')
            
        clear_sandbox(sandbox_dir)
        shutil.copy2(os.path.join(src_dir, nb_file), os.path.join(sandbox_dir, nb_file))
        sandbox_nb_path = os.path.join(sandbox_dir, nb_file)
        
        try:
            patch_notebook_paths(sandbox_nb_path, repo_root)
        except Exception as e:
            print(f"  [ERROR] Failed to patch paths: {e}")
            results.append({
                'name': name,
                'type': nb_type,
                'status': 'FAILED',
                'duration': 0.0,
                'error': f"Path patching failed: {e}"
            })
            continue

        ep = ExecutePreprocessor(timeout=parsed_args.timeout, kernel_name='python3')
        start_time = time.time()
        status = 'PASSED'
        error_msg = None
        
        try:
            with open(sandbox_nb_path, 'r', encoding='utf-8') as f:
                nb_obj = nbformat.read(f, as_version=4)
            print(f"  Executing cells in background dialog dismiss context...")
            with agent.dialog_dismiss_context(title='Studio RM'):
                ep.preprocess(nb_obj, {'metadata': {'path': sandbox_dir}})
        except CellExecutionError as e:
            status = 'FAILED'
            error_msg = f"CellExecutionError:\\n{e}"
            print(f"  [FAILED] Cell execution error in notebook.")
        except Exception as e:
            status = 'FAILED'
            error_msg = f"Exception:\\n{e}\\n{traceback.format_exc()}"
            print(f"  [FAILED] Unexpected exception during run: {e}")
        
        duration = time.time() - start_time
        print(f"  Result: {status} ({duration:.2f}s)")
        
        result_nb_file = f"{name}_{status.lower()}.ipynb"
        result_nb_path = os.path.join(results_dir, result_nb_file)
        try:
            with open(result_nb_path, 'w', encoding='utf-8') as f:
                nbformat.write(nb_obj, f)
            print(f"  Saved evaluated notebook to {os.path.relpath(result_nb_path, repo_root)}")
        except Exception as e:
            print(f"  [Warning] Failed to save evaluated notebook: {e}")

        results.append({
            'name': name,
            'type': nb_type,
            'status': status,
            'duration': duration,
            'error': error_msg
        })

    clear_sandbox(sandbox_dir)

    summary_path = os.path.join(results_dir, 'summary.md')
    passed_count = sum(1 for r in results if r['status'] == 'PASSED')
    failed_count = sum(1 for r in results if r['status'] == 'FAILED')
    total_duration = sum(r['duration'] for r in results)

    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write(f"# dmstudio Notebook Test Summary Report\\n\\n")
        f.write(f"- **Run ID:** `{run_id}`\\n")
        f.write(f"- **Timestamp:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\\n")
        f.write(f"- **Total Notebooks Run:** {len(results)}\\n")
        f.write(f"- **Passed:** {passed_count}\\n")
        f.write(f"- **Failed:** {failed_count}\\n")
        f.write(f"- **Total Execution Time:** {total_duration:.2f}s\\n\\n")
        f.write(f"## Detailed Results\\n\\n")
        f.write(f"| Name | Type | Status | Duration (s) | Error Details |\\n")
        f.write(f"| --- | --- | --- | --- | --- |\\n")
        for r in results:
            err_summary = r['error'].replace('\\n', '<br>') if r['error'] else ''
            f.write(f"| {r['name']} | {r['type']} | **{r['status']}** | {r['duration']:.2f} | {err_summary} |\\n")

    print("=" * 60)
    print("TESTING FINISHED")
    print(f"Total: {len(results)} | Passed: {passed_count} | Failed: {failed_count}")
    print(f"Total Time: {total_duration:.2f}s")
    print(f"Summary Report: {os.path.relpath(summary_path, repo_root)}")
    print("=" * 60)
"""

cells = [
    {
        "cell_type": "markdown",
        "id": "ce0b4d85",
        "metadata": {},
        "source": [
            "# dmstudio Tutorial Notebook Test Runner\n",
            "\n",
            "_Generated by dmstudio.notebook_builder on 2026-07-18 15:37_\n",
            "\n",
            "> Run with: `jupyter nbconvert --to notebook --execute --inplace run_tests.ipynb`"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "id": "8d22827d",
        "metadata": {},
        "outputs": [],
        "source": [
            "# Auto-generated preamble\n",
            "import warnings\n",
            "warnings.filterwarnings(\"ignore\")\n",
            "print(\"Notebook: dmstudio Tutorial Notebook Test Runner\")"
        ]
    },
    {
        "cell_type": "markdown",
        "id": "a0a005f7",
        "metadata": {},
        "source": [
            "## Environment Verification\n",
            "Run this cell first to verify we are in the correct directory and connected to Studio RM."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "id": "8d3feafc",
        "metadata": {},
        "outputs": [],
        "source": [
            "import sys\n",
            "import os\n",
            "from dmstudio import initialize\n",
            "\n",
            "print('Python Executable:', sys.executable)\n",
            "print('Current Working Directory:', os.getcwd())\n",
            "\n",
            "oScript = initialize.studio('StudioRM')\n",
            "print(f'Connected to: {oScript.Caption}')\n",
            "print(f'Active Project: {oScript.ActiveProject}')"
        ]
    },
    {
        "cell_type": "markdown",
        "id": "528a2dc6",
        "metadata": {},
        "source": [
            "## Helper function to run tests and stream output\n",
            "Run this cell to define the subprocess streaming helper. It default-configures a **60-second timeout per notebook** to abort any blocking prompts."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "id": "4d7ac7f8",
        "metadata": {},
        "outputs": [],
        "source": [line + "\n" for line in helper_code.splitlines()]
    },
    {
        "cell_type": "markdown",
        "id": "1de8741b",
        "metadata": {},
        "source": [
            "## Batch 1: Run Verified Core Commands\n",
            "Runs all verified process and file command notebooks."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "id": "fc017a49",
        "metadata": {},
        "outputs": [],
        "source": [
            "run_test_suite(['--only', 'accmlt,append,cokrig,compdh,copy,count,delete,diffrn,dmedit,extra,holes3d,ijkgen,join,mgsort,modtra,output,selcop,seldel,selexy,sortx,stats,tongrad,inpfil'])"
        ]
    },
    {
        "cell_type": "markdown",
        "id": "1de8741c",
        "metadata": {},
        "source": [
            "## Batch 1A: Process Sandboxes (A-D)\n",
            "Runs all process notebooks starting with letters A through D."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "id": "fc017a4a",
        "metadata": {},
        "outputs": [],
        "source": [
            "run_test_suite(['--processes', '--start', 'a', '--end', 'd'])"
        ]
    },
    {
        "cell_type": "markdown",
        "id": "7c9068bf",
        "metadata": {},
        "source": [
            "## Batch 1B: Process Sandboxes (E-H)\n",
            "Runs all process notebooks starting with letters E through H."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "id": "a911bb4a",
        "metadata": {},
        "outputs": [],
        "source": [
            "run_test_suite(['--processes', '--start', 'e', '--end', 'h'])"
        ]
    },
    {
        "cell_type": "markdown",
        "id": "9b12747d",
        "metadata": {},
        "source": [
            "## Batch 1C: Process Sandboxes (I-L)\n",
            "Runs all process notebooks starting with letters I through L."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "id": "c1930acb",
        "metadata": {},
        "outputs": [],
        "source": [
            "run_test_suite(['--processes', '--start', 'i', '--end', 'l'])"
        ]
    },
    {
        "cell_type": "markdown",
        "id": "83c68591",
        "metadata": {},
        "source": [
            "## Batch 1D: Process Sandboxes (M-P)\n",
            "Runs all process notebooks starting with letters M through P."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "id": "98c8063e",
        "metadata": {},
        "outputs": [],
        "source": [
            "run_test_suite(['--processes', '--start', 'm', '--end', 'p'])"
        ]
    },
    {
        "cell_type": "markdown",
        "id": "486bd8b7",
        "metadata": {},
        "source": [
            "## Batch 1E: Process Sandboxes (Q-T)\n",
            "Runs all process notebooks starting with letters Q through T."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "id": "27e67d39",
        "metadata": {},
        "outputs": [],
        "source": [
            "run_test_suite(['--processes', '--start', 'q', '--end', 't'])"
        ]
    },
    {
        "cell_type": "markdown",
        "id": "5ce50045",
        "metadata": {},
        "source": [
            "## Batch 1F: Process Sandboxes (U-Z)\n",
            "Runs all process notebooks starting with letters U through Z."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "id": "a8ccee94",
        "metadata": {},
        "outputs": [],
        "source": [
            "run_test_suite(['--processes', '--start', 'u', '--end', 'z'])"
        ]
    },
    {
        "cell_type": "markdown",
        "id": "002aaeb7",
        "metadata": {},
        "source": [
            "## Batch 2: File Sandboxes\n",
            "Runs all file command notebooks under `tutorials/collections/`."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "id": "a3244906",
        "metadata": {},
        "outputs": [],
        "source": [
            "run_test_suite(['--files'])"
        ]
    },
    {
        "cell_type": "markdown",
        "id": "662382cd",
        "metadata": {},
        "source": [
            "## Batch 3: Case Studies (Fast - 3 Notebooks)\n",
            "Runs Holes3D, Grade Estimation, and Studio RM 3.1 example notebooks."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "id": "d88c4fc2",
        "metadata": {},
        "outputs": [],
        "source": [
            "run_test_suite(['--case-studies'])"
        ]
    },
    {
        "cell_type": "markdown",
        "id": "4b8fc804",
        "metadata": {},
        "source": [
            "## Batch 4: Run Everything\n",
            "Runs all case studies, file sandboxes, and process sandboxes in one go."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "id": "0053c586",
        "metadata": {},
        "outputs": [],
        "source": [
            "run_test_suite(['--all'])"
        ]
    }
]

notebook_data = {
    "cells": cells,
    "metadata": {
        "kernelspec": {
            "display_name": "dmstudio",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.14.6"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 5
}

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(notebook_data, f, indent=1)

print("Successfully rebuilt run_tests.ipynb completely from scratch!")
