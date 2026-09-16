'''
tests/test_validator.py
-----------------------

Unit tests for the Datamine CLI command validator and linter.
Verifies syntax validation, missing whitespace detection, backslash checks,
and execution engine integration without requiring an active Studio RM session or license.
'''

import unittest
import warnings

from dmstudio.validator import lint_command, validate_command


class TestCommandLinter(unittest.TestCase):
    '''Test suite for dmstudio.validator.lint_command (Seam 1).'''

    def test_clean_valid_commands(self):
        '''Valid commands with standard parameters, options, and expressions must produce zero issues.'''
        valid_commands = [
            'mgsort &in=collars &out=sorted *key1=BHID',
            'desurv &inmods=collars &inmods1=surveys &out=dholes @survsmth=1 @print=0',
            'extra &in=data &out=data_out {AU_PPM = AU * 1000}',
            'extra &in=data &out=data_out {AU_PPM=AU*1000}',
            'selcop &in=dholes &out=filtered {FROM > 10.0 and TO < 50.0}',
            'copy &in=_vb_collars &out=collars_copy',
            'mgsort &in=collars &out=sorted *key1=*none',
            'create-isoshells @model=blockmod @field=AU @value=1.0 @out=isoshell',
        ]
        for cmd in valid_commands:
            with self.subTest(cmd=cmd):
                issues = lint_command(cmd)
                self.assertEqual(issues, [], f"Expected no issues for valid command: '{cmd}', got: {issues}")

    def test_detect_missing_whitespace_between_parameters(self):
        '''Proactively detect adjacent parameters lacking whitespace.'''
        cases = [
            ('&ERRORS=out*BHID=BHID', '*BHID'),
            ('file@PARAM=val', '@PARAM'),
            ('&in=collars&out=sorted', '&out'),
            ('*KEY1=BHID*KEY2=FROM', '*KEY2'),
            ('@PARAM1=1@PARAM2=2', '@PARAM2'),
            ('copy&in=collars &out=sorted', '&in'),
            ('cmd {AU>0}&out=res', '&out'),
            ('copy &in=&out=sorted', '&out'),
        ]
        for cmd, expected_token in cases:
            with self.subTest(cmd=cmd, expected_token=expected_token):
                issues = lint_command(cmd)
                self.assertGreater(len(issues), 0, f"Expected issues for malformed command '{cmd}'")
                self.assertTrue(
                    any('whitespace' in issue.lower() and expected_token in issue for issue in issues),
                    f"Expected issue mentioning whitespace and '{expected_token}', got: {issues}"
                )

    def test_detect_windows_backslashes_with_remediation(self):
        '''Detect Windows backslashes and advise using logical names or ActiveProject.AddFile.'''
        cmd = r'mgsort &in=C:\Projects\Data\collars.dm &out=sorted'
        issues = lint_command(cmd)
        self.assertGreater(len(issues), 0)
        has_backslash_guidance = any(
            'backslash' in issue.lower() and ('logical' in issue.lower() or 'addfile' in issue.lower())
            for issue in issues
        )
        self.assertTrue(
            has_backslash_guidance,
            f"Expected guidance mentioning backslash and logical names or AddFile, got: {issues}"
        )


class TestCommandValidator(unittest.TestCase):
    '''Test suite for dmstudio.validator.validate_command (Seam 1).'''

    def test_valid_command_returns_empty_and_no_warning(self):
        '''Valid commands must return an empty list and not trigger warnings or errors.'''
        with warnings.catch_warnings(record=True) as recorded_warnings:
            warnings.simplefilter('always')
            issues = validate_command('mgsort &in=collars &out=sorted *key1=BHID', strict=False)
            self.assertEqual(issues, [])
            self.assertEqual(len(recorded_warnings), 0)

            # Strict mode should also succeed cleanly
            issues_strict = validate_command('mgsort &in=collars &out=sorted *key1=BHID', strict=True)
            self.assertEqual(issues_strict, [])

    def test_default_warning_mode_emits_user_warning(self):
        '''Default mode (strict=False) must emit a UserWarning and return issues list.'''
        cmd = r'copy &in=C:\temp\collars.dm&out=collars_copy'
        with warnings.catch_warnings(record=True) as recorded_warnings:
            warnings.simplefilter('always')
            issues = validate_command(cmd, strict=False)

            self.assertGreater(len(issues), 0)
            self.assertEqual(len(recorded_warnings), 1)
            self.assertTrue(issubclass(recorded_warnings[0].category, UserWarning))
            warning_msg = str(recorded_warnings[0].message)
            self.assertIn('Pre-flight command validation detected', warning_msg)
            self.assertIn('backslash', warning_msg.lower())
            self.assertIn('&out', warning_msg)

    def test_strict_mode_raises_value_error(self):
        '''Strict mode (strict=True) must raise ValueError containing actionable diagnostics.'''
        cmd = 'mgsort &in=collars*key1=BHID'
        with self.assertRaises(ValueError) as ctx:
            validate_command(cmd, strict=True)
        err_msg = str(ctx.exception)
        self.assertIn('Pre-flight command validation detected', err_msg)
        self.assertIn('*key1', err_msg)


