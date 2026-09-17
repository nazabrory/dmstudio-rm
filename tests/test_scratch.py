'''
tests/test_scratch.py
---------------------

Unit tests for the Datamine in-memory scratch file manager and context manager.
Verifies unique scratch name generation, collision resistance, naming constraints,
tracking, lifecycle cleanup, and backwards-compatibility re-exports without requiring
an active Datamine Studio RM session or license.
'''

import unittest

from dmstudio.scratch import scratch_context, ScratchManager


class TestScratchNameGeneration(unittest.TestCase):
    '''Seam 1: ScratchManager name generation and collision resistance.'''

    def setUp(self):
        self.mgr = ScratchManager()

    def test_default_scratch_name_starts_with_underscore(self):
        '''Scratch names must strictly begin with an underscore for Datamine in-memory tables.'''
        name = self.mgr.temp()
        self.assertTrue(name.startswith('_'), f"Scratch name '{name}' must start with an underscore.")
        self.assertFalse(name.startswith('__'), f"Scratch name '{name}' should not start with double underscores.")

    def test_scratch_name_with_suffix(self):
        '''Callers can provide an optional suffix keyword argument.'''
        name = self.mgr.temp(suffix='dh_sort')
        self.assertTrue(name.startswith('_'))
        self.assertIn('dh_sort', name)

    def test_scratch_name_with_positional_suffix(self):
        '''Callers can provide an optional suffix as a positional argument.'''
        name = self.mgr.temp('wireframe')
        self.assertTrue(name.startswith('_'))
        self.assertIn('wireframe', name)

    def test_strip_leading_underscore_from_suffix(self):
        '''If user passes a suffix with leading underscore, avoid producing double underscores.'''
        name = self.mgr.temp(suffix='_collars')
        self.assertTrue(name.startswith('_'))
        self.assertFalse(name.startswith('__'), f"Expected single leading underscore, got '{name}'")
        self.assertIn('collars', name)

    def test_sanitize_suffix_characters(self):
        '''Special characters and spaces in suffix must be sanitized to valid Datamine identifiers.'''
        name = self.mgr.temp(suffix='my test-file.1')
        self.assertTrue(name.startswith('_'))
        self.assertNotIn(' ', name)
        self.assertNotIn('.', name)
        self.assertNotIn('-', name)

    def test_collision_resistance_across_many_calls(self):
        '''Generating a large volume of scratch names must never produce collisions.'''
        names = [self.mgr.temp(suffix='step') for _ in range(1000)]
        self.assertEqual(len(names), len(set(names)), 'Collision detected among generated scratch names.')


class TestScratchTracking(unittest.TestCase):
    '''Seam 2: Scratch table tracking and lifecycle registry.'''

    def setUp(self):
        self.mgr = ScratchManager()

    def test_tracks_generated_names_in_order(self):
        '''All generated names must be recorded in order of creation.'''
        n1 = self.mgr.temp(suffix='first')
        n2 = self.mgr.temp(suffix='second')
        n3 = self.mgr.temp(suffix='third')
        self.assertEqual(self.mgr.tracked_names, [n1, n2, n3])

    def test_len_reflects_number_of_tracked_tables(self):
        '''len(mgr) reflects the count of generated scratch files.'''
        self.assertEqual(len(self.mgr), 0)
        self.mgr.temp()
        self.mgr.temp(suffix='step2')
        self.assertEqual(len(self.mgr), 2)

    def test_contains_membership_check(self):
        '''Checking `name in mgr` evaluates whether the name is tracked.'''
        n1 = self.mgr.temp(suffix='target')
        self.assertIn(n1, self.mgr)
        self.assertNotIn('_untracked_table', self.mgr)

    def test_manual_register_enforces_scratch_prefix(self):
        '''Manual registration accepts a custom scratch name, guaranteeing leading underscore.'''
        registered = self.mgr.register('custom_scratch')
        self.assertEqual(registered, '_custom_scratch')
        self.assertIn('_custom_scratch', self.mgr.tracked_names)

    def test_tracked_names_returns_copy_to_prevent_external_tampering(self):
        '''Modifying tracked_names list must not mutate the internal state of ScratchManager.'''
        self.mgr.temp(suffix='test')
        names = self.mgr.tracked_names
        names.append('_fake_scratch')
        self.assertNotIn('_fake_scratch', self.mgr.tracked_names)

    def test_report_summary(self):
        '''report() returns a structured dictionary of tracked tables.'''
        t1 = self.mgr.temp(suffix='first')
        t2 = self.mgr.temp(suffix='second')
        rep = self.mgr.report()
        self.assertEqual(rep['count'], 2)
        self.assertEqual(rep['tables'], [t1, t2])


