import json
import os
import subprocess
import sys
import traceback
from contextlib import contextmanager
from typing import Any, Dict, Optional

from dmstudio.output_capture import CommandLogCapture, classify_log_delta


@contextmanager
def _safe_dialog():
    try:
        from dmstudio.dialog import dialog_dismiss_context
        with dialog_dismiss_context():
            yield
    except Exception:
        yield


def _execute_cells(notebook_path: str, custom_log_path: Optional[str] = None) -> Dict[str, Any]:
    '''
    Internal execution worker that sequentially runs notebook cells,
    monitoring Python execution and Datamine Command.log deltas.
    '''
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb_data = json.load(f)

    cells = nb_data.get('cells', [])

    capture = CommandLogCapture(log_path=custom_log_path)
    globals_dict: Dict[str, Any] = {'__name__': '__main__'}

    accumulated_log = []
    executed_code_cells = 0

    with _safe_dialog():
        for idx, cell in enumerate(cells):
            if cell.get('cell_type') != 'code':
                continue

            raw_source = cell.get('source', '')
            if isinstance(raw_source, list):
                cell_code = ''.join(raw_source)
            else:
                cell_code = str(raw_source)

            if not cell_code.strip():
                continue

            executed_code_cells += 1
            capture.mark()
            py_exc = None
            tb_str = ''

            try:
                compiled = compile(cell_code, f'<cell_{idx}>', 'exec')
                exec(compiled, globals_dict)
            except Exception as e:
                py_exc = e
                tb_str = traceback.format_exc()

            delta = capture.get_delta()
            if delta:
                accumulated_log.append(f'--- Cell {idx} ---\n{delta}')

            success, dm_errors, dm_warnings = classify_log_delta(delta)

            # Check for failure conditions:
            # 1. Python exception occurred
            # 2. Datamine command output contains fatal errors
            if py_exc is not None:
                return {
                    'success': False,
                    'total_cells': len(cells),
                    'failed_cell_index': idx,
                    'failed_cell_code': cell_code,
                    'error_type': 'PYTHON_EXCEPTION',
                    'error_message': f'{type(py_exc).__name__}: {str(py_exc)}',
                    'python_traceback': tb_str,
                    'command_log_delta': delta,
                    'summary': f'Cell {idx} failed with {type(py_exc).__name__}: {str(py_exc)}',
                }

            if not success:
                err_summary = '; '.join(dm_errors) if dm_errors else 'Datamine process error detected'
                return {
                    'success': False,
                    'total_cells': len(cells),
                    'failed_cell_index': idx,
                    'failed_cell_code': cell_code,
                    'error_type': 'DATAMINE_ERROR',
                    'error_message': err_summary,
                    'python_traceback': '',
                    'command_log_delta': delta,
                    'summary': f'Cell {idx} Datamine command failed: {err_summary}',
                }

    return {
        'success': True,
        'total_cells': len(cells),
        'cells_executed': executed_code_cells,
        'summary': 'All notebook cells executed successfully in Studio RM.',
        'full_log': '\n'.join(accumulated_log),
    }


def _resolve_default_sandbox() -> Optional[str]:
    '''Locates tutorials/test_sandbox if present in repository root.'''
    cur = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(cur)
    sandbox = os.path.join(root, 'tutorials', 'test_sandbox')
    if os.path.isdir(sandbox):
        return sandbox
    return None


def run_and_diagnose_notebook(
    notebook_path: str,
    timeout: int = 120,
    sandbox_dir: Optional[str] = None,
    custom_log_path: Optional[str] = None,
) -> Dict[str, Any]:
    '''
    run_and_diagnose_notebook
    -------------------------
    Executes a Jupyter Notebook in an isolated subprocess against Datamine Studio RM,
    capturing cell-level Python exceptions and pairing them with Command.log deltas.

    Parameters:
    -----------
    notebook_path: str
        Absolute or relative path to the .ipynb notebook.
    timeout: int, optional
        Maximum execution timeout in seconds. Default 120s.
    sandbox_dir: str, optional
        Working directory for the execution subprocess. Defaults to tutorials/test_sandbox/.
    custom_log_path: str, optional
        Custom Command.log path for testing.

    Returns:
    --------
    Dict[str, Any]:
        Structured diagnostic report containing execution status and failure bundles.
    '''
    if not os.path.exists(notebook_path):
        return {
            'success': False,
            'error_type': 'FILE_NOT_FOUND',
            'summary': f'Notebook file not found: {notebook_path}',
        }

    abs_nb_path = os.path.abspath(notebook_path)
    cwd = sandbox_dir or _resolve_default_sandbox() or os.path.dirname(abs_nb_path) or os.getcwd()

    cmd = [sys.executable, '-m', 'dmstudio.notebook_runner', abs_nb_path]
    if custom_log_path:
        cmd.extend(['--log-path', custom_log_path])

    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=cwd,
        )
    except subprocess.TimeoutExpired:
        return {
            'success': False,
            'error_type': 'TIMEOUT',
            'summary': f'Notebook execution timed out after {timeout} seconds.',
        }
    except Exception as e:
        return {
            'success': False,
            'error_type': 'SUBPROCESS_ERROR',
            'summary': f'Failed to launch runner subprocess: {e}',
        }

    if proc.returncode != 0 and not proc.stdout.strip():
        return {
            'success': False,
            'error_type': 'SUBPROCESS_CRASH',
            'summary': f'Runner crashed with code {proc.returncode}: {proc.stderr}',
        }

    try:
        report = json.loads(proc.stdout.strip())
        return report
    except json.JSONDecodeError:
        return {
            'success': False,
            'error_type': 'OUTPUT_PARSE_ERROR',
            'summary': f'Unparseable runner output: {proc.stdout}\nErrors: {proc.stderr}',
        }


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Headless Datamine Notebook Runner')
    parser.add_argument('notebook', help='Path to notebook file')
    parser.add_argument('--log-path', help='Custom log path', default=None)
    args = parser.parse_args()

    result = _execute_cells(args.notebook, custom_log_path=args.log_path)
    print(json.dumps(result))
