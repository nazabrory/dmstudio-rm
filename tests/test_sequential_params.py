'''
Unit tests for sequential and dual-mode parameter resolution in dmcommands.
Does not require an active Datamine Studio RM session.
'''

import os
import sys
import unittest
from unittest.mock import MagicMock

# Add project root to sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dmstudio import dmcommands


class TestSequentialParams(unittest.TestCase):

    def setUp(self):
        # Create an uninitialized instance and attach a mock oScript
        self.cmd = dmcommands.init.__new__(dmcommands.init)
        self.mock_script = MagicMock()
        self.cmd.oScript = self.mock_script

    def test_selcop_with_canonical_list(self):
        '''Verify selcop accepts canonical fields_f list parameter.'''
        self.cmd.selcop(in_i='in_file', out_o='out_file', fields_f=['BHID', 'FROM', 'TO'])
        self.mock_script.Parsecommand.assert_called_once()
        cli_cmd = self.mock_script.Parsecommand.call_args[0][0]
        self.assertIn('&in=in_file', cli_cmd)
        self.assertIn('&out=out_file', cli_cmd)
        self.assertIn('*f1=BHID', cli_cmd)
        self.assertIn('*f2=FROM', cli_cmd)
        self.assertIn('*f3=TO', cli_cmd)
        self.assertNotIn('*f2-f25', cli_cmd)

    def test_selcop_with_individual_kwargs(self):
        '''Verify selcop accepts individual numbered arguments (f1_f, f2_f, f3_f).'''
        self.cmd.selcop(in_i='in_file', out_o='out_file', f1_f='BHID', f2_f='FROM', f3_f='TO')
        self.mock_script.Parsecommand.assert_called_once()
        cli_cmd = self.mock_script.Parsecommand.call_args[0][0]
        self.assertIn('&in=in_file', cli_cmd)
        self.assertIn('&out=out_file', cli_cmd)
        self.assertIn('*f1=BHID', cli_cmd)
        self.assertIn('*f2=FROM', cli_cmd)
        self.assertIn('*f3=TO', cli_cmd)
        self.assertNotIn('*f2-f25', cli_cmd)

    def test_selcop_gap_raises_error(self):
        '''Verify that gaps in numbered arguments (f1_f and f3_f without f2_f) raise ValueError.'''
        with self.assertRaises(ValueError) as ctx:
            self.cmd.selcop(in_i='in_file', out_o='out_file', f1_f='BHID', f3_f='TO')
        self.assertIn('Gap', str(ctx.exception))

    def test_selcop_conflict_raises_error(self):
        '''Verify that passing both canonical list and individual kwargs raises ValueError.'''
        with self.assertRaises(ValueError) as ctx:
            self.cmd.selcop(in_i='in_file', out_o='out_file', fields_f=['BHID'], f1_f='BHID')
        self.assertIn('both', str(ctx.exception).lower())

    def test_selcop_empty_list_conflict_raises_error(self):
        '''Verify that passing empty list and individual kwargs also raises ValueError.'''
        with self.assertRaises(ValueError) as ctx:
            self.cmd.selcop(in_i='in_file', out_o='out_file', fields_f=[], f1_f='BHID')
        self.assertIn('both', str(ctx.exception).lower())

    def test_selcop_unknown_kwarg_raises_error(self):
        '''Verify that unrecognized kwargs raise TypeError to preserve typo safety.'''
        with self.assertRaises(TypeError) as ctx:
            self.cmd.selcop(in_i='in_file', out_o='out_file', non_existent_kwarg='bad')
        self.assertIn('unexpected keyword argument', str(ctx.exception).lower())

    def test_mgsort_dual_mode_kwargs(self):
        '''Verify other sequential commands (like mgsort) also support dual-mode individual kwargs.'''
        self.cmd.mgsort(in_i='in_file', out_o='out_file', key1_f='BHID', key2_f='FROM')
        self.mock_script.Parsecommand.assert_called_once()
        cli_cmd = self.mock_script.Parsecommand.call_args[0][0]
        self.assertIn('&in=in_file', cli_cmd)
        self.assertIn('&out=out_file', cli_cmd)
        self.assertIn('*key1=BHID', cli_cmd)
        self.assertIn('*key2=FROM', cli_cmd)

    def test_selcop_ptvi_mri_22_fields_scenario(self):
        '''Verify exact 22-field call from PTVI_MRI_compositing.ipynb succeeds.'''
        self.cmd.selcop(
            in_i='holesfcomp1',
            out_o='_temp1',
            f1_f='BHID', f2_f='FROM', f3_f='TO', f4_f='LYR',
            f5_f='NI1', f6_f='CO1', f7_f='FE1', f8_f='SIO21',
            f9_f='MGO1', f10_f='CR1', f11_f='AL1', f12_f='MN1',
            f13_f='CA1', f14_f='H2O1', f15_f='WTF', f16_f='DTF',
            f17_f='REC1', f18_f='DW1', f19_f='LENGTH',
            f20_f='mid_x', f21_f='mid_y', f22_f='mid_z'
        )
        self.mock_script.Parsecommand.assert_called_once()
        cli_cmd = self.mock_script.Parsecommand.call_args[0][0]
        self.assertIn('*f1=BHID', cli_cmd)
        self.assertIn('*f22=mid_z', cli_cmd)

    def test_selcop_exceeds_max_fields_raises_error(self):
        '''Verify that supplying more than 25 fields for selcop raises ValueError.'''
        kwargs = {f'f{i}_f': f'FIELD_{i}' for i in range(1, 27)}
        with self.assertRaises(ValueError) as ctx:
            self.cmd.selcop(in_i='in_file', out_o='out_file', **kwargs)
        self.assertIn('Maximum allowed fields', str(ctx.exception))

    def test_duplicate_index_raises_error(self):
        '''Verify providing duplicate keys for the same index (e.g. f1 and f1_f) raises ValueError.'''
        with self.assertRaises(ValueError) as ctx:
            self.cmd.selcop(in_i='in_file', out_o='out_file', f1_f='BHID', f1='BHID2', f2_f='FROM')
        self.assertIn('Duplicate sequential argument', str(ctx.exception))

    def test_case_insensitive_kwargs(self):
        '''Verify kwargs are case-insensitive (e.g. F1_F or F2).'''
        self.cmd.selcop(in_i='in_file', out_o='out_file', F1_F='BHID', F2_F='FROM')
        self.mock_script.Parsecommand.assert_called_once()
        cli_cmd = self.mock_script.Parsecommand.call_args[0][0]
        self.assertIn('*f1=BHID', cli_cmd)
        self.assertIn('*f2=FROM', cli_cmd)

    def test_other_expanded_commands(self):
        '''Verify factor and modtra also support fields_f properly now.'''
        self.cmd.modtra(model_i='model', grid_i='grid', out_o='out', fields_f=['GRADE', 'DENSITY'])
        self.mock_script.Parsecommand.assert_called_once()
        cli_cmd = self.mock_script.Parsecommand.call_args[0][0]
        self.assertIn('*f1=GRADE', cli_cmd)
        self.assertIn('*f2=DENSITY', cli_cmd)


if __name__ == '__main__':
    unittest.main()