class MockCommandEngine:
    '''Mock command engine recording delete calls for offline testing.'''

    def __init__(self, failing_tables=None):
        self.deleted_tables = []
        self.failing_tables = set(failing_tables or [])

    def delete(self, in_i, confirm_p=0):
        if in_i in self.failing_tables:
            raise RuntimeError(f'Failed to delete table {in_i}')
        self.deleted_tables.append((in_i, confirm_p))


class TestScratchContextLifecycle(unittest.TestCase):
    '''Seam 3: Context lifecycle, auto-cleanup, and error handling.'''

    def test_context_manager_yields_manager_instance(self):
        '''scratch_context yields an active ScratchManager instance.'''
        with scratch_context() as sc:
            self.assertIsInstance(sc, ScratchManager)
            t1 = sc.temp(suffix='sort')
            self.assertTrue(t1.startswith('_'))
            self.assertIn(t1, sc)

    def test_nested_contexts_maintain_independent_state(self):
        '''Nested scratch contexts must not mix up their tracked scratch tables.'''
        with scratch_context() as outer:
            o1 = outer.temp(suffix='outer')
            with scratch_context() as inner:
                i1 = inner.temp(suffix='inner')
                self.assertIn(i1, inner)
                self.assertNotIn(o1, inner)
            self.assertIn(o1, outer)
            self.assertNotIn(i1, outer)

    def test_explicit_cleanup_invokes_command_engine(self):
        '''Explicit cleanup() calls delete on each tracked scratch table.'''
        mock_cmd = MockCommandEngine()
        mgr = ScratchManager()
        t1 = mgr.temp(suffix='step1')
        t2 = mgr.temp(suffix='step2')

        deleted = mgr.cleanup(cmd=mock_cmd)

        expected = [(t1, 0), (t2, 0)]
        self.assertEqual(mock_cmd.deleted_tables, expected)
        self.assertEqual(deleted, [t1, t2])
        self.assertEqual(len(mgr), 0)

    def test_cleanup_without_cmd_returns_empty_and_preserves_tracking(self):
        '''Without cmd, cleanup cannot delete in-memory tables; returns empty list.'''
        mgr = ScratchManager()
        t1 = mgr.temp(suffix='no_cmd')
        deleted = mgr.cleanup(cmd=None, strict=False)
        self.assertEqual(deleted, [])
        self.assertIn(t1, mgr)

        with self.assertRaises(ValueError):
            mgr.cleanup(cmd=None, strict=True)

    def test_auto_cleanup_on_context_exit(self):
        '''Exiting scratch_context with auto_cleanup=True triggers cleanup automatically.'''
        mock_cmd = MockCommandEngine()

        with scratch_context(cmd=mock_cmd, auto_cleanup=True) as sc:
            t1 = sc.temp(suffix='temp1')
            t2 = sc.temp(suffix='temp2')

        self.assertEqual(mock_cmd.deleted_tables, [(t1, 0), (t2, 0)])

    def test_auto_cleanup_executes_on_exception_without_masking(self):
        '''Auto-cleanup runs even when an exception is raised inside the context block.'''
        mock_cmd = MockCommandEngine()

        with self.assertRaises(ValueError):
            with scratch_context(cmd=mock_cmd, auto_cleanup=True) as sc:
                t1 = sc.temp(suffix='fail')
                raise ValueError('Simulated pipeline failure')

        self.assertEqual(mock_cmd.deleted_tables, [(t1, 0)])

    def test_cleanup_handles_unmaterialized_tables_gracefully(self):
        '''Cleanup handles deletion failures gracefully unless strict=True is requested.'''
        mock_cmd = MockCommandEngine(failing_tables={'_missing_table'})
        mgr = ScratchManager()
        mgr.register('missing_table')
        t2 = mgr.temp(suffix='success')

        mgr.cleanup(cmd=mock_cmd, strict=False)
        self.assertEqual(mock_cmd.deleted_tables, [(t2, 0)])


class TestScratchReExports(unittest.TestCase):
    '''Seam 4: Re-exports and backwards-compatibility integration.'''

    def test_canonical_dmstudio_exports(self):
        '''dmstudio root exports scratch_context and ScratchManager.'''
        import dmstudio
        self.assertTrue(hasattr(dmstudio, 'scratch_context'))
        self.assertTrue(hasattr(dmstudio, 'ScratchManager'))
        self.assertTrue(hasattr(dmstudio, 'scratch'))

    def test_agent_backward_compatibility_reexports(self):
        '''dmstudio.agent re-exports scratch_context and ScratchManager.'''
        from dmstudio.agent import scratch_context as agent_sc, ScratchManager as AgentScratchManager
        from dmstudio.scratch import scratch_context as canon_sc, ScratchManager as CanonScratchManager

        self.assertIs(agent_sc, canon_sc)
        self.assertIs(AgentScratchManager, CanonScratchManager)


if __name__ == '__main__':
    unittest.main()
