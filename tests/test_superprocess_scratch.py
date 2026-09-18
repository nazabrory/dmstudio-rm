'''
tests/test_superprocess_scratch.py
-----------------------------------

Unit tests for scratch lifecycle management in superprocesses (dxf_to_dm and display_ellipsoids).
Verifies that intermediate operations are routed through scratch_context, eliminating
hardcoded temporary table names and manual delete calls.
'''

import unittest
from unittest.mock import MagicMock, patch

import pandas as pd

from dmstudio import superprocess
from dmstudio.scratch import ScratchManager


class MockActiveProject:
    def __init__(self):
        self.ExtendedPrecision = 1
        self.Data = MagicMock()
        self.mock_obj = MagicMock()
        self.Data.LastObjectAdded = self.mock_obj


class MockCommandEngine:
    def __init__(self):
        self.oScript = MagicMock()
        self.active_project = MockActiveProject()
        self.oScript.ActiveProject = self.active_project
        self.calls = []
        self.deleted = []

    def extra(self, in_i, out_o, arguments='optional'):
        self.calls.append(('extra', in_i, out_o, arguments))

    def copy(self, in_i, out_o):
        self.calls.append(('copy', in_i, out_o))

    def delete(self, in_i, confirm_p=0):
        self.deleted.append(in_i)
        self.calls.append(('delete', in_i, confirm_p))

    def ellipse(self, wiretr_o, wirept_o, **kwargs):
        self.calls.append(('ellipse', wiretr_o, wirept_o, kwargs))

    def addtri(self, wiretr1_i, wirept1_i, wiretr2_i, wirept2_i, wiretrou_o, wireptou_o):
        self.calls.append(('addtri', wiretr1_i, wirept1_i, wiretr2_i, wirept2_i, wiretrou_o, wireptou_o))


class TestDxfToDmScratchLifecycle(unittest.TestCase):
    '''Seam 1: dxf_to_dm scratch lifecycle and eliminated hardcoded names.'''

    def setUp(self):
        self.mock_cmd = MockCommandEngine()

    def test_dxf_to_dm_without_zone_direct_save(self):
        '''When zone_f is None, saves directly to out_o without intermediate scratch tables.'''
        res = superprocess.dxf_to_dm('test.dxf', 'out_wire', zone_f=None, cmd=self.mock_cmd)
        self.assertEqual(res, ('out_wiretr', 'out_wirept'))
        self.mock_cmd.active_project.mock_obj.SaveAsDatamineFile.assert_called_once_with(
            'out_wire', 1, True, ""
        )
        self.mock_cmd.active_project.mock_obj.Unload.assert_called_once()
        # No deletes or intermediate copies
        self.assertEqual(self.mock_cmd.deleted, [])

    def test_dxf_to_dm_with_zone_uses_scratch_context(self):
        '''When zone_f is set, intermediate tables use managed scratch names and auto-clean.'''
        res = superprocess.dxf_to_dm(
            'test.dxf', 'out_wire', zone_f='ZONE', zone_p=101, cmd=self.mock_cmd
        )
        self.assertEqual(res, ('out_wiretr', 'out_wirept'))

        # Verify SaveAsDatamineFile called with an underscore-prefixed scratch root
        args, _ = self.mock_cmd.active_project.mock_obj.SaveAsDatamineFile.call_args
        temp_root = args[0]
        self.assertTrue(temp_root.startswith('_'), f"Scratch root '{temp_root}' must start with an underscore.")
        self.assertNotEqual(temp_root, '_t1', "Must not use hardcoded '_t1'.")

        # Verify extra was called with registered triangle scratch and out_wiretr
        extra_calls = [c for c in self.mock_cmd.calls if c[0] == 'extra']
        self.assertEqual(len(extra_calls), 1)
        _, in_tr, out_tr, extra_args = extra_calls[0]
        self.assertEqual(in_tr, temp_root + 'tr')
        self.assertEqual(out_tr, 'out_wiretr')
        self.assertIn('ZONE;N = 101', extra_args)

        # Verify copy was called with points scratch and out_wirept
        copy_calls = [c for c in self.mock_cmd.calls if c[0] == 'copy']
        self.assertEqual(len(copy_calls), 1)
        _, in_pt, out_pt = copy_calls[0]
        self.assertEqual(in_pt, temp_root + 'pt')
        self.assertEqual(out_pt, 'out_wirept')

        # Verify auto-cleanup cleaned up both intermediate tables
        self.assertIn(temp_root + 'tr', self.mock_cmd.deleted)
        self.assertIn(temp_root + 'pt', self.mock_cmd.deleted)

    def test_dxf_to_dm_cleans_scratch_on_error(self):
        '''If extra or copy raises an error, auto-cleanup still deletes intermediate scratch tables.'''
        def faulty_extra(*args, **kwargs):
            raise RuntimeError('Datamine EXTRA execution failed')

        self.mock_cmd.extra = faulty_extra

        with self.assertRaises(RuntimeError):
            superprocess.dxf_to_dm(
                'test.dxf', 'out_wire', zone_f='ZONE', zone_p='ORE', cmd=self.mock_cmd
            )

        # Even though extra failed, intermediate scratch tables should have been cleaned up
        args, _ = self.mock_cmd.active_project.mock_obj.SaveAsDatamineFile.call_args
        temp_root = args[0]
        self.assertIn(temp_root + 'tr', self.mock_cmd.deleted)
        self.assertIn(temp_root + 'pt', self.mock_cmd.deleted)


