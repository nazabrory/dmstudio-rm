import json
import os
import tempfile
import unittest
from unittest.mock import MagicMock, patch

class TestNotebookRunner(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        import shutil
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)

    def _create_notebook(self, cells):
        nb_data = {
            "cells": [
                {
                    "cell_type": "code",
                    "execution_count": None,
                    "metadata": {},
                    "outputs": [],
                    "source": cell if isinstance(cell, list) else cell.splitlines(True),
                }
                for cell in cells
            ],
            "metadata": {},
            "nbformat": 4,
            "nbformat_minor": 5,
        }
        nb_path = os.path.join(self.temp_dir, "test_workflow.ipynb")
        with open(nb_path, "w", encoding="utf-8") as f:
            json.dump(nb_data, f)
        return nb_path

    def test_run_success_notebook(self):
        from dmstudio.notebook_runner import run_and_diagnose_notebook

        nb_path = self._create_notebook([
            "a = 10\nb = 20",
            "c = a + b\nassert c == 30",
        ])

        report = run_and_diagnose_notebook(nb_path, timeout=30)
        self.assertTrue(report["success"])
        self.assertEqual(report["total_cells"], 2)
        self.assertIn("All notebook cells executed successfully", report["summary"])

    def test_run_failing_python_cell(self):
        from dmstudio.notebook_runner import run_and_diagnose_notebook

        nb_path = self._create_notebook([
            "x = 100",
            "y = x / 0",  # ZeroDivisionError
            "z = 200",
        ])

        report = run_and_diagnose_notebook(nb_path, timeout=30)
        self.assertFalse(report["success"])
        self.assertEqual(report["failed_cell_index"], 1)
        self.assertEqual(report["error_type"], "PYTHON_EXCEPTION")
        self.assertIn("ZeroDivisionError", report["error_message"])
        self.assertIn("y = x / 0", report["failed_cell_code"])

    def test_run_failing_datamine_log_cell(self):
        from dmstudio.notebook_runner import run_and_diagnose_notebook

        custom_log = os.path.join(self.temp_dir, "Command.log")
        with open(custom_log, "w", encoding="utf-8") as f:
            f.write("Line 0\n")

        # Simulate a cell writing an error to custom_log
        sim_code = f"""
with open(r'{custom_log}', 'a', encoding='utf-8') as f:
    f.write('26/10/2026 10:40:00 : >>> ERROR: FIELD NOT FOUND IN FILE <<<\\n')
"""
        nb_path = self._create_notebook([
            "x = 1",
            sim_code,
        ])

        report = run_and_diagnose_notebook(nb_path, timeout=30, custom_log_path=custom_log)
        self.assertFalse(report["success"])
        self.assertEqual(report["failed_cell_index"], 1)
        self.assertEqual(report["error_type"], "DATAMINE_ERROR")
        self.assertIn("FIELD NOT FOUND", report["error_message"])

    def test_clean_cell_code_and_magics_execution(self):
        from dmstudio.notebook_runner import _clean_cell_code, run_and_diagnose_notebook

        # Unit test _clean_cell_code directly
        raw = "%%time\n%matplotlib inline\n!pip list\n?func\nx = 10"
        cleaned = _clean_cell_code(raw)
        self.assertIn("# [IPython magic stripped] %%time", cleaned)
        self.assertIn("# [IPython magic stripped] %matplotlib inline", cleaned)
        self.assertIn("# [Shell/Help stripped] !pip list", cleaned)
        self.assertIn("# [Shell/Help stripped] ?func", cleaned)
        self.assertIn("x = 10", cleaned)
        self.assertEqual(len(raw.splitlines()), len(cleaned.splitlines()))

        # End-to-end execution of cell magics in runner subprocess
        nb_path = self._create_notebook([
            "%%time\nx = 10\ny = 20",
            "%matplotlib inline\nz = x + y",
            "!pip --version\nassert z == 30",
        ])
        report = run_and_diagnose_notebook(nb_path, timeout=30)
        self.assertTrue(report["success"], msg=report.get("error_message"))
        self.assertEqual(report["total_cells"], 3)

    def test_plt_show_does_not_block(self):
        from dmstudio.notebook_runner import run_and_diagnose_notebook

        nb_path = self._create_notebook([
            "import matplotlib.pyplot as plt\nfig, ax = plt.subplots()\nax.plot([1, 2], [3, 4])\nplt.show()\nx = 42",
            "assert x == 42",
        ])
        report = run_and_diagnose_notebook(nb_path, timeout=30)
        self.assertTrue(report["success"], msg=report.get("error_message"))
        self.assertEqual(report["total_cells"], 2)

    def test_utf8_emoji_output_and_stdout_mixing(self):
        from dmstudio.notebook_runner import run_and_diagnose_notebook

        nb_path = self._create_notebook([
            "print('✅ Compositing complete! 🚀 Processed 12,500 intervals ⚡')\nval = 100",
            "print('🎉 Capping finished: 99.5% percentile applied 💎')\nassert val == 100",
        ])
        report = run_and_diagnose_notebook(nb_path, timeout=30)
        self.assertTrue(report["success"], msg=report.get("error_message"))
        self.assertEqual(report["total_cells"], 2)

    def test_attach_only_never_dispatches(self):
        from dmstudio import initialize

        # Scenario 1: Studio RM process is running, but ROT attachment fails
        mock_proc = MagicMock()
        mock_proc.info = {'name': 'studiorm.exe'}
        with patch('win32com.client.GetActiveObject', side_effect=Exception('ROT lookup failed')):
            with patch('psutil.process_iter', return_value=[mock_proc]):
                with patch('win32com.client.Dispatch') as mock_dispatch:
                    with self.assertRaises(RuntimeError) as ctx:
                        initialize.studio('StudioRM', attach_only=True)
                    self.assertIn("running, but failed to attach via COM Running Object Table", str(ctx.exception))
                    mock_dispatch.assert_not_called()

        # Scenario 2: Studio RM process is NOT running
        with patch('win32com.client.GetActiveObject', side_effect=Exception('ROT lookup failed')):
            with patch('psutil.process_iter', return_value=[]):
                with patch('win32com.client.Dispatch') as mock_dispatch:
                    with self.assertRaises(RuntimeError) as ctx:
                        initialize.studio('StudioRM', attach_only=True)
                    self.assertIn("process is not running", str(ctx.exception))
                    mock_dispatch.assert_not_called()

        # Scenario 3: attach_only=False falls back to Dispatch
        with patch('win32com.client.GetActiveObject', side_effect=Exception('ROT lookup failed')):
            with patch('win32com.client.Dispatch', return_value='mock_com_obj') as mock_dispatch:
                res = initialize.studio('StudioRM', attach_only=False)
                mock_dispatch.assert_called_once_with('Datamine.StudioRM.Application')


    def test_extra_auto_appends_go(self):
        from dmstudio.dmcommands import init

        mock_com = MagicMock()
        captured_commands = []
        mock_com.Parsecommand = lambda cmd: captured_commands.append(cmd)

        dmc = init.__new__(init)
        dmc.oScript = mock_com
        dmc.version = "MockVersion"
        dmc.strict = False
        dmc._capture = MagicMock()
        dmc._capture.mark = lambda: None
        dmc._capture.get_delta = lambda: ""

        # Case 1: Single quoted expression without GO -> inserts GO before closing quote
        dmc.extra(in_i="f_in", out_o="f_out", arguments="'BHID=100;'")
        self.assertIn("'BHID=100; GO'", captured_commands[-1])

        # Case 2: Double quoted expression without GO -> inserts GO before closing quote
        dmc.extra(in_i="f_in", out_o="f_out", arguments='"BHID=100;"')
        self.assertIn('"BHID=100; GO"', captured_commands[-1])

        # Case 3: Unquoted expression without GO -> appends GO
        dmc.extra(in_i="f_in", out_o="f_out", arguments="BHID=100;")
        self.assertIn("BHID=100; GO", captured_commands[-1])

        # Case 4: Expression already containing GO -> does not duplicate
        dmc.extra(in_i="f_in", out_o="f_out", arguments="'BHID=100; GO'")
        self.assertIn("'BHID=100; GO'", captured_commands[-1])
        self.assertNotIn("GO GO", captured_commands[-1])

        # Case 5: Case-insensitive 'go' -> does not duplicate
        dmc.extra(in_i="f_in", out_o="f_out", arguments="'BHID=100; go'")
        self.assertIn("'BHID=100; go'", captured_commands[-1])
        self.assertNotIn("go GO", captured_commands[-1])


if __name__ == "__main__":
    unittest.main()
