'''
tests/test_sequential_keys.py
------------------------------

Unit tests verifying:
1. Dual-mode parameter resolution with singular aliases (keys_f, key1_f, and key_f)
2. JOIN command wrapper keyfields parameter support
3. ACCMLT command wrapper singular key_f alias support
'''

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dmstudio import command_registry, dmcommands
from tests import generate_wrappers


class DummyScript:
    def __init__(self):
        self.commands = []

    def Parsecommand(self, cmd):
        self.commands.append(cmd)


class TestSequentialKeys(unittest.TestCase):
    def setUp(self):
        self.engine = dmcommands.init.__new__(dmcommands.init)
        self.engine.oScript = DummyScript()
        self.engine.strict = False

    def test_resolve_canonical_list(self):
        kwargs = {}
        res = self.engine._resolve_sequential_param('keys_f', 'key', ['BHID', 'FROM'], 30, 'f', kwargs)
        self.assertEqual(res, ['BHID', 'FROM'])
        self.assertEqual(kwargs, {})

    def test_resolve_numbered_kwargs(self):
        kwargs = {'key1_f': 'BHID', 'key2_f': 'FROM'}
        res = self.engine._resolve_sequential_param('keys_f', 'key', ['optional'], 30, 'f', kwargs)
        self.assertEqual(res, ['BHID', 'FROM'])
        self.assertEqual(kwargs, {})

    def test_resolve_singular_alias_string(self):
        kwargs = {'key_f': 'BHID'}
        res = self.engine._resolve_sequential_param('keys_f', 'key', ['optional'], 30, 'f', kwargs)
        self.assertEqual(res, ['BHID'])
        self.assertEqual(kwargs, {})

    def test_resolve_singular_alias_list(self):
        kwargs = {'key_f': ['BHID', 'FROM']}
        res = self.engine._resolve_sequential_param('keys_f', 'key', ['optional'], 30, 'f', kwargs)
        self.assertEqual(res, ['BHID', 'FROM'])
        self.assertEqual(kwargs, {})

    def test_resolve_conflict_canonical_and_singular(self):
        kwargs = {'key_f': 'BHID'}
        with self.assertRaises(ValueError) as ctx:
            self.engine._resolve_sequential_param('keys_f', 'key', ['ZONE'], 30, 'f', kwargs)
        self.assertIn('Cannot specify both', str(ctx.exception))

    def test_resolve_conflict_numbered_and_singular(self):
        kwargs = {'key1_f': 'BHID', 'key_f': 'ZONE'}
        with self.assertRaises(ValueError) as ctx:
            self.engine._resolve_sequential_param('keys_f', 'key', ['optional'], 30, 'f', kwargs)
        self.assertIn('Cannot specify both', str(ctx.exception))

    def test_resolve_gap_detection(self):
        kwargs = {'key1_f': 'BHID', 'key3_f': 'ZONE'}
        with self.assertRaises(ValueError) as ctx:
            self.engine._resolve_sequential_param('keys_f', 'key', ['optional'], 30, 'f', kwargs)
        self.assertIn('Gap detected', str(ctx.exception))

    def test_join_with_canonical_keys_f(self):
        self.engine.join(out_o='out_tab', inmods_i=['tab1', 'tab2'], keys_f=['BHID'])
        self.assertTrue(len(self.engine.oScript.commands) > 0)
        last_cmd = self.engine.oScript.commands[-1]
        self.assertIn('&out=out_tab', last_cmd)
        self.assertIn('&in1=tab1', last_cmd)
        self.assertIn('&in2=tab2', last_cmd)
        self.assertIn('*key1=BHID', last_cmd)

    def test_join_with_singular_key_f(self):
        self.engine.join(out_o='out_tab', inmods_i=['tab1', 'tab2'], key_f='BHID')
        last_cmd = self.engine.oScript.commands[-1]
        self.assertIn('*key1=BHID', last_cmd)

    def test_join_with_numbered_key1_f(self):
        self.engine.join(out_o='out_tab', inmods_i=['tab1', 'tab2'], key1_f='BHID', key2_f='FROM')
        last_cmd = self.engine.oScript.commands[-1]
        self.assertIn('*key1=BHID', last_cmd)
        self.assertIn('*key2=FROM', last_cmd)

    def test_accmlt_with_singular_key_f(self):
        self.engine.accmlt(in_i='tab1', out_o='out_tab', key_f='BHID')
        last_cmd = self.engine.oScript.commands[-1]
        self.assertIn('&in=tab1', last_cmd)
        self.assertIn('&out=out_tab', last_cmd)
        self.assertIn('*key1=BHID', last_cmd)

    def test_join_schema(self):
        schema = command_registry.get_command_schema('join')
        param_names = [p['name'] for p in schema['parameters']]
        self.assertIn('keys_f', param_names)
        self.assertIn('inmods_i', param_names)
        self.assertIn('out_o', param_names)

    def test_generator_join_parsing(self):
        join_md = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'datamine_help', 'StudioRM', 'Process_Help_XML', 'join.md'
        )
        if os.path.exists(join_md):
            info = generate_wrappers.parse_markdown_file(join_md)
            self.assertEqual(len(info['fields']), 30)
            self.assertEqual(info['fields'][0]['name'], 'KEY1')
            self.assertEqual(info['fields'][-1]['name'], 'KEY30')


if __name__ == '__main__':
    unittest.main()