class TestDisplayEllipsoidsScratchLifecycle(unittest.TestCase):
    '''Seam 2: display_ellipsoids scratch lifecycle and eliminated hardcoded names.'''

    def setUp(self):
        self.mock_cmd = MockCommandEngine()
        self.sample_df = pd.DataFrame({
            'XPT': [100.0, 110.0],
            'YPT': [200.0, 210.0],
            'ZPT': [300.0, 310.0],
            'TRDIPDIR': [45.0, 135.0],
            'TRDIP': [30.0, 45.0],
            '_PLUNGE': [-90.0, -90.0],
        })

    @patch('dmstudio.superprocess.read_datamine')
    def test_display_ellipsoids_uses_scratch_context(self, mock_read_dm):
        '''Intermediate ellipse steps use managed scratch names and auto-clean without hardcoded names.'''
        mock_read_dm.return_value = self.sample_df

        res = superprocess.display_ellipsoids(
            in_i='samples',
            out_o='out_ellipses',
            num_ellipsoids_p=2,
            cmd=self.mock_cmd,
        )
        self.assertEqual(res, ('out_ellipsestr', 'out_ellipsespt'))

        # Check ellipse calls: verify no hardcoded '_1tr', '_1pt'
        ellipse_calls = [c for c in self.mock_cmd.calls if c[0] == 'ellipse']
        self.assertEqual(len(ellipse_calls), 2)
        for _, w_tr, w_pt, _ in ellipse_calls:
            self.assertTrue(w_tr.startswith('_'))
            self.assertTrue(w_pt.startswith('_'))
            self.assertNotIn(w_tr, ('_1tr', '_2tr', '_3tr'))
            self.assertNotIn(w_pt, ('_1pt', '_2pt', '_3pt'))

        # Check final output copy
        final_copies = [c for c in self.mock_cmd.calls if c[0] == 'copy' and c[2].startswith('out_ellipses')]
        self.assertEqual(len(final_copies), 2)

        # Check auto-cleanup: all created intermediate scratch tables were deleted
        self.assertTrue(len(self.mock_cmd.deleted) > 0)
        for deleted_table in self.mock_cmd.deleted:
            self.assertTrue(deleted_table.startswith('_'))
            self.assertNotIn(deleted_table, ('_1tr', '_2tr', '_3tr', '_1pt', '_2pt', '_3pt'))


if __name__ == '__main__':
    unittest.main()
