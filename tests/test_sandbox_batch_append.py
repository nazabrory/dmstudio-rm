'''
tests/test_sandbox_batch_append.py
----------------------------------

Live sandbox integration test for batch_append superprocess with Datamine Studio RM.
Requires an active Datamine Studio RM session with tutorials/test_sandbox/Project.rmproj loaded.
If Studio RM is not running or no project is active, tests gracefully skip.
'''

import os
import sys
import unittest

# Ensure project root is on sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dmstudio import initialize, dmcommands, superprocess, sandbox
from dmstudio.dm_io import read_datamine


class TestSandboxBatchAppend(unittest.TestCase):
    '''Sandbox integration test against active Studio RM session.'''

    @classmethod
    def setUpClass(cls):
        cls.oScript = None
        cls.project = None
        cls.has_active_project = False

        try:
            cls.oScript = initialize.studio('StudioRM')
            if cls.oScript and getattr(cls.oScript, 'ActiveProject', None):
                cls.project = cls.oScript.ActiveProject
                cls.has_active_project = True
        except Exception:
            cls.has_active_project = False

    def setUp(self):
        if not self.has_active_project:
            self.skipTest("Datamine Studio RM is not running with an active project. Skipping live sandbox test.")

    def test_live_batch_append_with_collars(self):
        '''Combine collar subsets, tag with provenance metadata, and sort on BHID.'''
        cmd = dmcommands.init('StudioRM')

        # Ensure sandbox has collar datasets
        sandbox.copy_database_files(['_vb_collars.dmx'])

        # Create two subsets using retrieval expressions
        cmd.copy(in_i='_vb_collars', out_o='t_test_col_a', retrieval='RECORD<=12')
        cmd.copy(in_i='_vb_collars', out_o='t_test_col_b', retrieval='RECORD>12')

        df_a = read_datamine('t_test_col_a.dmx')
        df_b = read_datamine('t_test_col_b.dmx')
        expected_total_rows = len(df_a) + len(df_b)

        out_table = 't_test_col_combined'

        result = superprocess.batch_append(
            tables_i=['t_test_col_a', 't_test_col_b'],
            out_o=out_table,
            flag_f='PROVENANCE',
            flag_map={'t_test_col_a': 'NORTH_PIT', 't_test_col_b': 'SOUTH_PIT'},
            sort_keys_f=['BHID'],
            cmd=cmd,
        )

        self.assertEqual(result, out_table)

        # Read back consolidated table and verify acceptance criteria
        df_out = read_datamine(f'{out_table}.dmx')
        self.assertEqual(len(df_out), expected_total_rows, "Total rows must equal sum of inputs.")
        self.assertIn('PROVENANCE', df_out.columns, "Provenance flag column must exist.")

        flag_vals = set(df_out['PROVENANCE'].str.strip())
        self.assertEqual(flag_vals, {'NORTH_PIT', 'SOUTH_PIT'}, "Flag values must match mapped values.")

        # Verify sorting by BHID
        bhids = list(df_out['BHID'].str.strip())
        self.assertEqual(bhids, sorted(bhids), "Output table records must be sorted by BHID.")

        # Clean up test output tables
        cmd.delete(in_i='t_test_col_a', confirm_p=0)
        cmd.delete(in_i='t_test_col_b', confirm_p=0)
        cmd.delete(in_i=out_table, confirm_p=0)


if __name__ == '__main__':
    unittest.main()
