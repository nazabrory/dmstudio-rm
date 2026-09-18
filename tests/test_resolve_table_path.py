'''
tests/test_resolve_table_path.py
--------------------------------

Unit tests for centralized table path resolution seam in dmstudio.dm_io.
Verifies three-tier precedence:
1. Exact file match (absolute or relative to current working directory).
2. Extension probing (.dm, .dmx) in current working directory / relative path.
3. Active project folder probing (explicit project_folder, cmd.oScript.ActiveProject, or COM).
Also verifies input validation and descriptive error reporting for missing tables.
'''

import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock

from dmstudio.dm_io import (
    read_datamine,
    read_datamine_header,
    read_datamine_summary,
    resolve_table_path,
)
from dmstudio.superprocess import transform_model


class TestResolveTablePath(unittest.TestCase):
    '''Unit tests for resolve_table_path resolution seam.'''

    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        self.mock_proj_dir = self.temp_dir.name

    def test_invalid_table_name_raises_value_error(self) -> None:
        '''Rejects None, non-string, empty, and whitespace-only table names.'''
        for invalid in [None, 123, [], {}, True]:
            with self.assertRaises(ValueError):
                resolve_table_path(invalid)  # type: ignore

        for empty in ['', '   ', '\t\n']:
            with self.assertRaises(ValueError):
                resolve_table_path(empty)

    def test_exact_existing_file_absolute(self) -> None:
        '''Resolves an exact existing file given by an absolute path.'''
        test_file = os.path.join(self.mock_proj_dir, 'exact_table.dm')
        Path(test_file).touch()

        resolved = resolve_table_path(test_file)
        self.assertEqual(os.path.normpath(resolved), os.path.normpath(test_file))

    def test_exact_existing_file_relative(self) -> None:
        '''Resolves an exact existing file given by a relative path from current working directory.'''
        orig_cwd = os.getcwd()
        try:
            os.chdir(self.mock_proj_dir)
            Path('local_table.dm').touch()

            resolved = resolve_table_path('local_table.dm')
            expected = os.path.abspath('local_table.dm')
            self.assertEqual(os.path.normpath(resolved), os.path.normpath(expected))
        finally:
            os.chdir(orig_cwd)

    def test_cwd_extension_probing(self) -> None:
        '''Resolves bare name without extension in current working directory when .dm or .dmx exists.'''
        orig_cwd = os.getcwd()
        try:
            os.chdir(self.mock_proj_dir)
            Path('probed_table.dm').touch()

            resolved = resolve_table_path('probed_table')
            expected = os.path.abspath('probed_table.dm')
            self.assertEqual(os.path.normpath(resolved), os.path.normpath(expected))

            # Test .dmx probing
            Path('probed_dmx.dmx').touch()
            resolved_dmx = resolve_table_path('probed_dmx')
            expected_dmx = os.path.abspath('probed_dmx.dmx')
            self.assertEqual(os.path.normpath(resolved_dmx), os.path.normpath(expected_dmx))
        finally:
            os.chdir(orig_cwd)

    def test_explicit_project_folder_bare_name(self) -> None:
        '''Resolves bare table name in explicit project_folder.'''
        target = os.path.join(self.mock_proj_dir, 'collars.dm')
        Path(target).touch()

        # Call from a different directory
        resolved = resolve_table_path('collars', project_folder=self.mock_proj_dir)
        self.assertEqual(os.path.normpath(resolved), os.path.normpath(target))

    def test_explicit_project_folder_with_extension(self) -> None:
        '''Resolves table name with extension in explicit project_folder.'''
        target = os.path.join(self.mock_proj_dir, 'collars.dmx')
        Path(target).touch()

        resolved = resolve_table_path('collars.dmx', project_folder=self.mock_proj_dir)
        self.assertEqual(os.path.normpath(resolved), os.path.normpath(target))

    def test_cmd_active_project_folder(self) -> None:
        '''Resolves bare table name from cmd.oScript.ActiveProject.Folder.'''
        target = os.path.join(self.mock_proj_dir, 'model.dm')
        Path(target).touch()

        mock_cmd = MagicMock()
        mock_cmd.oScript.ActiveProject.Folder = self.mock_proj_dir
        del mock_cmd.oScript.ActiveProject.Directory  # Ensure only Folder is used

        resolved = resolve_table_path('model', cmd=mock_cmd)
        self.assertEqual(os.path.normpath(resolved), os.path.normpath(target))

    def test_cmd_active_project_directory(self) -> None:
        '''Resolves bare table name from cmd.oScript.ActiveProject.Directory fallback.'''
        target = os.path.join(self.mock_proj_dir, 'block_model.dmx')
        Path(target).touch()

        mock_cmd = MagicMock()
        mock_cmd.oScript.ActiveProject.Folder = None
        mock_cmd.oScript.ActiveProject.Directory = self.mock_proj_dir

        resolved = resolve_table_path('block_model', cmd=mock_cmd)
        self.assertEqual(os.path.normpath(resolved), os.path.normpath(target))

    def test_unresolved_table_raises_runtime_error_with_evaluated_paths(self) -> None:
        '''Raises descriptive RuntimeError showing searched locations when table is missing.'''
        with self.assertRaises(RuntimeError) as ctx:
            resolve_table_path('non_existent_table_xyz', project_folder=self.mock_proj_dir)

        err_msg = str(ctx.exception)
        self.assertIn('non_existent_table_xyz', err_msg)
        self.assertIn('Could not resolve Datamine table', err_msg)
        self.assertIn(self.mock_proj_dir, err_msg)


