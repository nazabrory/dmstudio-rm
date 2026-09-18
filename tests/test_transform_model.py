'''
tests/test_transform_model.py
-----------------------------

Unit tests for the block model coordinate transformation superprocess.
Verifies input parameter validation, prototype generation via PROTOM,
block model transformation via COPYMOD, cell position recalculation via EXTRA,
managed scratch table lifecycle, and backwards-compatibility re-exports.
Runs offline without requiring an active Datamine Studio RM session or license.
'''

import unittest
from typing import Any, Dict, List, Tuple

from dmstudio.superprocess import transform_model


class MockCommandEngine:
    '''Mock Studio RM command engine recording all executed commands.'''

    def __init__(self) -> None:
        self.calls: List[Tuple[str, Dict[str, Any]]] = []

    def copy(self, in_i: str, out_o: str, **kwargs: Any) -> None:
        self.calls.append(('copy', {'in_i': in_i, 'out_o': out_o, **kwargs}))

    def extra(self, in_i: str, out_o: str, arguments: str = 'optional', **kwargs: Any) -> None:
        self.calls.append(('extra', {'in_i': in_i, 'out_o': out_o, 'arguments': arguments, **kwargs}))

    def copymod(
        self,
        modelin_i: str = 'required',
        modelout_o: str = 'required',
        xworld_f: str = 'optional',
        yworld_f: str = 'optional',
        zworld_f: str = 'optional',
        modtype_p: Any = 'optional',
        arguments: str = 'optional',
        **kwargs: Any,
    ) -> None:
        self.calls.append((
            'copymod',
            {
                'modelin_i': modelin_i,
                'modelout_o': modelout_o,
                'xworld_f': xworld_f,
                'yworld_f': yworld_f,
                'zworld_f': zworld_f,
                'modtype_p': modtype_p,
                'arguments': arguments,
                **kwargs,
            },
        ))

    def protom(self, out_o: str = 'required', rotmod_p: Any = '0', arguments: str = 'optional', **kwargs: Any) -> None:
        self.calls.append(('protom', {'out_o': out_o, 'rotmod_p': rotmod_p, 'arguments': arguments, **kwargs}))

    def delete(self, in_i: str = None, confirm_p: int = 0, **kwargs: Any) -> None:
        self.calls.append(('delete', {'in_i': in_i, 'confirm_p': confirm_p, **kwargs}))


