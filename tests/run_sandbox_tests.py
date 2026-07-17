"""
run_sandbox_tests.py
--------------------

Automated test runner that executes Jupyter Notebook tutorials sequentially
inside a dedicated test sandbox directory.

Features:
- Verifies connection to Datamine Studio RM.
- Verifies that the active project matches the test sandbox folder.
- Patches path resolution strings in copied notebooks to point to the absolute repo root.
- Runs notebooks sequentially under agent.dialog_dismiss_context() to prevent blocking modals.
- Implements execution timeouts (default 300s/5m).
- Performs aggressive sandbox cleanup between runs.
- Stores evaluated notebooks and summaries in tutorials/test_results/.
"""

import os
import sys
import shutil
import glob
import time
import datetime
import argparse
import json
import re
import traceback

# Add parent directory to path so dmstudio is importable
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dmstudio import agent, initialize
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor, CellExecutionError

def clear_sandbox(sandbox_dir):
    """Delete all files and directories in sandbox_dir except Project.rmproj and its metadata."""
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

def copy_notebook_files(src_dir, dest_dir):
    """Copy all files/subdirs from src_dir to dest_dir, ignoring project files and temp folders."""
    for item in os.listdir(src_dir):
        item_lower = item.lower()
        if item_lower in ('project.rmproj', '__pycache__', '.ipynb_checkpoints'):
            continue
        if item_lower.startswith('project.rmproj.'):
            continue
        src_path = os.path.join(src_dir, item)
        dest_path = os.path.join(dest_dir, item)
        try:
            if os.path.isdir(src_path):
                shutil.copytree(src_path, dest_path)
            else:
                shutil.copy2(src_path, dest_path)
        except Exception as e:
            print(f"  [Warning] Failed to copy {item}: {e}")

