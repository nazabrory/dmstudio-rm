'''
tests/test_sandbox_export.py
----------------------------

Live sandbox integration tests for DataFrame export and scratch lifecycle with Datamine Studio RM.
Requires an active Datamine Studio RM session with tutorials/test_sandbox/Project.rmproj loaded.
If Studio RM is not running or no project is active, tests gracefully skip.
'''

import os
import sys
import unittest

import pandas as pd

# Ensure project root is on sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dmstudio import initialize, dmcommands, to_datamine, read_datamine, patch_dataframe


class TestSandboxExport(unittest.TestCase):
    '''Sandbox integration test against active Studio RM session.'''

    @classmethod
    def setUpClass(cls):
        cls.oScript = None
        cls.project = None
        cls.has_active_project = False
        cls.proj_folder = None

        try:
            cls.oScript = initialize.studio('StudioRM')
            if cls.oScript and getattr(cls.oScript, 'ActiveProject', None):
                cls.project = cls.oScript.ActiveProject
                cls.proj_folder = getattr(cls.project, 'Folder', None) or getattr(cls.project, 'Directory', None)
                cls.has_active_project = True
        except Exception:
            cls.has_active_project = False

    def setUp(self):
        if not self.has_active_project or not self.proj_folder:
            self.skipTest("Datamine Studio RM is not running with an active project. Skipping live sandbox test.")
        self.cmd = dmcommands.init('StudioRM')

    def test_live_to_datamine_export_and_readback(self):
        '''Export DataFrame to project folder and verify 0 unmanaged temporary files.'''
        test_df = pd.DataFrame({
            'BHID': ['HOLE1', 'HOLE2', 'HOLE3'],
            'FROM': [0.0, 10.0, 20.0],
            'TO': [10.0, 20.0, 30.0],
            'AU': [0.55, 1.82, 3.41],
        })

        out_table = 't_live_export.dmx'
        out_path = os.path.join(self.proj_folder, out_table)

        # Remove prior test file if exists
        if os.path.exists(out_path):
            os.remove(out_path)

        # Snapshot project folder before export
        before_files = set(os.listdir(self.proj_folder))

        # Perform streamlined export
        result = to_datamine(test_df, out_path, project_folder=self.proj_folder, cmd=self.cmd)
        self.assertEqual(result, out_path)
        self.assertTrue(os.path.exists(out_path), "Exported Datamine file must exist.")

        # Read back table and assert values
        readback_df = read_datamine(out_table, project_folder=self.proj_folder, cmd=self.cmd)
        self.assertEqual(len(readback_df), len(test_df))
        self.assertIn('BHID', readback_df.columns)
        self.assertIn('AU', readback_df.columns)

        read_bhids = [str(v).strip() for v in readback_df['BHID']]
        self.assertEqual(read_bhids, ['HOLE1', 'HOLE2', 'HOLE3'])

        # Snapshot project folder after export
        after_files = set(os.listdir(self.proj_folder))
        new_files = after_files - before_files

        # Ensure the only new durable file is out_table, and NO df_out_ files exist
        self.assertIn(out_table, new_files)
        unmanaged = [f for f in new_files if f.startswith('df_out_') or f.startswith('in_')]
        self.assertEqual(unmanaged, [], f"Found unmanaged temporary files: {unmanaged}")

        # Cleanup
        try:
            self.cmd.delete(in_i='t_live_export', confirm_p=0)
        except Exception:
            pass
        if os.path.exists(out_path):
            try:
                os.remove(out_path)
            except Exception:
                pass

    def test_live_patched_dataframe_export(self):
        '''Verify monkey-patched DataFrame.to_datamine() method in live sandbox.'''
        patch_dataframe()

        test_df = pd.DataFrame({
            'ZONE': [1, 2],
            'DENSITY': [2.65, 2.78],
        })

        out_table = 't_live_patched.dmx'
        out_path = os.path.join(self.proj_folder, out_table)

        if os.path.exists(out_path):
            os.remove(out_path)

        test_df.to_datamine(out_path, project_folder=self.proj_folder, cmd=self.cmd)
        self.assertTrue(os.path.exists(out_path))

        read_df = read_datamine(out_table, project_folder=self.proj_folder, cmd=self.cmd)
        self.assertEqual(len(read_df), 2)

        # Cleanup
        try:
            self.cmd.delete(in_i='t_live_patched', confirm_p=0)
        except Exception:
            pass
        if os.path.exists(out_path):
            try:
                os.remove(out_path)
            except Exception:
                pass


if __name__ == '__main__':
    unittest.main()
