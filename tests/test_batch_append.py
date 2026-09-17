'''
tests/test_batch_append.py
--------------------------

Unit tests for the multi-table batch append superprocess.
Verifies input parameter validation, single/multi-table chaining, managed scratch
file lifecycle cleanup, provenance flag tagging (default and mapped values),
final table sorting via mgsort, and backwards-compatibility re-exports.
Runs offline without requiring an active Datamine Studio RM session or license.
'''

import unittest
from typing import Any, Dict, List, Tuple

from dmstudio.superprocess import batch_append
from dmstudio import batch_append as root_batch_append
from dmstudio.agent import batch_append as agent_batch_append


class MockCommandEngine:
    '''Mock Studio RM command engine recording all executed commands.'''

    def __init__(self) -> None:
        self.calls: List[Tuple[str, Dict[str, Any]]] = []

    def copy(self, in_i: str, out_o: str, **kwargs: Any) -> None:
        self.calls.append(('copy', {'in_i': in_i, 'out_o': out_o, **kwargs}))

    def extra(self, in_i: str, out_o: str, arguments: str = 'optional', **kwargs: Any) -> None:
        self.calls.append(('extra', {'in_i': in_i, 'out_o': out_o, 'arguments': arguments, **kwargs}))

    def append(self, in1_i: str = None, in2_i: str = None, out_o: str = None, **kwargs: Any) -> None:
        self.calls.append(('append', {'in1_i': in1_i, 'in2_i': in2_i, 'out_o': out_o, **kwargs}))

    def mgsort(self, in_i: str = None, out_o: str = None, keys_f: Any = None, **kwargs: Any) -> None:
        self.calls.append(('mgsort', {'in_i': in_i, 'out_o': out_o, 'keys_f': keys_f, **kwargs}))

    def delete(self, in_i: str = None, confirm_p: int = 0, **kwargs: Any) -> None:
        self.calls.append(('delete', {'in_i': in_i, 'confirm_p': confirm_p, **kwargs}))