class TestTransformModelValidation(unittest.TestCase):
    '''Seam 1: Input Validation and Parameter Normalization.'''

    def setUp(self) -> None:
        self.cmd = MockCommandEngine()

    def test_missing_model_i_raises_value_error(self) -> None:
        '''Missing or empty model_i must raise descriptive ValueError.'''
        with self.assertRaises(ValueError) as ctx:
            transform_model(model_i='', out_o='out_m', dx_p=100.0, dy_p=200.0, cmd=self.cmd)
        self.assertIn('model_i', str(ctx.exception).lower())

        with self.assertRaises(ValueError) as ctx:
            transform_model(model_i=None, out_o='out_m', dx_p=100.0, dy_p=200.0, cmd=self.cmd)  # type: ignore
        self.assertIn('model_i', str(ctx.exception).lower())

    def test_missing_out_o_raises_value_error(self) -> None:
        '''Missing or empty out_o must raise descriptive ValueError.'''
        with self.assertRaises(ValueError) as ctx:
            transform_model(model_i='in_m', out_o='', dx_p=100.0, dy_p=200.0, cmd=self.cmd)
        self.assertIn('out_o', str(ctx.exception).lower())

        with self.assertRaises(ValueError) as ctx:
            transform_model(model_i='in_m', out_o=None, dx_p=100.0, dy_p=200.0, cmd=self.cmd)  # type: ignore
        self.assertIn('out_o', str(ctx.exception).lower())

    def test_backslashes_in_table_names_raise_value_error(self) -> None:
        '''Backslashes in input or output table names must raise ValueError.'''
        with self.assertRaises(ValueError) as ctx:
            transform_model(model_i=r'C:\Data\model', out_o='out_m', dx_p=100.0, dy_p=200.0, cmd=self.cmd)
        self.assertIn('backslash', str(ctx.exception).lower())

        with self.assertRaises(ValueError) as ctx:
            transform_model(model_i='in_m', out_o=r'C:\Data\out', dx_p=100.0, dy_p=200.0, cmd=self.cmd)
        self.assertIn('backslash', str(ctx.exception).lower())

    def test_spaces_in_table_names_raise_value_error(self) -> None:
        '''Spaces in table names break Datamine parser and must raise ValueError.'''
        with self.assertRaises(ValueError) as ctx:
            transform_model(model_i='my model', out_o='out_m', dx_p=100.0, dy_p=200.0, cmd=self.cmd)
        self.assertIn('space', str(ctx.exception).lower())

        with self.assertRaises(ValueError) as ctx:
            transform_model(model_i='in_m', out_o='my out', dx_p=100.0, dy_p=200.0, cmd=self.cmd)
        self.assertIn('space', str(ctx.exception).lower())

    def test_missing_or_invalid_offsets_raise_value_error(self) -> None:
        '''Offsets dx_p and dy_p are required and must be numeric (not None, string, or boolean).'''
        with self.assertRaises(ValueError) as ctx:
            transform_model(model_i='in_m', out_o='out_m', dx_p=None, dy_p=200.0, cmd=self.cmd)  # type: ignore
        self.assertIn('dx_p', str(ctx.exception).lower())

        with self.assertRaises(ValueError) as ctx:
            transform_model(model_i='in_m', out_o='out_m', dx_p='invalid', dy_p=200.0, cmd=self.cmd)  # type: ignore
        self.assertIn('dx_p', str(ctx.exception).lower())

        with self.assertRaises(ValueError) as ctx:
            transform_model(model_i='in_m', out_o='out_m', dx_p=100.0, dy_p='invalid', cmd=self.cmd)  # type: ignore
        self.assertIn('dy_p', str(ctx.exception).lower())

        # Booleans must not be accepted as numbers
        with self.assertRaises(ValueError) as ctx:
            transform_model(model_i='in_m', out_o='out_m', dx_p=True, dy_p=200.0, cmd=self.cmd)  # type: ignore
        self.assertIn('dx_p', str(ctx.exception).lower())

        with self.assertRaises(ValueError) as ctx:
            transform_model(model_i='in_m', out_o='out_m', dx_p=100.0, dy_p=200.0, dz_p=False, cmd=self.cmd)  # type: ignore
        self.assertIn('dz_p', str(ctx.exception).lower())

    def test_invalid_rotation_angle_raises_value_error(self) -> None:
        '''Rotation angle must be a valid number between -360 and 360 degrees.'''
        with self.assertRaises(ValueError) as ctx:
            transform_model(model_i='in_m', out_o='out_m', dx_p=100.0, dy_p=200.0, angle_p='30deg', cmd=self.cmd)  # type: ignore
        self.assertIn('angle', str(ctx.exception).lower())

        with self.assertRaises(ValueError) as ctx:
            transform_model(model_i='in_m', out_o='out_m', dx_p=100.0, dy_p=200.0, angle_p=400.0, cmd=self.cmd)
        self.assertIn('angle', str(ctx.exception).lower())

        with self.assertRaises(ValueError) as ctx:
            transform_model(model_i='in_m', out_o='out_m', dx_p=100.0, dy_p=200.0, angle_p=-450.0, cmd=self.cmd)
        self.assertIn('angle', str(ctx.exception).lower())

    def test_invalid_rotation_axis_raises_value_error(self) -> None:
        '''Rotation axis must be in {0, 1, 2, 3}.'''
        with self.assertRaises(ValueError) as ctx:
            transform_model(model_i='in_m', out_o='out_m', dx_p=100.0, dy_p=200.0, angle_p=30.0, axis_p=5, cmd=self.cmd)
        self.assertIn('axis', str(ctx.exception).lower())


