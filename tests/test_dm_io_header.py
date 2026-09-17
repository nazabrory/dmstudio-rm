'''
tests/test_dm_io_header.py
--------------------------

Unit tests for lightweight metadata and header inspection of Datamine binary tables (.dm/.dmx).
Covers Seam 1: read_datamine_header, Seam 2: read_datamine_summary, and Seam 3: Packaging/Agent re-exports.
'''

import os
import unittest
from unittest.mock import MagicMock, patch

from dmstudio.dm_io import read_datamine_header, read_datamine_summary


_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COLLARS_FILE = os.path.join(
    _PROJECT_ROOT,
    'tutorials', 'Database', 'DMTutorials', 'Data', 'VBOP', 'Datamine',
    'MineTrust', 'Drillhole Files', 'Master Files', 'mstCollars.dm'
)
COLLARS_DMX_FILE = os.path.join(
    _PROJECT_ROOT,
    'tutorials', 'Database', 'DMTutorials', 'Data', 'VBOP', 'Datamine',
    'MineTrust', 'Drillhole Files', 'Master Files', 'mstCollars.dmx'
)
BLOCK_MODEL_FILE = os.path.join(
    _PROJECT_ROOT,
    'tutorials', 'Database', 'DMTutorials', 'Data', 'VBOP', 'Datamine', 'OPDemo3PB.dm'
)