class TestBatchAppendValidation(unittest.TestCase):
    '''Seam 1: Input Validation and Parameter Normalization.'''

    def setUp(self) -> None:
        self.cmd = MockCommandEngine()

    def test_empty_table_list_raises_value_error(self) -> None:
        '''Empty tables list must raise descriptive ValueError.'''
        with self.assertRaises(ValueError) as ctx:
            batch_append([], out_o='out_tab', cmd=self.cmd)
        self.assertIn('empty', str(ctx.exception).lower())

    def test_non_list_tables_raises_value_error(self) -> None:
        '''Passing non-list/tuple (e.g. single string) must raise descriptive ValueError.'''
        with self.assertRaises(ValueError) as ctx:
            batch_append('single_table', out_o='out_tab', cmd=self.cmd)  # type: ignore
        self.assertIn('list', str(ctx.exception).lower())

    def test_none_tables_raises_value_error(self) -> None:
        '''Passing None as tables list must raise ValueError.'''
        with self.assertRaises(ValueError):
            batch_append(None, out_o='out_tab', cmd=self.cmd)  # type: ignore

    def test_non_string_elements_raise_value_error(self) -> None:
        '''Any non-string item in tables list must raise descriptive ValueError.'''
        with self.assertRaises(ValueError) as ctx:
            batch_append(['valid_tab', 123, 'another_tab'], out_o='out_tab', cmd=self.cmd)  # type: ignore
        self.assertIn('string', str(ctx.exception).lower())

        with self.assertRaises(ValueError) as ctx:
            batch_append(['valid_tab', None], out_o='out_tab', cmd=self.cmd)  # type: ignore
        self.assertIn('string', str(ctx.exception).lower())

    def test_empty_string_table_name_raises_value_error(self) -> None:
        '''Blank or whitespace-only table names must raise ValueError.'''
        with self.assertRaises(ValueError) as ctx:
            batch_append(['tab1', '   '], out_o='out_tab', cmd=self.cmd)
        self.assertIn('empty', str(ctx.exception).lower())

    def test_table_name_with_backslashes_raises_value_error(self) -> None:
        '''File paths with backslashes must raise ValueError directing to use logical names.'''
        with self.assertRaises(ValueError) as ctx:
            batch_append(['tab1', r'C:\Data\tab2'], out_o='out_tab', cmd=self.cmd)
        self.assertIn('backslash', str(ctx.exception).lower())

    def test_table_name_with_spaces_raises_value_error(self) -> None:
        '''Table names with spaces break Datamine parser and must raise ValueError.'''
        with self.assertRaises(ValueError) as ctx:
            batch_append(['tab1', 'my table'], out_o='out_tab', cmd=self.cmd)
        self.assertIn('space', str(ctx.exception).lower())

    def test_invalid_out_o_raises_value_error(self) -> None:
        '''Missing, empty, or invalid target output name must raise ValueError.'''
        with self.assertRaises(ValueError):
            batch_append(['tab1', 'tab2'], out_o='', cmd=self.cmd)
        with self.assertRaises(ValueError):
            batch_append(['tab1', 'tab2'], out_o=None, cmd=self.cmd)  # type: ignore
        with self.assertRaises(ValueError):
            batch_append(['tab1', 'tab2'], out_o=123, cmd=self.cmd)  # type: ignore
        with self.assertRaises(ValueError):
            batch_append(['tab1', 'tab2'], out_o=r'C:\path\out', cmd=self.cmd)

    def test_invalid_flag_parameters_raise_value_error(self) -> None:
        '''Invalid flag column name or mapping dictionary must raise ValueError.'''
        with self.assertRaises(ValueError):
            batch_append(['t1', 't2'], out_o='out', flag_f=123, cmd=self.cmd)  # type: ignore
        with self.assertRaises(ValueError):
            batch_append(['t1', 't2'], out_o='out', flag_f='  ', cmd=self.cmd)
        with self.assertRaises(ValueError):
            batch_append(['t1', 't2'], out_o='out', flag_f='SRC', flag_map='not_a_dict', cmd=self.cmd)  # type: ignore

    def test_invalid_sort_keys_raise_value_error(self) -> None:
        '''Invalid sort keys must raise ValueError.'''
        with self.assertRaises(ValueError):
            batch_append(['t1', 't2'], out_o='out', sort_keys_f=123, cmd=self.cmd)  # type: ignore
        with self.assertRaises(ValueError):
            batch_append(['t1', 't2'], out_o='out', sort_keys_f=['BHID', 456], cmd=self.cmd)  # type: ignore


class TestBatchAppendSingleTable(unittest.TestCase):
    '''Seam 2: Single Table Pass-through and Tagging.'''

    def setUp(self) -> None:
        self.cmd = MockCommandEngine()

    def test_single_table_without_flag_or_sort_copies(self) -> None:
        '''Single table with no flag and no sort performs a direct copy.'''
        result = batch_append(['tab1'], out_o='out_tab', cmd=self.cmd)
        self.assertEqual(result, 'out_tab')
        self.assertEqual(len(self.cmd.calls), 1)
        action, kwargs = self.cmd.calls[0]
        self.assertEqual(action, 'copy')
        self.assertEqual(kwargs['in_i'], 'tab1')
        self.assertEqual(kwargs['out_o'], 'out_tab')

    def test_single_table_with_flag_tags_records(self) -> None:
        '''Single table with flag tags records via EXTRA directly to output.'''
        result = batch_append(['tab1'], out_o='out_tab', flag_f='SRC', cmd=self.cmd)
        self.assertEqual(result, 'out_tab')
        self.assertEqual(len(self.cmd.calls), 1)
        action, kwargs = self.cmd.calls[0]
        self.assertEqual(action, 'extra')
        self.assertEqual(kwargs['in_i'], 'tab1')
        self.assertEqual(kwargs['out_o'], 'out_tab')
        self.assertIn('SRC', kwargs['arguments'])
        self.assertIn('"tab1"', kwargs['arguments'])

    def test_single_table_with_sort_keys_sorts(self) -> None:
        '''Single table with sort keys calls mgsort directly.'''
        result = batch_append(['tab1'], out_o='out_tab', sort_keys_f=['BHID'], cmd=self.cmd)
        self.assertEqual(result, 'out_tab')
        self.assertEqual(len(self.cmd.calls), 1)
        action, kwargs = self.cmd.calls[0]
        self.assertEqual(action, 'mgsort')
        self.assertEqual(kwargs['in_i'], 'tab1')
        self.assertEqual(kwargs['out_o'], 'out_tab')
        self.assertEqual(kwargs['keys_f'], ['BHID'])

    def test_single_table_with_flag_and_sort_cleans_scratch(self) -> None:
        '''Single table with flag and sort tags to scratch, sorts to out, and cleans scratch.'''
        result = batch_append(['tab1'], out_o='out_tab', flag_f='SRC', sort_keys_f=['BHID'], cmd=self.cmd)
        self.assertEqual(result, 'out_tab')
        actions = [call[0] for call in self.cmd.calls]
        self.assertIn('extra', actions)
        self.assertIn('mgsort', actions)
        self.assertIn('delete', actions)