class TestTransformModelProtom(unittest.TestCase):
    '''Seam 2: Prototype Transformation & Origin Recalculation via PROTOM.'''

    def setUp(self) -> None:
        self.cmd = MockCommandEngine()

    def test_prototype_orthogonal_transformation_calls_protom(self) -> None:
        '''Orthogonal prototype transformation recalculates origin and invokes PROTOM.'''
        result = transform_model(
            model_i='proto_in',
            out_o='proto_out',
            dx_p=100.0,
            dy_p=200.0,
            dz_p=50.0,
            angle_p=0.0,
            x_orig_p=5900.0,
            y_orig_p=4800.0,
            z_orig_p=-100.0,
            xinc_p=10.0,
            yinc_p=15.0,
            zinc_p=20.0,
            nx_p=25,
            ny_p=30,
            nz_p=35,
            is_prototype=True,
            cmd=self.cmd,
        )
        self.assertEqual(result, 'proto_out')

        protom_calls = [c for c in self.cmd.calls if c[0] == 'protom']
        self.assertEqual(len(protom_calls), 1)
        action, kwargs = protom_calls[0]
        self.assertEqual(kwargs['rotmod_p'], 0)
        # Check scratch table output
        scratch_out = kwargs['out_o']
        self.assertTrue(scratch_out.startswith('_'), f"Intermediate prototype {scratch_out} must start with '_'")

        args = kwargs['arguments']
        # Recalculated origin: 5900+100=6000, 4800+200=5000, -100+50=-50
        self.assertIn("'6000.0'", args)
        self.assertIn("'5000.0'", args)
        self.assertIn("'-50.0'", args)
        # Dimensions and counts
        self.assertIn("'10.0'", args)
        self.assertIn("'15.0'", args)
        self.assertIn("'20.0'", args)
        self.assertIn("'25'", args)
        self.assertIn("'30'", args)
        self.assertIn("'35'", args)

        # Copied to target out_o
        copy_calls = [c for c in self.cmd.calls if c[0] == 'copy']
        self.assertEqual(len(copy_calls), 1)
        self.assertEqual(copy_calls[0][1]['in_i'], scratch_out)
        self.assertEqual(copy_calls[0][1]['out_o'], 'proto_out')

        # Cleaned scratch table
        delete_calls = [c for c in self.cmd.calls if c[0] == 'delete']
        deleted = [c[1]['in_i'] for c in delete_calls]
        self.assertIn(scratch_out, deleted)
        self.assertNotIn('proto_out', deleted)

    def test_prototype_rotated_transformation_calls_protom(self) -> None:
        '''Rotated prototype sets rotmod=1 and passes rotation angles/axes to PROTOM.'''
        result = transform_model(
            model_i='proto_in',
            out_o='proto_out',
            dx_p=50.0,
            dy_p=75.0,
            dz_p=0.0,
            angle_p=35.0,
            axis_p=3,
            x_orig_p=1000.0,
            y_orig_p=2000.0,
            z_orig_p=300.0,
            is_prototype=True,
            cmd=self.cmd,
        )
        self.assertEqual(result, 'proto_out')

        protom_calls = [c for c in self.cmd.calls if c[0] == 'protom']
        self.assertEqual(len(protom_calls), 1)
        action, kwargs = protom_calls[0]
        self.assertEqual(kwargs['rotmod_p'], 1)
        args = kwargs['arguments']
        self.assertIn("'1050.0'", args)
        self.assertIn("'2075.0'", args)
        self.assertIn("'300.0'", args)
        self.assertIn("'35.0'", args)
        self.assertIn("'3'", args)


