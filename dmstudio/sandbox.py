'''
dmstudio.sandbox
----------------

Sandbox and database helper module for Datamine Studio RM scripting.

Provides:
- initialize_sandbox()     : Initialize the active Datamine project sandbox.
- copy_database_files()    : Copy specific files from the tutorials Database to the target directory.
'''
import os
import shutil
import sys

from dmstudio import initialize

# Capture the current working directory at import time.
# Used as a fallback if notebook_folder is not specified or is resolved
# to the sandbox directory upon repeated execution.
_initial_cwd = os.getcwd()


def copy_database_files(files_to_copy, target_dir=None):
    '''
    copy_database_files
    -------------------

    Copy specific files from the tutorials Database to the target directory.

    Parameters:
    -----------
    files_to_copy: list or dict
        List of filenames to copy, or dict mapping source name to destination name.
    target_dir: str, optional
        Target directory to copy files to. Defaults to current working directory.
    '''
    if target_dir is None:
        target_dir = os.getcwd()

    repo_root = target_dir
    while True:
        if os.path.exists(os.path.join(repo_root, 'pyproject.toml')) or os.path.exists(os.path.join(repo_root, 'AGENTS.md')):
            break
        parent = os.path.dirname(repo_root)
        if parent == repo_root:
            break
        repo_root = parent

    help_db = os.path.join(repo_root, 'tutorials', 'Database', 'DMTutorials', 'Data', 'VBOP', 'Datamine')
    if not os.path.exists(help_db):
        raise ValueError('Tutorial Database folder not found at: {}'.format(help_db))

    items = files_to_copy.items() if isinstance(files_to_copy, dict) else [(f, None) for f in files_to_copy]

    for src_name, dst_name in items:
        src = os.path.join(help_db, src_name)
        if not dst_name:
            if src_name.startswith('_vb_'):
                dst_name = 't_' + src_name.replace('_vb_', '')
            else:
                dst_name = src_name
        dst = os.path.join(target_dir, dst_name)
        if os.path.exists(src):
            shutil.copy2(src, dst)
            print('Initialized database dataset: {}'.format(dst_name))
        else:
            print('Warning: Source {} not found in database at {}.'.format(src_name, help_db))


def initialize_sandbox(notebook_folder=None, files_to_copy=None):
    '''
    initialize_sandbox
    ------------------

    Initialize the active Datamine project sandbox.
    Changes Python's working directory to the active project folder,
    validates that it is the test_sandbox, and copies any local/required files.

    Parameters:
    -----------
    notebook_folder: str, optional
        The path to the folder containing the notebook. If None or if it incorrectly
        resolves to the sandbox on re-execution, defaults to the initial directory.
    files_to_copy: list of str, optional
        A list of specific filenames to copy from the help database to the sandbox.
    '''
    if notebook_folder is None or os.path.basename(notebook_folder).lower() == 'test_sandbox':
        notebook_folder = _initial_cwd

    notebook_folder = os.path.abspath(notebook_folder)

    # 1. Connect to Datamine Studio RM COM Application
    try:
        oScript = initialize.studio('StudioRM')
    except Exception as e:
        raise RuntimeError(
            'Could not connect to Datamine Studio RM. '
            'Please ensure Datamine Studio RM is open and licensed.'
            ) from e

    # 2. Get active project folder
    project = oScript.ActiveProject
    if project is None:
        raise RuntimeError(
            'No active project in Studio RM! '
            'Please open "tutorials/test_sandbox/Project.rmproj" inside Studio RM first.'
        )

    active_folder = os.path.abspath(project.Folder)

    # 3. Find repo root dynamically
    repo_root = notebook_folder
    while True:
        if os.path.exists(os.path.join(repo_root, 'pyproject.toml')) or os.path.exists(os.path.join(repo_root, 'AGENTS.md')):
            break
        parent = os.path.dirname(repo_root)
        if parent == repo_root:
            repo_root = os.path.abspath(os.path.join(notebook_folder, '..', '..', '..', '..'))
            break
        repo_root = parent

    expected_sandbox = os.path.abspath(os.path.join(repo_root, 'tutorials', 'test_sandbox'))

    # 4. Enforce that the active project matches test_sandbox
    if os.path.normpath(active_folder).lower() != os.path.normpath(expected_sandbox).lower():
        raise RuntimeError(
            'Active Datamine Project ({}) does not match the test sandbox ({}).\n'
            'Please open "tutorials/test_sandbox/Project.rmproj" inside Datamine Studio RM first!'.format(
                active_folder, expected_sandbox
            )
        )

    # 5. Change current working directory to active folder (sandbox)
    os.chdir(active_folder)
    print('Working directory changed to active project folder: {}'.format(active_folder))

    # 6. Ensure active_folder is in sys.path so 'import dmdir' works locally
    if active_folder not in sys.path:
        sys.path.insert(0, active_folder)

    # 7. Copy any local tutorial files (excluding project metadata and notebooks) from notebook_folder to active_folder
    if os.path.normpath(notebook_folder).lower() != os.path.normpath(active_folder).lower():
        for filename in os.listdir(notebook_folder):
            file_lower = filename.lower()
            if file_lower in ('project.rmproj', 'dmstusub.dat', '__pycache__', '.ipynb_checkpoints', 'dmdir.py', '__init__.py') or file_lower.endswith('.ipynb'):
                continue
            if file_lower.startswith('project.rmproj.'):
                continue
            src_file = os.path.join(notebook_folder, filename)
            if os.path.isfile(src_file):
                dst_file = os.path.join(active_folder, filename)
                shutil.copy2(src_file, dst_file)
                print('Copied local notebook asset: {}'.format(filename))

    # 8. Copy database files if requested
    if files_to_copy:
        copy_database_files(files_to_copy, target_dir=active_folder)
