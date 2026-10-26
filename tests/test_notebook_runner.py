import json
import os
import tempfile
import unittest

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


if __name__ == "__main__":
    unittest.main()