class TestTransformModelCopymod(unittest.TestCase):
    '''Seam 3: Block Model Transformation via COPYMOD.'''

    def setUp(self) -> None:
        self.cmd = MockCommandEngine()

    def test_model_translation_only_calls_copymod_modtype1(self) -> None:
        '''Model translation without rotation calls COPYMOD with modtype=1.'''
        result = transform_model(
            model_i='bm_in',
            out_o='bm_out',
            dx_p=150.0,
            dy_p=-250.0,
            dz_p=20.0,
            angle_p=0.0,
            x_orig_p=1000.0,
            y_orig_p=2000.0,
            z_orig_p=100.0,
            is_prototype=False,
            cmd=self.cmd,
        )
        self.assertEqual(result, 'bm_out')

        copymod_calls = [c for c in self.cmd.calls if c[0] == 'copymod']
        self.assertEqual(len(copymod_calls), 1)
        action, kwargs = copymod_calls[0]
        self.assertEqual(kwargs['modelin_i'], 'bm_in')
        self.assertEqual(kwargs['modtype_p'], 1)

        scratch_out = kwargs['modelout_o']
        self.assertTrue(scratch_out.startswith('_'), f"Intermediate output {scratch_out} must start with '_'")

        args = kwargs['arguments']
        # 1000+150=1150, 2000-250=1750, 100+20=120
        self.assertIn('@xneworig=1150.0', args)
        self.assertIn('@yneworig=1750.0', args)
        self.assertIn('@zneworig=120.0', args)
        self.assertNotIn('@angle1', args)

        # Copied to output
        copy_calls = [c for c in self.cmd.calls if c[0] == 'copy']
        self.assertEqual(len(copy_calls), 1)
        self.assertEqual(copy_calls[0][1]['in_i'], scratch_out)
        self.assertEqual(copy_calls[0][1]['out_o'], 'bm_out')

        # Cleaned scratch
        delete_calls = [c for c in self.cmd.calls if c[0] == 'delete']
        deleted = [c[1]['in_i'] for c in delete_calls]
        self.assertIn(scratch_out, deleted)
        self.assertNotIn('bm_out', deleted)

    def test_model_translation_and_rotation_calls_copymod_modtype2(self) -> None:
        '''Model translation with rotation calls COPYMOD with modtype=2 and rotation angles.'''
        result = transform_model(
            model_i='bm_in',
            out_o='bm_out',
            dx_p=100.0,
            dy_p=200.0,
            dz_p=0.0,
            angle_p=45.0,
            axis_p=3,
            x_orig_p=500.0,
            y_orig_p=600.0,
            z_orig_p=100.0,
            is_prototype=False,
            cmd=self.cmd,
        )
        self.assertEqual(result, 'bm_out')

        copymod_calls = [c for c in self.cmd.calls if c[0] == 'copymod']
        self.assertEqual(len(copymod_calls), 1)
        action, kwargs = copymod_calls[0]
        self.assertEqual(kwargs['modtype_p'], 2)

        args = kwargs['arguments']
        self.assertIn('@xneworig=600.0', args)
        self.assertIn('@yneworig=800.0', args)
        self.assertIn('@zneworig=100.0', args)
        self.assertIn('@angle1=45.0', args)
        self.assertIn('@axis1=3', args)

    def test_model_with_world_coordinates_fields(self) -> None:
        '''When world coordinate fields are specified, they are passed to COPYMOD.'''
        transform_model(
            model_i='bm_in',
            out_o='bm_out',
            dx_p=100.0,
            dy_p=200.0,
            angle_p=30.0,
            xworld_f='XWORLD',
            yworld_f='YWORLD',
            zworld_f='ZWORLD',
            is_prototype=False,
            cmd=self.cmd,
        )

        copymod_calls = [c for c in self.cmd.calls if c[0] == 'copymod']
        self.assertEqual(len(copymod_calls), 1)
        action, kwargs = copymod_calls[0]
        self.assertEqual(kwargs['xworld_f'], 'XWORLD')
        self.assertEqual(kwargs['yworld_f'], 'YWORLD')
        self.assertEqual(kwargs['zworld_f'], 'ZWORLD')


class TestTransformModelExtra(unittest.TestCase):
    '''Seam 4: Cell Coordinate Shifting and Attribute Calculation via EXTRA.'''

    def setUp(self) -> None:
        self.cmd = MockCommandEngine()

    def test_model_with_adjust_cells_invokes_extra(self) -> None:
        '''When adjust_cells=True, EXTRA is chained to update cell centroid coordinates.'''
        result = transform_model(
            model_i='bm_in',
            out_o='bm_out',
            dx_p=25.0,
            dy_p=50.0,
            dz_p=-10.0,
            adjust_cells=True,
            is_prototype=False,
            cmd=self.cmd,
        )
        self.assertEqual(result, 'bm_out')

        copymod_calls = [c for c in self.cmd.calls if c[0] == 'copymod']
        extra_calls = [c for c in self.cmd.calls if c[0] == 'extra']
        self.assertEqual(len(copymod_calls), 1)
        self.assertEqual(len(extra_calls), 1)

        cm_scratch = copymod_calls[0][1]['modelout_o']
        extra_in = extra_calls[0][1]['in_i']
        extra_out = extra_calls[0][1]['out_o']
        self.assertEqual(extra_in, cm_scratch)
        self.assertTrue(extra_out.startswith('_'))

        args = extra_calls[0][1]['arguments']
        self.assertIn('XC = XC + 25.0', args)
        self.assertIn('YC = YC + 50.0', args)
        self.assertIn('ZC = ZC + -10.0', args)
        self.assertIn('GO', args)

        # Both scratch tables cleaned up
        delete_calls = [c for c in self.cmd.calls if c[0] == 'delete']
        deleted = [c[1]['in_i'] for c in delete_calls]
        self.assertIn(cm_scratch, deleted)
        self.assertIn(extra_out, deleted)
        self.assertNotIn('bm_out', deleted)

    def test_direct_extra_method(self) -> None:
        '''When method='extra', shifts cell positions directly without calling COPYMOD.'''
        result = transform_model(
            model_i='bm_in',
            out_o='bm_out',
            dx_p=30.0,
            dy_p=-40.0,
            dz_p=15.0,
            method='extra',
            cmd=self.cmd,
        )
        self.assertEqual(result, 'bm_out')

        copymod_calls = [c for c in self.cmd.calls if c[0] == 'copymod']
        extra_calls = [c for c in self.cmd.calls if c[0] == 'extra']
        self.assertEqual(len(copymod_calls), 0)
        self.assertEqual(len(extra_calls), 1)

        args = extra_calls[0][1]['arguments']
        self.assertIn('XC = XC + 30.0', args)
        self.assertIn('YC = YC + -40.0', args)
        self.assertIn('ZC = ZC + 15.0', args)