class TestReadDatamineHeader(unittest.TestCase):
    '''Test suite for Seam 1: read_datamine_header.'''

    def test_nonexistent_file_raises_runtime_error(self):
        '''Raises a descriptive RuntimeError if the file does not exist.'''
        fake_path = os.path.join(_PROJECT_ROOT, 'non_existent_file_xyz123.dm')
        with self.assertRaises(RuntimeError) as ctx:
            read_datamine_header(fake_path)
        err_msg = str(ctx.exception).lower()
        self.assertTrue('not exist' in err_msg or 'could not open' in err_msg)
        self.assertIn('non_existent_file_xyz123.dm', str(ctx.exception))

    def test_open_failure_raises_runtime_error(self):
        '''Raises a descriptive RuntimeError if the table cannot be opened by COM.'''
        mock_table = MagicMock()
        mock_table.Open.side_effect = Exception('Access denied or locked handle')

        with patch('win32com.client.Dispatch', return_value=mock_table):
            with self.assertRaises(RuntimeError) as ctx:
                read_datamine_header(COLLARS_FILE)
            self.assertIn('Could not open Datamine file', str(ctx.exception))

    def test_read_header_collars_schema(self):
        '''Inspects field definitions, data types, character lengths, and record count without loading all records.'''
        self.assertTrue(os.path.exists(COLLARS_FILE), 'Sample file not found: {}'.format(COLLARS_FILE))
        header = read_datamine_header(COLLARS_FILE)

        self.assertIsInstance(header, dict)
        self.assertEqual(header['record_count'], 26)
        self.assertEqual(header['field_count'], 9)
        self.assertIn('BHID', header['field_names'])
        self.assertIn('XCOLLAR', header['field_names'])
        self.assertIn('ENDDEPTH', header['field_names'])
        self.assertEqual(len(header['fields']), 9)

        # Check field structure
        field_by_name = {f['name']: f for f in header['fields']}
        bhid = field_by_name['BHID']
        self.assertEqual(bhid['type'], 3)
        self.assertEqual(bhid['type_name'], 'alphanumeric')
        self.assertEqual(bhid['size_chars'], 8)
        self.assertFalse(bhid['implicit'])

        xcollar = field_by_name['XCOLLAR']
        self.assertEqual(xcollar['type'], 1)
        self.assertEqual(xcollar['type_name'], 'numeric')
        self.assertFalse(xcollar['implicit'])

        self.assertIsInstance(header['description'], str)
        self.assertIsInstance(header['double_precision'], bool)
        self.assertIsInstance(header['attributes'], dict)

    def test_read_header_dmx_extended_table(self):
        '''Inspects Datamine extended tables (.dmx) in read-only mode.'''
        self.assertTrue(os.path.exists(COLLARS_DMX_FILE), 'Sample dmx file not found: {}'.format(COLLARS_DMX_FILE))
        header = read_datamine_header(COLLARS_DMX_FILE)

        self.assertIsInstance(header, dict)
        self.assertEqual(header['record_count'], 26)
        self.assertEqual(header['field_count'], 9)
        self.assertIn('BHID', header['field_names'])

    def test_read_header_block_model_attributes(self):
        '''Extracts global/implicit attributes from the first record for block models.'''
        self.assertTrue(os.path.exists(BLOCK_MODEL_FILE), 'Sample file not found: {}'.format(BLOCK_MODEL_FILE))
        header = read_datamine_header(BLOCK_MODEL_FILE)

        self.assertEqual(header['record_count'], 18981)
        self.assertGreater(header['field_count'], 20)

        attrs = header['attributes']
        self.assertIsInstance(attrs, dict)
        self.assertEqual(attrs.get('XMORIG'), 4700.0)
        self.assertEqual(attrs.get('YMORIG'), 10000.0)
        self.assertEqual(attrs.get('ZMORIG'), 1800.0)
        self.assertEqual(attrs.get('XINC'), 5.0)
        self.assertEqual(attrs.get('YINC'), 5.0)
        self.assertAlmostEqual(attrs.get('ZINC'), 3.1496, places=3)
        self.assertEqual(attrs.get('NX'), 80.0)
        self.assertEqual(attrs.get('NY'), 120.0)
        self.assertEqual(attrs.get('NZ'), 50.0)

    def test_guaranteed_cleanup_on_error(self):
        '''Guarantees table.Close() is called even if an error occurs during inspection.'''
        mock_table = MagicMock()
        mock_table.GetRowCount.return_value = 10
        type(mock_table).Schema = unittest.mock.PropertyMock(side_effect=RuntimeError('Corrupted schema descriptor'))

        with patch('win32com.client.Dispatch', return_value=mock_table):
            with self.assertRaises(RuntimeError):
                read_datamine_header(COLLARS_FILE)
            mock_table.Close.assert_called_once()

    def test_read_header_zero_record_prototype_model(self):
        '''Extracts model attributes and recognizes block model status for 0-record prototypes via schema defaults.'''
        mock_table = MagicMock()
        mock_table.GetRowCount.return_value = 0
        mock_table.EOF = True

        mock_schema = MagicMock()
        mock_fields = ['XMORIG', 'YMORIG', 'ZMORIG', 'XINC', 'YINC', 'ZINC', 'NX', 'NY', 'NZ']
        mock_defaults = {
            'XMORIG': 1000.0, 'YMORIG': 2000.0, 'ZMORIG': 300.0,
            'XINC': 10.0, 'YINC': 10.0, 'ZINC': 5.0,
            'NX': 50, 'NY': 60, 'NZ': 20
        }
        mock_schema.FieldCount = len(mock_fields)
        mock_schema.GetFieldName.side_effect = lambda idx: mock_fields[idx - 1]
        mock_schema.GetFieldType.return_value = 1  # numeric
        mock_schema.GetFieldSize.return_value = 4
        mock_schema.GetFieldSizeChars.return_value = 4
        mock_schema.GetFieldDefault.side_effect = lambda idx: mock_defaults.get(mock_fields[idx - 1])
        mock_schema.IsFieldImplicit.return_value = True
        mock_schema.Description = 'Model Prototype'
        mock_schema.DoublePrecision = False
        mock_schema.TypeHint = 1
        type(mock_table).Schema = mock_schema

        with patch('win32com.client.Dispatch', return_value=mock_table):
            header = read_datamine_header(COLLARS_FILE)
            self.assertEqual(header['record_count'], 0)
            self.assertEqual(header['attributes'].get('XMORIG'), 1000.0)
            self.assertEqual(header['attributes'].get('XINC'), 10.0)

            summary = read_datamine_summary(COLLARS_FILE)
            self.assertTrue(summary['is_block_model'])
            self.assertEqual(summary['model_attributes'].get('XMORIG'), 1000.0)