class TestBatchAppendMultiTable(unittest.TestCase):
    '''Seam 3: Multi-Table Sequential Append Chaining with Managed Scratch Tables.'''

    def setUp(self) -> None:
        self.cmd = MockCommandEngine()

    def test_two_tables_appends_directly_to_output(self) -> None:
        '''Two tables without sort or flags append directly to output table.'''
        result = batch_append(['tab1', 'tab2'], out_o='combined', cmd=self.cmd)
        self.assertEqual(result, 'combined')
        self.assertEqual(len(self.cmd.calls), 1)
        action, kwargs = self.cmd.calls[0]
        self.assertEqual(action, 'append')
        self.assertEqual(kwargs['in1_i'], 'tab1')
        self.assertEqual(kwargs['in2_i'], 'tab2')
        self.assertEqual(kwargs['out_o'], 'combined')

    def test_three_tables_uses_managed_scratch_chaining(self) -> None:
        '''Three tables uses scratch table for step 1, then appends step 2 to output and cleans scratch.'''
        result = batch_append(['tab1', 'tab2', 'tab3'], out_o='combined', cmd=self.cmd)
        self.assertEqual(result, 'combined')

        append_calls = [call for call in self.cmd.calls if call[0] == 'append']
        self.assertEqual(len(append_calls), 2)

        # First append produces an in-memory scratch table
        first_out = append_calls[0][1]['out_o']
        self.assertTrue(first_out.startswith('_'), f"Intermediate table '{first_out}' must start with '_'")
        self.assertEqual(append_calls[0][1]['in1_i'], 'tab1')
        self.assertEqual(append_calls[0][1]['in2_i'], 'tab2')

        # Second append merges scratch table with third input to final output
        self.assertEqual(append_calls[1][1]['in1_i'], first_out)
        self.assertEqual(append_calls[1][1]['in2_i'], 'tab3')
        self.assertEqual(append_calls[1][1]['out_o'], 'combined')

        # Intermediate scratch table must be cleaned up
        deleted_tables = [call[1]['in_i'] for call in self.cmd.calls if call[0] == 'delete']
        self.assertIn(first_out, deleted_tables)
        self.assertNotIn('combined', deleted_tables)

    def test_many_tables_chaining(self) -> None:
        '''Chains 5 tables sequentially through managed scratch tables without disk pollution.'''
        tables = ['t1', 't2', 't3', 't4', 't5']
        result = batch_append(tables, out_o='combined', cmd=self.cmd)
        self.assertEqual(result, 'combined')

        append_calls = [call for call in self.cmd.calls if call[0] == 'append']
        self.assertEqual(len(append_calls), 4)

        deleted_tables = [call[1]['in_i'] for call in self.cmd.calls if call[0] == 'delete']
        # 3 intermediate scratch tables should be deleted
        self.assertEqual(len(deleted_tables), 3)
        self.assertNotIn('combined', deleted_tables)
        for t in tables:
            self.assertNotIn(t, deleted_tables)


