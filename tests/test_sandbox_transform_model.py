'''
tests/test_sandbox_transform_model.py
-------------------------------------

Live sandbox integration test for transform_model superprocess with Datamine Studio RM.
Requires an active Datamine Studio RM session with tutorials/test_sandbox/Project.rmproj loaded.
If Studio RM is not running or no project is active, tests gracefully skip.
'''

import os
import sys
import unittest

# Ensure project root is on sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dmstudio import initialize, dmcommands, dmfiles, superprocess
from dmstudio.dm_io import read_datamine_header


class TestSandboxTransformModel(unittest.TestCase):
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

    def test_live_transform_prototype(self):
        '''Generate a test prototype, transform its origin coordinates, and verify via read_datamine_header.'''
        cmd = dmcommands.init('StudioRM')
        dm_fil = dmfiles.init('StudioRM')

        orig_proto = 't_test_orig_proto'
        trans_proto = 't_test_trans_proto'

        # 1. Create a base prototype (Origin: 5000, 4000, 100; Inc: 10, 10, 10; Counts: 20, 20, 10)
        dm_fil.protom(
            out_o=orig_proto,
            rotmod_p=0,
            arguments=" 'N' 'Y' '5000' '4000' '100' '10' '10' '10' '20' '20' '10'",
        )

        # Verify base prototype origin via bare logical table name resolution
        hdr_orig = read_datamine_header(orig_proto)
        attrs_orig = hdr_orig['attributes']
        self.assertAlmostEqual(float(attrs_orig['XMORIG']), 5000.0, places=2)
        self.assertAlmostEqual(float(attrs_orig['YMORIG']), 4000.0, places=2)
        self.assertAlmostEqual(float(attrs_orig['ZMORIG']), 100.0, places=2)

        # 2. Transform prototype origin by dx=500, dy=600, dz=50
        result = superprocess.transform_model(
            model_i=orig_proto,
            out_o=trans_proto,
            dx_p=500.0,
            dy_p=600.0,
            dz_p=50.0,
            is_prototype=True,
            cmd=cmd,
        )
        self.assertEqual(result, trans_proto)

        # 3. Verify transformed prototype origin via bare logical table name resolution
        hdr_trans = read_datamine_header(trans_proto)
        attrs_trans = hdr_trans['attributes']
        self.assertAlmostEqual(float(attrs_trans['XMORIG']), 5500.0, places=2)
        self.assertAlmostEqual(float(attrs_trans['YMORIG']), 4600.0, places=2)
        self.assertAlmostEqual(float(attrs_trans['ZMORIG']), 150.0, places=2)

        # Clean up test files
        cmd.delete(in_i=orig_proto, confirm_p=0)
        cmd.delete(in_i=trans_proto, confirm_p=0)


if __name__ == '__main__':
    unittest.main()
