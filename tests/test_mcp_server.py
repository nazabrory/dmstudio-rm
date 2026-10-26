import json
import os
import tempfile
import unittest

class TestMcpServer(unittest.TestCase):

    def test_read_recent_command_log(self):
        from dmstudio.mcp_server import read_recent_command_log

        res_str = read_recent_command_log(lines=10)
        res = json.loads(res_str)
        self.assertIn("log_path", res)
        # If Command.log exists on this system, content should be present
        if "error" not in res:
            self.assertIn("line_count", res)
            self.assertIn("content", res)

    def test_run_and_diagnose_notebook_missing_file(self):
        from dmstudio.mcp_server import run_and_diagnose_notebook

        res_str = run_and_diagnose_notebook("non_existent_notebook.ipynb")
        res = json.loads(res_str)
        self.assertFalse(res["success"])
        self.assertEqual(res["error_type"], "FILE_NOT_FOUND")

    def test_run_and_diagnose_notebook_success(self):
        from dmstudio.mcp_server import run_and_diagnose_notebook

        temp_dir = tempfile.mkdtemp()
        try:
            nb_data = {
                "cells": [
                    {
                        "cell_type": "code",
                        "execution_count": None,
                        "metadata": {},
                        "outputs": [],
                        "source": ["x = 42\n", "assert x == 42"],
                    }
                ],
                "metadata": {},
                "nbformat": 4,
                "nbformat_minor": 5,
            }
            nb_path = os.path.join(temp_dir, "mcp_test.ipynb")
            with open(nb_path, "w", encoding="utf-8") as f:
                json.dump(nb_data, f)

            res_str = run_and_diagnose_notebook(nb_path)
            res = json.loads(res_str)
            self.assertTrue(res["success"])
            self.assertEqual(res["total_cells"], 1)
        finally:
            import shutil
            if os.path.exists(temp_dir):
                shutil.rmtree(temp_dir)


if __name__ == "__main__":
    unittest.main()