class TestPackagingAndReExports(unittest.TestCase):
    '''Test suite for package exports and compatibility re-exports.'''

    def test_canonical_and_compat_exports(self):
        '''lint_command and validate_command must be accessible via canonical and compat modules.'''
        import dmstudio
        from dmstudio import agent

        self.assertTrue(hasattr(dmstudio, 'validator'))
        self.assertTrue(callable(getattr(dmstudio.validator, 'lint_command', None)))
        self.assertTrue(callable(getattr(dmstudio.validator, 'validate_command', None)))

        self.assertTrue(hasattr(agent, 'lint_command'))
        self.assertTrue(hasattr(agent, 'validate_command'))
        self.assertIs(agent.lint_command, dmstudio.validator.lint_command)
        self.assertIs(agent.validate_command, dmstudio.validator.validate_command)


class MockStudio:
    '''Mock COM Studio object for offline command dispatch inspection.'''

    def __init__(self):
        self.dispatched = []

    def Parsecommand(self, cmd):
        self.dispatched.append(cmd)


class TestExecutionEngineIntegration(unittest.TestCase):
    '''Test suite for dmcommands.init and dmfiles.init pre-flight validation integration (Seam 2).'''

    def test_dmcommands_run_command_warning_mode(self):
        '''dmcommands.init.run_command emits warning and dispatches when strict=False.'''
        from dmstudio import dmcommands

        cmd = dmcommands.init.__new__(dmcommands.init)
        cmd.oScript = MockStudio()
        cmd.version = None
        cmd.strict = False

        malformed = 'mgsort &in=collars*key1=BHID'
        with warnings.catch_warnings(record=True) as recorded_warnings:
            warnings.simplefilter('always')
            cmd.run_command(malformed)

            self.assertEqual(len(recorded_warnings), 1)
            self.assertTrue(issubclass(recorded_warnings[0].category, UserWarning))
            self.assertEqual(cmd.oScript.dispatched, [malformed])

    def test_dmcommands_run_command_strict_mode(self):
        '''dmcommands.init.run_command raises ValueError and blocks dispatch when strict=True.'''
        from dmstudio import dmcommands

        cmd = dmcommands.init.__new__(dmcommands.init)
        cmd.oScript = MockStudio()
        cmd.version = None
        cmd.strict = True

        malformed = 'mgsort &in=collars*key1=BHID'
        with self.assertRaises(ValueError):
            cmd.run_command(malformed)

        # COM Parsecommand must NOT have been called
        self.assertEqual(cmd.oScript.dispatched, [])

    def test_dmfiles_run_command_warning_and_strict(self):
        '''dmfiles.init.run_command validates prior to dispatching to COM.'''
        from dmstudio import dmfiles

        files_cmd = dmfiles.init.__new__(dmfiles.init)
        files_cmd.oScript = MockStudio()
        files_cmd.version = None
        files_cmd.strict = True

        malformed = r'inpfil &out=C:\data\new_file.dm'
        with self.assertRaises(ValueError):
            files_cmd.run_command(malformed)
        self.assertEqual(files_cmd.oScript.dispatched, [])

        # Strict=False emits warning and dispatches
        files_cmd.strict = False
        with warnings.catch_warnings(record=True) as recorded_warnings:
            warnings.simplefilter('always')
            files_cmd.run_command(malformed)
            self.assertEqual(len(recorded_warnings), 1)
            self.assertEqual(files_cmd.oScript.dispatched, [malformed])

    def test_special_create_isoshells_validation(self):
        '''special.create_isoshells warns if backslash or invalid parameter passed.'''
        from dmstudio import special

        mock_studio = MockStudio()
        malformed_path = r'C:\data\isoshell'
        with warnings.catch_warnings(record=True) as recorded_warnings:
            warnings.simplefilter('always')
            special.create_isoshells(mock_studio, model='bm', field='AU', out=malformed_path)
            self.assertEqual(len(recorded_warnings), 1)
            self.assertTrue(issubclass(recorded_warnings[0].category, UserWarning))
            self.assertIn('backslash', str(recorded_warnings[0].message).lower())
            self.assertEqual(len(mock_studio.dispatched), 1)

    def test_special_create_isoshells_strict_mode(self):
        '''special.create_isoshells raises ValueError and halts dispatch when strict=True.'''
        from dmstudio import special

        mock_studio = MockStudio()
        malformed_path = r'C:\data\isoshell'
        with self.assertRaises(ValueError):
            special.create_isoshells(mock_studio, strict=True, model='bm', field='AU', out=malformed_path)
        self.assertEqual(mock_studio.dispatched, [])






if __name__ == '__main__':
    unittest.main()