_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_COLLARS_DIR = os.path.join(
    _PROJECT_ROOT,
    'tutorials', 'Database', 'DMTutorials', 'Data', 'VBOP', 'Datamine',
    'MineTrust', 'Drillhole Files', 'Master Files'
)
_OPDEMO_DIR = os.path.join(
    _PROJECT_ROOT,
    'tutorials', 'Database', 'DMTutorials', 'Data', 'VBOP', 'Datamine'
)


class TestReadDatamineWithResolution(unittest.TestCase):
    '''Seam 2: Wiring resolve_table_path into read_datamine, read_datamine_header, and read_datamine_summary.'''

    def test_read_datamine_header_with_bare_name_and_project_folder(self) -> None:
        '''read_datamine_header resolves bare logical name in project_folder.'''
        hdr = read_datamine_header('mstCollars', project_folder=_COLLARS_DIR)
        self.assertIsInstance(hdr, dict)
        self.assertEqual(hdr['record_count'], 26)
        self.assertEqual(os.path.basename(hdr['filepath']), 'mstCollars.dm')

    def test_read_datamine_summary_with_bare_name_and_project_folder(self) -> None:
        '''read_datamine_summary resolves bare logical name in project_folder.'''
        summary = read_datamine_summary('OPDemo3PB', project_folder=_OPDEMO_DIR)
        self.assertIsInstance(summary, dict)
        self.assertEqual(summary['filename'], 'OPDemo3PB.dm')
        self.assertTrue(summary['is_block_model'])

    def test_read_datamine_with_bare_name_and_project_folder(self) -> None:
        '''read_datamine resolves bare logical name in project_folder and loads records.'''
        df = read_datamine('mstCollars', project_folder=_COLLARS_DIR)
        self.assertEqual(len(df), 26)
        self.assertIn('BHID', df.columns)

    def test_read_missing_table_raises_runtime_error_with_evaluated_paths(self) -> None:
        '''read_datamine_header raises descriptive RuntimeError when bare table cannot be found.'''
        with self.assertRaises(RuntimeError) as ctx:
            read_datamine_header('nonexistent_collars_table_123', project_folder=_COLLARS_DIR)
        self.assertIn('Could not resolve Datamine table', str(ctx.exception))
        self.assertIn('nonexistent_collars_table_123', str(ctx.exception))


class TestTransformModelPathResolution(unittest.TestCase):
    '''Seam 3: Wiring resolve_table_path into transform_model superprocess.'''

    def test_transform_model_resolves_bare_model_in_active_project(self) -> None:
        '''transform_model resolves bare model name from active project folder via resolve_table_path.'''
        mock_cmd = MagicMock()
        mock_cmd.oScript.ActiveProject.Folder = _OPDEMO_DIR
        copymod_calls = []
        mock_cmd.copymod.side_effect = lambda **kwargs: copymod_calls.append(kwargs)
        mock_cmd.delete.return_value = None

        result = transform_model(
            model_i='OPDemo3PB',
            out_o='out_transformed',
            dx_p=100.0,
            dy_p=200.0,
            cmd=mock_cmd,
        )
        self.assertEqual(result, 'out_transformed')
        self.assertEqual(len(copymod_calls), 1)

        # In OPDemo3PB.dm, XMORIG is 4700.0 and YMORIG is 10000.0
        # So shifted xneworig should be 4700.0 + 100.0 = 4800.0, yneworig = 10000.0 + 200.0 = 10200.0
        args = copymod_calls[0].get('arguments', '')
        self.assertIn('@xneworig=4800.0', args)
        self.assertIn('@yneworig=10200.0', args)

    def test_transform_model_prototype_resolves_bare_model(self) -> None:
        '''transform_model with is_prototype=True resolves bare model and calls protom.'''
        mock_cmd = MagicMock()
        mock_cmd.oScript.ActiveProject.Folder = _OPDEMO_DIR
        protom_calls = []
        mock_cmd.protom.side_effect = lambda **kwargs: protom_calls.append(kwargs)
        mock_cmd.delete.return_value = None

        result = transform_model(
            model_i='OPDemo3PB',
            out_o='out_transformed',
            dx_p=100.0,
            dy_p=200.0,
            is_prototype=True,
            cmd=mock_cmd,
        )
        self.assertEqual(result, 'out_transformed')
        self.assertEqual(len(protom_calls), 1)

        args = protom_calls[0].get('arguments', '')
        self.assertIn("'4800.0'", args)
        self.assertIn("'10200.0'", args)


class TestPackagingAndReExports(unittest.TestCase):
    '''Seam 4: Packaging and agent backwards-compatibility re-exports.'''

    def test_re_exports_in_agent_and_package_root(self) -> None:
        '''resolve_table_path must be accessible via canonical dmstudio, dmstudio.dm_io, and dmstudio.agent.'''
        import dmstudio
        from dmstudio import agent, dm_io

        self.assertTrue(hasattr(dm_io, 'resolve_table_path'))
        self.assertTrue(hasattr(dmstudio, 'resolve_table_path'))
        self.assertIs(dmstudio.resolve_table_path, dm_io.resolve_table_path)

        self.assertTrue(hasattr(agent, 'resolve_table_path'))
        self.assertIs(agent.resolve_table_path, dm_io.resolve_table_path)


if __name__ == '__main__':
    unittest.main()