class TestReadDatamineSummary(unittest.TestCase):
    '''Test suite for Seam 2: read_datamine_summary.'''

    def test_summary_collars(self):
        '''Generates high-level summary metrics for non-model table.'''
        summary = read_datamine_summary(COLLARS_FILE)

        self.assertIsInstance(summary, dict)
        self.assertEqual(summary['filename'], 'mstCollars.dm')
        self.assertEqual(summary['record_count'], 26)
        self.assertEqual(summary['field_count'], 9)
        self.assertFalse(summary['is_block_model'])
        self.assertEqual(summary['model_attributes'], {})
        self.assertIn('XCOLLAR', summary['numeric_fields'])
        self.assertIn('BHID', summary['alphanumeric_fields'])
        self.assertNotIn('BHID', summary['numeric_fields'])

    def test_summary_block_model(self):
        '''Generates high-level summary metrics and detects block model origin attributes.'''
        summary = read_datamine_summary(BLOCK_MODEL_FILE)

        self.assertIsInstance(summary, dict)
        self.assertEqual(summary['filename'], 'OPDemo3PB.dm')
        self.assertEqual(summary['record_count'], 18981)
        self.assertTrue(summary['is_block_model'])
        self.assertEqual(summary['model_attributes'].get('XMORIG'), 4700.0)
        self.assertEqual(summary['model_attributes'].get('XINC'), 5.0)
        self.assertEqual(summary['model_attributes'].get('NX'), 80.0)
        self.assertIn('XC', summary['numeric_fields'])


class TestPackagingAndReExports(unittest.TestCase):
    '''Test suite for Seam 3: Packaging and Agent backwards-compatibility re-exports.'''

    def test_re_exports_in_agent_and_package_root(self):
        '''Functions must be accessible via dmstudio.agent and dmstudio root shortcuts.'''
        import dmstudio
        from dmstudio import agent, dm_io

        # Canonical module
        self.assertTrue(hasattr(dm_io, 'read_datamine_header'))
        self.assertTrue(hasattr(dm_io, 'read_datamine_summary'))
        self.assertTrue(hasattr(dm_io, 'read_dm_header'))
        self.assertTrue(hasattr(dm_io, 'read_dm_summary'))
        self.assertIs(dm_io.read_dm_header, dm_io.read_datamine_header)
        self.assertIs(dm_io.read_dm_summary, dm_io.read_datamine_summary)

        # agent.py compat re-export layer
        self.assertTrue(hasattr(agent, 'read_datamine_header'))
        self.assertTrue(hasattr(agent, 'read_datamine_summary'))
        self.assertTrue(hasattr(agent, 'read_dm_header'))
        self.assertTrue(hasattr(agent, 'read_dm_summary'))
        self.assertIs(agent.read_datamine_header, dm_io.read_datamine_header)
        self.assertIs(agent.read_datamine_summary, dm_io.read_datamine_summary)
        self.assertIs(agent.read_dm_header, dm_io.read_datamine_header)
        self.assertIs(agent.read_dm_summary, dm_io.read_datamine_summary)

        # dmstudio root package shortcuts
        self.assertTrue(hasattr(dmstudio, 'read_datamine_header'))
        self.assertTrue(hasattr(dmstudio, 'read_datamine_summary'))
        self.assertTrue(hasattr(dmstudio, 'read_dm_header'))
        self.assertTrue(hasattr(dmstudio, 'read_dm_summary'))
        self.assertIs(dmstudio.read_datamine_header, dm_io.read_datamine_header)
        self.assertIs(dmstudio.read_datamine_summary, dm_io.read_datamine_summary)
        self.assertIs(dmstudio.read_dm_header, dm_io.read_datamine_header)
        self.assertIs(dmstudio.read_dm_summary, dm_io.read_datamine_summary)


if __name__ == '__main__':
    unittest.main()