class TestBatchAppendProvenanceFlagging(unittest.TestCase):
    '''Seam 4: Provenance Metadata Flagging.'''

    def setUp(self) -> None:
        self.cmd = MockCommandEngine()

    def test_flag_defaults_to_source_table_names(self) -> None:
        '''When flag_f is set without flag_map, tags each table with its own name.'''
        batch_append(['north_collars', 'south_collars'], out_o='all_collars', flag_f='SOURCE', cmd=self.cmd)

        extra_calls = [call for call in self.cmd.calls if call[0] == 'extra']
        self.assertEqual(len(extra_calls), 2)

        args0 = extra_calls[0][1]['arguments']
        args1 = extra_calls[1][1]['arguments']

        self.assertIn('SOURCE', args0)
        self.assertIn('"north_collars"', args0)
        self.assertIn('SOURCE', args1)
        self.assertIn('"south_collars"', args1)

    def test_flag_custom_mapping_string(self) -> None:
        '''Custom flag mapping dictionary assigns mapped string values.'''
        mapping = {'t1': 'ZONE_A', 't2': 'ZONE_B'}
        batch_append(['t1', 't2'], out_o='out', flag_f='ZONE', flag_map=mapping, cmd=self.cmd)

        extra_calls = [call for call in self.cmd.calls if call[0] == 'extra']
        self.assertEqual(len(extra_calls), 2)
        self.assertIn('"ZONE_A"', extra_calls[0][1]['arguments'])
        self.assertIn('"ZONE_B"', extra_calls[1][1]['arguments'])

    def test_flag_custom_mapping_numeric(self) -> None:
        '''Numeric flag values are declared with ;N.'''
        mapping = {'t1': 101, 't2': 202}
        batch_append(['t1', 't2'], out_o='out', flag_f='SECTOR', flag_map=mapping, cmd=self.cmd)

        extra_calls = [call for call in self.cmd.calls if call[0] == 'extra']
        self.assertEqual(len(extra_calls), 2)
        self.assertIn('SECTOR;N = 101', extra_calls[0][1]['arguments'])
        self.assertIn('SECTOR;N = 202', extra_calls[1][1]['arguments'])


class TestBatchAppendSorting(unittest.TestCase):
    '''Seam 5: Output Key Sorting via mgsort.'''

    def setUp(self) -> None:
        self.cmd = MockCommandEngine()

    def test_multi_table_sort_executes_mgsort(self) -> None:
        '''When sort_keys_f is specified, output table is sorted via mgsort.'''
        batch_append(['t1', 't2'], out_o='sorted_out', sort_keys_f=['BHID', 'FROM'], cmd=self.cmd)

        sort_calls = [call for call in self.cmd.calls if call[0] == 'mgsort']
        self.assertEqual(len(sort_calls), 1)
        self.assertEqual(sort_calls[0][1]['out_o'], 'sorted_out')
        self.assertEqual(sort_calls[0][1]['keys_f'], ['BHID', 'FROM'])

    def test_single_string_sort_key_normalized(self) -> None:
        '''Single string sort key is normalized to list.'''
        batch_append(['t1', 't2'], out_o='sorted_out', sort_keys_f='BHID', cmd=self.cmd)

        sort_calls = [call for call in self.cmd.calls if call[0] == 'mgsort']
        self.assertEqual(len(sort_calls), 1)
        self.assertEqual(sort_calls[0][1]['keys_f'], ['BHID'])


class TestBatchAppendReExports(unittest.TestCase):
    '''Seam 6: Module Re-exports and Backwards Compatibility.'''

    def test_reexported_at_root_and_agent(self) -> None:
        '''batch_append is accessible via canonical and compat modules.'''
        self.assertIs(root_batch_append, batch_append)
        self.assertIs(agent_batch_append, batch_append)


if __name__ == '__main__':
    unittest.main()
