'''
tests/test_sandbox_resilience.py
--------------------------------

Offline unit test suite for sandbox file copying resilience.
Validates that _safe_copy and copy_database_files gracefully handle Windows
file-locking errors (WinError 32 PermissionError) when existing datasets are open
in active Datamine Studio RM sessions.
'''

import os
import shutil
import tempfile
import unittest
from unittest.mock import patch

from dmstudio import sandbox


class TestSandboxResilience(unittest.TestCase):
    '''Test defensive copying behavior in dmstudio.sandbox.'''

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.src_file = os.path.join(self.test_dir, 'source.txt')
        with open(self.src_file, 'w', encoding='utf-8') as f:
            f.write('Sample Datamine content')

    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_safe_copy_normal(self):
        '''_safe_copy successfully copies file when destination is unlocked.'''
        dst_file = os.path.join(self.test_dir, 'dest_normal.txt')
        result = sandbox._safe_copy(self.src_file, dst_file, 'dest_normal.txt')
        self.assertTrue(result)
        self.assertTrue(os.path.exists(dst_file))
        with open(dst_file, 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), 'Sample Datamine content')

    def test_safe_copy_locked_existing_nonempty(self):
        '''_safe_copy recovers gracefully when destination is locked by active session.'''
        dst_file = os.path.join(self.test_dir, 'dest_locked.txt')
        with open(dst_file, 'w', encoding='utf-8') as f:
            f.write('Existing locked content')

        perm_err = PermissionError(32, 'The process cannot access the file because it is being used by another process')
        perm_err.winerror = 32

        with patch('shutil.copy2', side_effect=perm_err):
            result = sandbox._safe_copy(self.src_file, dst_file, 'dest_locked.txt')
            self.assertFalse(result)

    def test_safe_copy_locked_missing_destination(self):
        '''_safe_copy re-raises PermissionError if destination does not exist.'''
        dst_file = os.path.join(self.test_dir, 'non_existent.txt')

        perm_err = PermissionError(13, 'Permission denied')
        with patch('shutil.copy2', side_effect=perm_err):
            with self.assertRaises(PermissionError):
                sandbox._safe_copy(self.src_file, dst_file, 'non_existent.txt')

    def test_safe_copy_locked_empty_destination(self):
        '''_safe_copy re-raises PermissionError if destination exists but is 0 bytes.'''
        dst_file = os.path.join(self.test_dir, 'empty.txt')
        open(dst_file, 'w').close()

        perm_err = PermissionError(32, 'The process cannot access the file because it is being used by another process')
        perm_err.winerror = 32
        with patch('shutil.copy2', side_effect=perm_err):
            with self.assertRaises(PermissionError):
                sandbox._safe_copy(self.src_file, dst_file, 'empty.txt')

    def test_safe_copy_oserror_winerror32(self):
        '''_safe_copy recovers on generic OSError with winerror 32.'''
        dst_file = os.path.join(self.test_dir, 'oserror_locked.txt')
        with open(dst_file, 'w', encoding='utf-8') as f:
            f.write('Existing valid data')

        os_err = OSError(32, 'File locked')
        os_err.winerror = 32
        with patch('shutil.copy2', side_effect=os_err):
            result = sandbox._safe_copy(self.src_file, dst_file, 'oserror_locked.txt')
            self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
