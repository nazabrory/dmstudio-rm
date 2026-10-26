import os
import tempfile
import unittest
from unittest.mock import MagicMock

class TestDmCommandsCapture(unittest.TestCase):

    def test_run_command_returns_execution_result(self):
        from dmstudio.dmcommands import init
        from dmstudio.output_capture import CommandLogCapture

        with tempfile.NamedTemporaryFile("w+", delete=False, encoding="utf-8") as f:
            f.write("Line 0\n")
            f.flush()
            temp_path = f.name

        try:
            # Create a mock studio COM object
            mock_com = MagicMock()
            
            def fake_parsecommand(cmd):
                # simulate Datamine writing to Command.log
                with open(temp_path, "a", encoding="utf-8") as lf:
                    lf.write("26/10/2026 10:30:00 : >>> MGSORT   Complete <<<\n")

            mock_com.Parsecommand = fake_parsecommand

            # Instantiate dmcommands.init bypassing COM attach
            dmc = init.__new__(init)
            dmc.oScript = mock_com
            dmc.version = "MockVersion"
            dmc.strict = False
            dmc._capture = CommandLogCapture(log_path=temp_path)

            res = dmc.run_command("mgsort &IN=test &OUT=sorted *KEY1=BHID")

            self.assertIsNotNone(res)
            self.assertTrue(res.success)
            self.assertIn("MGSORT   Complete", res.output)
            self.assertEqual(dmc.last_result, res)
            self.assertEqual(dmc.last_output, res.output)
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

    def test_run_command_detects_error(self):
        from dmstudio.dmcommands import init
        from dmstudio.output_capture import CommandLogCapture

        with tempfile.NamedTemporaryFile("w+", delete=False, encoding="utf-8") as f:
            f.write("Line 0\n")
            f.flush()
            temp_path = f.name

        try:
            mock_com = MagicMock()
            
            def fake_parsecommand_error(cmd):
                with open(temp_path, "a", encoding="utf-8") as lf:
                    lf.write("26/10/2026 10:30:00 : >>> ERROR: FIELD NOT FOUND <<<\n")

            mock_com.Parsecommand = fake_parsecommand_error

            dmc = init.__new__(init)
            dmc.oScript = mock_com
            dmc.version = "MockVersion"
            dmc.strict = False
            dmc._capture = CommandLogCapture(log_path=temp_path)

            res = dmc.run_command("mgsort &IN=test &OUT=sorted *KEY1=UNKNOWN")

            self.assertFalse(res.success)
            self.assertIn("FIELD NOT FOUND", res.errors[0])
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)


if __name__ == "__main__":
    unittest.main()