class TestTransformModelScratchLifecycle(unittest.TestCase):
    '''Seam 5: Managed Scratch Table Lifecycle and Cleanup.'''

    def setUp(self) -> None:
        self.cmd = MockCommandEngine()

    def test_scratch_cleanup_on_normal_execution(self) -> None:
        '''All intermediate scratch tables are tracked and cleaned up on successful execution.'''
        transform_model(
            model_i='bm_in',
            out_o='bm_final',
            dx_p=10.0,
            dy_p=20.0,
            adjust_cells=True,
            is_prototype=False,
            cmd=self.cmd,
        )

        deleted_tables = [c[1]['in_i'] for c in self.cmd.calls if c[0] == 'delete']
        self.assertGreaterEqual(len(deleted_tables), 2)
        for t in deleted_tables:
            self.assertTrue(t.startswith('_'), f"Deleted table '{t}' must be a scratch table starting with '_'")
            self.assertNotEqual(t, 'bm_final', "Final output table must never be deleted")
            self.assertNotEqual(t, 'bm_in', "Input table must never be deleted")

    def test_scratch_cleanup_on_exception(self) -> None:
        '''When an error occurs during execution, scratch context guarantees intermediate cleanup.'''
        class FailingCommandEngine(MockCommandEngine):
            def extra(self, in_i: str, out_o: str, arguments: str = 'optional', **kwargs: Any) -> None:
                super().extra(in_i, out_o, arguments, **kwargs)
                raise RuntimeError("Simulated COM parse failure inside extra")

        failing_cmd = FailingCommandEngine()
        with self.assertRaises(RuntimeError):
            transform_model(
                model_i='bm_in',
                out_o='bm_final',
                dx_p=10.0,
                dy_p=20.0,
                adjust_cells=True,
                is_prototype=False,
                cmd=failing_cmd,
            )

        deleted_tables = [c[1]['in_i'] for c in failing_cmd.calls if c[0] == 'delete']
        # The scratch table generated by copymod before extra failed should have been cleaned up
        self.assertGreaterEqual(len(deleted_tables), 1)
        for t in deleted_tables:
            self.assertTrue(t.startswith('_'))


class TestTransformModelReExports(unittest.TestCase):
    '''Seam 6: Module Re-exports and Backwards Compatibility.'''

    def test_reexported_at_root_and_agent(self) -> None:
        '''transform_model and aliases are accessible via canonical and compat modules.'''
        import dmstudio
        from dmstudio import agent
        from dmstudio.superprocess import (
            transform_model as canonical_transform,
            transform_block_model as canonical_alias,
            coordinate_transform as canonical_alias2,
        )

        self.assertIs(canonical_alias, canonical_transform)
        self.assertIs(canonical_alias2, canonical_transform)

        self.assertTrue(hasattr(dmstudio, 'transform_model'))
        self.assertIs(dmstudio.transform_model, canonical_transform)
        self.assertTrue(hasattr(dmstudio, 'transform_block_model'))
        self.assertIs(dmstudio.transform_block_model, canonical_transform)

        self.assertTrue(hasattr(agent, 'transform_model'))
        self.assertIs(agent.transform_model, canonical_transform)
        self.assertTrue(hasattr(agent, 'transform_block_model'))
        self.assertIs(agent.transform_block_model, canonical_transform)


if __name__ == '__main__':
    unittest.main()
