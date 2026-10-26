import os
import tempfile
import unittest

class TestOutputCapture(unittest.TestCase):

    def test_classify_log_delta_success(self):
        from dmstudio.output_capture import classify_log_delta
        log_sample = """
26/10/2026 10:12:16 :  RETRIEVAL FIELDS
26/10/2026 10:12:16 :  Written 15293 rows.
26/10/2026 10:12:16 : >>> COPY     Complete <<< 
"""
        success, errors, warnings = classify_log_delta(log_sample)
        self.assertTrue(success)
        self.assertEqual(len(errors), 0)

    def test_classify_log_delta_error(self):
        from dmstudio.output_capture import classify_log_delta
        log_sample = """
26/10/2026 10:15:22 : Checking fields...
26/10/2026 10:15:22 : >>> ERROR: FIELD STRAT DOES NOT EXIST IN FILE collars <<<
26/10/2026 10:15:22 : Process failed
"""
        success, errors, warnings = classify_log_delta(log_sample)
        self.assertFalse(success)
        self.assertTrue(any("FIELD STRAT DOES NOT EXIST" in err for err in errors))

    def test_command_log_capture_delta(self):
        from dmstudio.output_capture import CommandLogCapture

        with tempfile.NamedTemporaryFile("w+", delete=False, encoding="utf-8") as f:
            f.write("Line 1: prior logs\n")
            f.flush()
            temp_path = f.name

        try:
            capture = CommandLogCapture(log_path=temp_path)
            capture.mark()

            with open(temp_path, "a", encoding="utf-8") as f:
                f.write("Line 2: >>> SORTX    Complete <<<\n")

            delta = capture.get_delta()
            self.assertIn(">>> SORTX    Complete <<<", delta)
            self.assertNotIn("Line 1: prior logs", delta)
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

    def test_command_capture_context_manager(self):
        from dmstudio.output_capture import CommandLogCapture, command_capture

        with tempfile.NamedTemporaryFile("w+", delete=False, encoding="utf-8") as f:
            f.write("Initial log line\n")
            f.flush()
            temp_path = f.name

        try:
            capture = CommandLogCapture(log_path=temp_path)
            with command_capture(capture=capture) as res:
                with open(temp_path, "a", encoding="utf-8") as f:
                    f.write("26/10/2026 10:20:00 : >>> MGSORT   Complete <<<\n")

            self.assertTrue(res.success)
            self.assertIn("MGSORT   Complete", res.output)
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)


if __name__ == "__main__":
    unittest.main()
