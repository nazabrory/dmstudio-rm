'''
tests/test_dataframe_export.py
------------------------------

Unit tests for streamlined DataFrame export and leak-free table creation.
Verifies that:
1. special.inpfil accepts a pandas DataFrame directly without requiring a CSV file.
2. to_datamine uses underscore-prefixed in-memory scratch names (_df_out_...).
3. to_datamine eliminates redundant intermediate CSV roundtrips on disk.
4. to_datamine leaves zero un-underscored temporary files on completion or error.
'''

import os
import shutil
import tempfile
import unittest
from unittest.mock import MagicMock, patch

import pandas as pd

from dmstudio import special, dm_io
from dmstudio.dm_io import to_datamine


class TestDataFrameExportSeam(unittest.TestCase):
    '''Seam 3: Streamlined DataFrame export and leak-free lifecycle.'''

    def setUp(self):
        self.test_dir = tempfile.mkdtemp(prefix='dm_test_export_')
        self.df = pd.DataFrame({
            'BHID': ['DH001', 'DH002'],
            'FROM': [0.0, 5.0],
            'TO': [5.0, 10.0],
            'AU': [1.25, 3.50],
        })

    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)

    @patch('dmstudio.dmfiles.init')
    def test_inpfil_accepts_dataframe_directly_without_csv(self, mock_dmfiles_init):
        '''special.inpfil accepts df directly without requiring csv path or pd.read_csv.'''
        mock_dmf = MagicMock()
        mock_dmf.oScript = MagicMock()
        mock_dmf.oScript.ActiveProject.Folder = self.test_dir
        mock_dmfiles_init.return_value = mock_dmf

        special.inpfil(df=self.df, out_o='_test_direct_df')

        mock_dmf.inpfil.assert_called_once()
        _, kwargs = mock_dmf.inpfil.call_args
        self.assertEqual(kwargs['out_o'], '_test_direct_df')
        args_str = kwargs['arguments']
        self.assertIn('BHID', args_str)
        self.assertIn('AU', args_str)

    @patch('dmstudio.special.inpfil')
    def test_to_datamine_uses_underscore_scratch_name(self, mock_inpfil):
        '''to_datamine generates scratch names with leading underscore for in-memory handling.'''
        target_path = os.path.join(self.test_dir, 'target.dm')

        def side_effect(df=None, csv=None, out_o=None, definition=None, **kwargs):
            # Simulate Datamine creating the file in test_dir
            created = os.path.join(self.test_dir, out_o + '.dm')
            with open(created, 'w') as f:
                f.write('mock datamine content')

        mock_inpfil.side_effect = side_effect

        to_datamine(self.df, target_path, project_folder=self.test_dir)

        self.assertTrue(mock_inpfil.called)
        call_kwargs = mock_inpfil.call_args[1]
        out_o = call_kwargs.get('out_o')

        self.assertTrue(out_o.startswith('_'), f"Intermediate table '{out_o}' must start with underscore.")
        self.assertFalse(out_o.startswith('__'), f"Intermediate table '{out_o}' should not have double underscore.")
        self.assertTrue(os.path.exists(target_path), "Target file should have been moved to target_path.")

    @patch('dmstudio.special.inpfil')
    @patch('pandas.DataFrame.to_csv')
    def test_to_datamine_eliminates_redundant_csv_passes(self, mock_to_csv, mock_inpfil):
        '''to_datamine should NOT serialize the DataFrame to an intermediate CSV on disk.'''
        target_path = os.path.join(self.test_dir, 'target.dm')

        def side_effect(df=None, csv=None, out_o=None, definition=None, **kwargs):
            created = os.path.join(self.test_dir, out_o + '.dm')
            with open(created, 'w') as f:
                f.write('mock')

        mock_inpfil.side_effect = side_effect

        to_datamine(self.df, target_path, project_folder=self.test_dir)

        # Ensure df.to_csv was NOT called by to_datamine
        mock_to_csv.assert_not_called()
        # Ensure df was passed directly to special.inpfil
        self.assertTrue(mock_inpfil.called)
        self.assertIs(mock_inpfil.call_args[1].get('df'), self.df)

    @patch('dmstudio.special.inpfil')
    def test_to_datamine_leaves_zero_ununderscored_files_on_error(self, mock_inpfil):
        '''If export fails or crashes, no un-underscored temporary files are left in project folder.'''
        target_path = os.path.join(self.test_dir, 'target.dm')

        def failing_inpfil(*args, **kwargs):
            # Simulate a temporary underscore file left by crash
            out_o = kwargs.get('out_o', '_temp')
            created = os.path.join(self.test_dir, out_o + '.dm')
            with open(created, 'w') as f:
                f.write('partial')
            raise RuntimeError('Datamine crash during inpfil')

        mock_inpfil.side_effect = failing_inpfil

        with self.assertRaises(RuntimeError):
            to_datamine(self.df, target_path, project_folder=self.test_dir)

        # Inspect test_dir: NO un-underscored files (like df_out_...) must exist!
        files_in_dir = os.listdir(self.test_dir)
        ununderscored = [f for f in files_in_dir if not f.startswith('_') and f != 'target.dm']
        self.assertEqual(
            ununderscored, [],
            f"Found un-underscored temporary files left in project folder: {ununderscored}"
        )


if __name__ == '__main__':
    unittest.main()