def patch_notebook_paths(nb_path, repo_root_abs):
    """Replace relative repo_root lookups with the absolute path to repo_root_abs."""
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    modified = False
    for cell in nb.cells:
        if cell.cell_type == 'code':
            lines = cell.source.splitlines()
            new_lines = []
            for line in lines:
                # Matches repo_root = os.path.abspath(os.path.join(notebook_folder, ...))
                # or repo_root = os.path.abspath(os.path.join(project_folder, ...))
                if 'repo_root = os.path.abspath(os.path.join(' in line:
                    indent = line[:line.find('repo_root')]
                    new_lines.append(f'{indent}repo_root = r"{repo_root_abs}"')
                    modified = True
                else:
                    new_lines.append(line)
            cell.source = '\n'.join(new_lines)

    if modified:
        with open(nb_path, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
        print("  Patched repo_root path to absolute.")

def main():
    parser = argparse.ArgumentParser(description="dmstudio Notebook Tutorial Validation Runner")
    parser.add_argument("--all", action="store_true", help="Run all notebooks")
    parser.add_argument("--case-studies", action="store_true", help="Run case study notebooks only")
    parser.add_argument("--processes", action="store_true", help="Run process sandbox notebooks only")
    parser.add_argument("--files", action="store_true", help="Run file sandbox notebooks only")
    parser.add_argument("--only", type=str, help="Comma-separated names of specific command/notebook to run")
    parser.add_argument("--timeout", type=int, default=300, help="Timeout in seconds per notebook (default: 300)")
    args = parser.parse_args()

    repo_root = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    sandbox_dir = os.path.join(repo_root, 'tutorials', 'test_sandbox')

    print("Checking Datamine Studio RM COM connection...")
    try:
        oScript = initialize.studio('StudioRM')
        print(f"Connected to: {oScript.Caption}")
    except Exception as e:
        print(f"\n[ERROR] Could not connect to Datamine Studio RM: {e}")
        print("Please ensure Datamine Studio RM is open and licensed.")
        sys.exit(1)

    project = oScript.ActiveProject
    if project is None:
        print("\n[ERROR] No active project in Studio RM!")
        print(f"Please open: {os.path.join(sandbox_dir, 'Project.rmproj')} inside Studio RM.")
        sys.exit(1)

    active_folder = os.path.normpath(project.Folder).lower()
    expected_folder = os.path.normpath(sandbox_dir).lower()

    if active_folder != expected_folder:
        print(f"\n[ERROR] Active project folder mismatch!")
        print(f"Active project: {active_folder}")
        print(f"Expected:       {expected_folder}")
        print(f"Please open: {os.path.join(sandbox_dir, 'Project.rmproj')} inside Studio RM.")
        sys.exit(1)

    print("Active project folder verified successfully.")

    # Find notebooks based on filters
    notebook_queue = []
    
    # 1. Case Studies
    if args.all or args.case_studies or (not args.processes and not args.files and not args.only):
        case_studies_dir = os.path.join(repo_root, 'tutorials', 'case_studies')
        for folder in os.listdir(case_studies_dir):
            folder_path = os.path.join(case_studies_dir, folder)
            if os.path.isdir(folder_path):
                for f in os.listdir(folder_path):
                    if f.endswith('.ipynb'):
                        notebook_queue.append({
                            'name': f.replace('.ipynb', ''),
                            'type': 'case_study',
                            'dir': folder_path,
                            'file': f
                        })

    # 2. Processes
    if args.all or args.processes:
        proc_dir = os.path.join(repo_root, 'tutorials', 'collections', 'processes')
        for folder in os.listdir(proc_dir):
            folder_path = os.path.join(proc_dir, folder)
            if os.path.isdir(folder_path):
                for f in os.listdir(folder_path):
                    if f.endswith('.ipynb'):
                        notebook_queue.append({
                            'name': folder,
                            'type': 'process',
                            'dir': folder_path,
                            'file': f
                        })

    # 3. Files
    if args.all or args.files:
        files_dir = os.path.join(repo_root, 'tutorials', 'collections', 'files')
        for folder in os.listdir(files_dir):
            folder_path = os.path.join(files_dir, folder)
            if os.path.isdir(folder_path):
                for f in os.listdir(folder_path):
                    if f.endswith('.ipynb'):
                        notebook_queue.append({
                            'name': folder,
                            'type': 'file',
                            'dir': folder_path,
                            'file': f
                        })

    # Filter by specific name if --only is passed
    if args.only:
        names_to_keep = [n.strip().lower() for n in args.only.split(',')]
        notebook_queue = [nb for nb in notebook_queue if nb['name'].lower() in names_to_keep]

    if not notebook_queue:
        print("No notebooks found matching the criteria.")
        sys.exit(0)

    print(f"\nQueued {len(notebook_queue)} notebooks for validation.")
    print("=" * 60)

    # Initialize results directories
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
        
        print(f"\n[{idx}/{len(notebook_queue)}] Running {nb_type.upper()}: {name}...")
        
        # 1. Clear Sandbox
        clear_sandbox(sandbox_dir)
        
        # 2. Copy notebook and files to sandbox
        copy_notebook_files(src_dir, sandbox_dir)
        sandbox_nb_path = os.path.join(sandbox_dir, nb_file)
        
        # 3. Patch notebook paths to absolute repo root
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

        # 4. Prepare execution preprocessor
        ep = ExecutePreprocessor(timeout=args.timeout, kernel_name='python3')
        
        start_time = time.time()
        status = 'PASSED'
        error_msg = None
        
        # 5. Execute notebook cells in sandbox
        try:
            with open(sandbox_nb_path, 'r', encoding='utf-8') as f:
                nb = nbformat.read(f, as_version=4)
            
            print(f"  Executing cells in background dialog dismiss context...")
            with agent.dialog_dismiss_context(title='Studio RM'):
                ep.preprocess(nb, {'metadata': {'path': sandbox_dir}})
                
        except CellExecutionError as e:
            status = 'FAILED'
            error_msg = f"CellExecutionError:\n{e}"
            print(f"  [FAILED] Cell execution error in notebook.")
        except Exception as e:
            status = 'FAILED'
            error_msg = f"Exception:\n{e}\n{traceback.format_exc()}"
            print(f"  [FAILED] Unexpected exception during run: {e}")
        
        duration = time.time() - start_time
        print(f"  Result: {status} ({duration:.2f}s)")
        
        # 6. Save evaluated notebook to test results folder
        result_nb_file = f"{name}_{status.lower()}.ipynb"
        result_nb_path = os.path.join(results_dir, result_nb_file)
        try:
            # We re-read from disk if execution succeeded (since preprocess edits nb object in memory)
            with open(result_nb_path, 'w', encoding='utf-8') as f:
                nbformat.write(nb, f)
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

    # Post-run cleanup
    clear_sandbox(sandbox_dir)

    # Generate Summary Report
    summary_path = os.path.join(results_dir, 'summary.md')
    passed_count = sum(1 for r in results if r['status'] == 'PASSED')
    failed_count = sum(1 for r in results if r['status'] == 'FAILED')
    total_duration = sum(r['duration'] for r in results)

    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write(f"# dmstudio Notebook Test Summary Report\n\n")
        f.write(f"- **Run ID:** `{run_id}`\n")
        f.write(f"- **Timestamp:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"- **Total Notebooks Run:** {len(results)}\n")
        f.write(f"- **Passed:** {passed_count}\n")
        f.write(f"- **Failed:** {failed_count}\n")
        f.write(f"- **Total Execution Time:** {total_duration:.2f}s\n\n")
        
        f.write(f"## Detailed Results\n\n")
        f.write(f"| Name | Type | Status | Duration (s) | Error Details |\n")
        f.write(f"| --- | --- | --- | --- | --- |\n")
        for r in results:
            err_summary = r['error'].replace('\n', '<br>') if r['error'] else ''
            f.write(f"| {r['name']} | {r['type']} | **{r['status']}** | {r['duration']:.2f} | {err_summary} |\n")

    print("\n" + "=" * 60)
    print("TESTING FINISHED")
    print(f"Total: {len(results)} | Passed: {passed_count} | Failed: {failed_count}")
    print(f"Total Time: {total_duration:.2f}s")
    print(f"Summary Report: {os.path.relpath(summary_path, repo_root)}")
    print("=" * 60)

if __name__ == "__main__":
    main()
