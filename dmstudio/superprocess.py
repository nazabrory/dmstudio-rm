'''
Superprocess module - multi-command Studio RM workflows.
'''
import os
import math
from typing import List, Dict, Optional, Union, Any

from dmstudio import initialize
from dmstudio import dmcommands
from dmstudio import dmfiles
from dmstudio.dialog import dialog_dismiss_context
from dmstudio.scratch import scratch_context
from dmstudio.dm_io import read_datamine_header, resolve_table_path


def dxf_to_dm(dxf_i, out_o, zone_f=None, zone_p=None):

    '''

    :param dxf_i: File in dxf format. The dxfin can also be provided as a full path
    :param out_o: Name of output file without the tr and pt suffix
    :param zone_f: zone field to be created in wireframe file
    :param zone_p: zone value - can be numeric or alphanumeric
    :return: returns a datamine tr and pt file
    '''

    assert dxf_i.lower().endswith('.dxf'), "Input file is not a dxf"

    oScript = initialize.studio(version=None)
    dmc = dmcommands.init()

    dmc.oScript.ActiveProject.Data.LoadFile(dxf_i)
    obj3d = oScript.ActiveProject.Data.LastObjectAdded

    if zone_f is None:
        obj3d.SaveAsDatamineFile(out_o, oScript.ActiveProject.ExtendedPrecision, True, "")
        obj3d.Unload()

    else:
        obj3d.SaveAsDatamineFile('_t1', oScript.ActiveProject.ExtendedPrecision, True, "")
        obj3d.Unload()

        # check if zone_value is numeric or alphanumeric

        if type(zone_p) is float or type(zone_p) is int:
            expression = " '" + zone_f + "=" + str(zone_p) + " '"
        else:
            expression = " '" + zone_f + ";a24=" + '"' + zone_p + '"' + " '"

        dmc.extra('_t1tr', out_o + 'tr', expression=expression)
        dmc.copy('_t1pt', out_o + 'pt')
        dmc.delete(in_i='_t1tr')
        dmc.delete(in_i='_t1pt')

def display_ellipsoids(in_i='required', out_o='required',
                       x_f='XPT', y_f='YPT', z_f='ZPT', trdipdir_f='TRDIPDIR', trdip_d='TRDIP', plunge_f='optional',
                       sdist1_p=100., sdist2_p=50., sdist3_p=25.,
                       num_ellipsoids_p=10, plunge_p=-90, invert_range_p=None):
    '''
    display_ellipsoids
    ------------------

    Generates wireframe ellipsoids for a set of randomly sampled spatial data points.
    Uses native dmstudio commands and the agent.read_datamine() function.

    Parameters:
    -----------
    in_i: str
        Input datamine file (without extension).
    out_o: str
        Output datamine file prefix (without tr/pt suffix).
    x_f, y_f, z_f: str
        Field names for X, Y, Z coordinates. Default: XPT, YPT, ZPT.
    trdipdir_f: str
        Trend/dip direction field name. Default: TRDIPDIR.
    trdip_d: str
        Dip field name. Default: TRDIP.
    plunge_f: str
        Plunge field name. Default: 'optional' (uses plunge_p constant).
    sdist1_p, sdist2_p, sdist3_p: float
        Semi-axis lengths. Defaults: 100, 50, 25.
    num_ellipsoids_p: int
        Number of ellipsoids to display. Default: 10.
    plunge_p: float
        Default plunge value when plunge_f is 'optional'. Default: -90.
    invert_range_p: list
        [min, max] trend range for plunge inversion. Default: [90, 270].
    '''
    import numpy as np
    from dmstudio import agent

    if invert_range_p is None:
        invert_range_p = [90, 270]

    if in_i == 'required':
        raise ValueError('in_i is required.')
    if out_o == 'required':
        raise ValueError('out_o is required.')

    # Use native read_datamine instead of proprietary pyrpa dependency
    df = agent.read_datamine(in_i + '.dm')
    choice = np.random.choice(df.index, min(num_ellipsoids_p, len(df)), replace=False)
    df_choice = df.loc[choice, :].copy().reset_index(drop=True)
    dm = dmcommands.init()

    if plunge_f == 'optional':
        df_choice = df_choice.copy()
        df_choice['_PLUNGE'] = plunge_p
        plunge_f = '_PLUNGE'

    for i in range(len(df_choice)):

        plunge = df_choice.loc[i, plunge_f]

        if df_choice.loc[i, trdipdir_f] > invert_range_p[1] or df_choice.loc[i, trdipdir_f] < invert_range_p[0]:
            plunge *= -1

        dm.ellipse(
            wiretr_o='_1tr',
            wirept_o='_1pt',
            sangle1_p=df_choice.loc[i, trdipdir_f],
            sangle2_p=df_choice.loc[i, trdip_d],
            sangle3_p=plunge,
            saxis1_p=3,
            saxis2_p=1,
            saxis3_p=3,
            sdist1_p=sdist1_p,
            sdist2_p=sdist2_p,
            sdist3_p=sdist3_p,
            xcentre_p=df_choice.loc[i, x_f],
            ycentre_p=df_choice.loc[i, y_f],
            zcentre_p=df_choice.loc[i, z_f])

        if i == 0:
            dm.copy('_1tr', '_2tr')
            dm.copy('_1pt', '_2pt')
        else:
            dm.addtri(
                wiretr1_i='_1tr',
                wirept1_i='_1pt',
                wiretr2_i='_2tr',
                wirept2_i='_2pt',
                wiretrou_o='_3tr',
                wireptou_o='_3pt')
            dm.copy('_3tr', '_2tr')
            dm.copy('_3pt', '_2pt')
    dm.copy('_2tr', out_o=out_o + "tr")
    dm.copy('_2pt', out_o=out_o + "pt")

    dm.delete('_1tr')
    dm.delete('_1pt')
    dm.delete('_2tr')
    dm.delete('_2pt')
    dm.delete('_3tr')
    dm.delete('_3pt')


def batch_append(
    tables_i: Optional[List[str]] = None,
    out_o: Optional[str] = None,
    flag_f: Optional[str] = None,
    flag_map: Optional[Dict[str, Any]] = None,
    sort_keys_f: Optional[Union[str, List[str]]] = None,
    cmd: Optional[Any] = None,
    **kwargs: Any,
) -> str:
    '''
    BATCH_APPEND
    ------------
    Consolidates an arbitrary list of Datamine tables into a single output table
    in one unified call, eliminating manual CLI string concatenation and sequential
    chaining errors.

    Intermediate chaining steps use managed in-memory scratch tables, leaving no
    permanent temporary files on disk. When flag_f is specified, each input table's
    records are tagged with provenance metadata prior to appending (defaulting to
    the source table name or custom mapped values from flag_map). When sort_keys_f
    is specified, the final table is sorted using Datamine's mgsort process.

    Parameters:
    -----------
    tables_i: List[str]
        List of Datamine table names (without .dm/.dmx extension) to append.
        Can also be passed as `tables` or `in_tables`.
    out_o: str
        Target output table name in the active project.
        Can also be passed as `out` or `out_table`.
    flag_f: Optional[str]
        Optional provenance flag field name to create in output table.
        Can also be passed as `flag_column`.
    flag_map: Optional[Dict[str, Any]]
        Optional dictionary mapping source table names to custom flag values
        (strings or numbers). Tables not in flag_map default to their table name.
    sort_keys_f: Optional[Union[str, List[str]]]
        Optional field name or list of field names to sort the output table by
        using mgsort. Can also be passed as `sort_keys` or `keys_f`.
    cmd: Optional[Any]
        Datamine command engine instance (e.g. from `dmcommands.init()`).
        If None, initializes a new command engine via `dmcommands.init()`.

    Returns:
    --------
    str:
        The target output table name (out_o).
    '''
    if tables_i is None:
        tables_i = kwargs.pop('tables', None) or kwargs.pop('in_tables', None)
    if out_o is None:
        out_o = kwargs.pop('out', None) or kwargs.pop('out_table', None)
    if flag_f is None:
        flag_f = kwargs.pop('flag_column', None)
    if sort_keys_f is None:
        sort_keys_f = kwargs.pop('sort_keys', None) or kwargs.pop('keys_f', None)

    if kwargs:
        raise TypeError(f"batch_append() got unexpected keyword argument(s): {', '.join(kwargs.keys())}")

    if tables_i is None:
        raise ValueError("tables_i is required and cannot be None.")
    if not isinstance(tables_i, (list, tuple)):
        raise ValueError(f"tables_i must be a list or tuple of table names, got {type(tables_i).__name__}.")
    if len(tables_i) == 0:
        raise ValueError("tables_i cannot be empty; provide at least one table name.")

    clean_tables: List[str] = []
    for idx, name in enumerate(tables_i):
        if not isinstance(name, str):
            raise ValueError(
                f"All elements in tables_i must be strings. Element at index {idx} is {type(name).__name__}: {name}"
            )
        stripped = name.strip()
        if not stripped:
            raise ValueError(f"Table name at index {idx} is empty or whitespace.")
        if '\\' in stripped:
            raise ValueError(
                f"Table name '{stripped}' contains Windows backslashes. "
                "Datamine command parser breaks on backslashes. Register files with ActiveProject.AddFile() and use logical names."
            )
        if ' ' in stripped:
            raise ValueError(
                f"Table name '{stripped}' contains spaces. "
                "Spaces break the Datamine command parser. Register files with ActiveProject.AddFile() and use logical names without spaces."
            )
        clean_tables.append(stripped)

    if out_o is None or not isinstance(out_o, str):
        raise ValueError(f"out_o must be a non-empty string, got {type(out_o).__name__ if out_o is not None else 'None'}.")
    clean_out = out_o.strip()
    if not clean_out:
        raise ValueError("out_o cannot be empty or whitespace.")
    if '\\' in clean_out:
        raise ValueError(
            f"Output table name '{clean_out}' contains Windows backslashes. "
            "Datamine command parser breaks on backslashes. Use a logical name residing in the active project."
        )
    if ' ' in clean_out:
        raise ValueError(
            f"Output table name '{clean_out}' contains spaces. "
            "Spaces break the Datamine command parser. Use a logical name without spaces."
        )

    clean_flag_f: Optional[str] = None
    if flag_f is not None:
        if not isinstance(flag_f, str):
            raise ValueError(f"flag_f must be a string, got {type(flag_f).__name__}.")
        clean_flag_f = flag_f.strip()
        if not clean_flag_f:
            raise ValueError("flag_f cannot be empty or whitespace.")
        if '\\' in clean_flag_f or ' ' in clean_flag_f:
            raise ValueError(f"flag_f '{clean_flag_f}' cannot contain backslashes or spaces.")

    if flag_map is not None:
        if not isinstance(flag_map, dict):
            raise ValueError(f"flag_map must be a dictionary, got {type(flag_map).__name__}.")

    clean_sort_keys: Optional[List[str]] = None
    if sort_keys_f is not None:
        if isinstance(sort_keys_f, str):
            sk = sort_keys_f.strip()
            if not sk:
                raise ValueError("sort_keys_f string cannot be empty.")
            clean_sort_keys = [sk]
        elif isinstance(sort_keys_f, (list, tuple)):
            if len(sort_keys_f) == 0:
                clean_sort_keys = None
            else:
                clean_sort_keys = []
                for s_idx, k in enumerate(sort_keys_f):
                    if not isinstance(k, str):
                        raise ValueError(
                            f"All elements in sort_keys_f must be strings. Element at index {s_idx} is {type(k).__name__}."
                        )
                    sk_clean = k.strip()
                    if not sk_clean:
                        raise ValueError(f"Sort key at index {s_idx} is empty or whitespace.")
                    clean_sort_keys.append(sk_clean)
        else:
            raise ValueError(f"sort_keys_f must be a string or list/tuple of strings, got {type(sort_keys_f).__name__}.")

    if cmd is None:
        cmd = dmcommands.init()

    with scratch_context(cmd=cmd, auto_cleanup=True) as sc:
        # 1. Provenance flag tagging (if requested)
        if clean_flag_f is not None:
            raw_values = [
                flag_map.get(t, t) if flag_map is not None and t in flag_map else t
                for t in clean_tables
            ]
            has_string = any(not isinstance(v, (int, float)) or isinstance(v, bool) for v in raw_values)
            if has_string:
                max_vlen = max(len(str(v)) for v in raw_values)
                flag_len = max(24, int((max_vlen - 1) // 4 + 1) * 4)
                flag_len = min(flag_len, 256)

            prep_tables: List[str] = []
            for t, val in zip(clean_tables, raw_values):
                if has_string:
                    val_str = str(val).replace('"', '')
                    expr = f'{clean_flag_f};A{flag_len} = "{val_str}"'
                else:
                    expr = f'{clean_flag_f};N = {val}'

                # If single table and no sorting, tag directly into target output
                if len(clean_tables) == 1 and clean_sort_keys is None:
                    cmd.extra(in_i=t, out_o=clean_out, arguments=f" '{expr}' 'GO' ")
                    return clean_out

                tagged_sc = sc.temp(suffix=f'tag_{t}')
                cmd.extra(in_i=t, out_o=tagged_sc, arguments=f" '{expr}' 'GO' ")
                prep_tables.append(tagged_sc)
        else:
            prep_tables = list(clean_tables)

        n = len(prep_tables)

        # 2. Single table pass-through
        if n == 1:
            single_input = prep_tables[0]
            if clean_sort_keys is not None:
                cmd.mgsort(in_i=single_input, out_o=clean_out, keys_f=clean_sort_keys)
            else:
                cmd.copy(in_i=single_input, out_o=clean_out)
            return clean_out

        # 3. Multi-table sequential append chaining
        curr = prep_tables[0]
        for i in range(1, n):
            is_last = (i == n - 1)
            next_input = prep_tables[i]

            if is_last and clean_sort_keys is None:
                target = clean_out
            else:
                target = sc.temp(suffix=f'chain_{i}')

            cmd.append(in1_i=curr, in2_i=next_input, out_o=target)
            curr = target

        # 4. Final sorting (if requested)
        if clean_sort_keys is not None:
            cmd.mgsort(in_i=curr, out_o=clean_out, keys_f=clean_sort_keys)

        return clean_out


def _validate_numeric_param(
    val: Any,
    name: str,
    min_val: Optional[float] = None,
    max_val: Optional[float] = None,
) -> float:
    '''Validate numeric parameter rejecting bools, None, NaN, and inf.'''
    if val is None or isinstance(val, bool) or not isinstance(val, (int, float)):
        raise ValueError(
            f"{name} must be a numeric value, got {type(val).__name__ if val is not None else 'None'}."
        )
    f_val = float(val)
    if math.isnan(f_val) or math.isinf(f_val):
        raise ValueError(f"{name} cannot be NaN or infinite.")
    if min_val is not None and f_val < min_val:
        raise ValueError(f"{name} must be >= {min_val}, got {f_val}.")
    if max_val is not None and f_val > max_val:
        raise ValueError(f"{name} must be <= {max_val}, got {f_val}.")
    return f_val


def transform_model(
    model_i: Optional[str] = None,
    out_o: Optional[str] = None,
    dx_p: Optional[float] = None,
    dy_p: Optional[float] = None,
    dz_p: float = 0.0,
    angle_p: float = 0.0,
    axis_p: int = 3,
    angle2_p: float = 0.0,
    axis2_p: int = 0,
    angle3_p: float = 0.0,
    axis3_p: int = 0,
    rotmod_p: Optional[int] = None,
    xworld_f: Optional[str] = None,
    yworld_f: Optional[str] = None,
    zworld_f: Optional[str] = None,
    is_prototype_p: Optional[bool] = None,
    method_p: Optional[str] = None,
    adjust_cells_p: bool = False,
    x_orig_p: Optional[float] = None,
    y_orig_p: Optional[float] = None,
    z_orig_p: Optional[float] = None,
    xinc_p: Optional[float] = None,
    yinc_p: Optional[float] = None,
    zinc_p: Optional[float] = None,
    nx_p: Optional[int] = None,
    ny_p: Optional[int] = None,
    nz_p: Optional[int] = None,
    cmd: Optional[Any] = None,
    **kwargs: Any,
) -> str:
    '''
    TRANSFORM_MODEL
    ---------------
    Translates, rotates, and recalculates block model prototypes and cell positions
    between local mine grids and UTM coordinate reference systems using approved
    Datamine file-based processes (COPYMOD, PROTOM, and EXTRA).

    Automates coordinate origin offsets, rotation axes, and cell position recalculation
    without requiring custom 3D matrix math or manual trigonometry in user notebooks.
    Intermediate transformation steps use managed in-memory scratch tables, leaving no
    temporary files on disk.

    Parameters:
    -----------
    model_i: str
        Input block model prototype or model file name (without .dm/.dmx extension).
        Can also be passed as `model`, `in_i`, `modelin_i`, `proto_i`, or `prototype_i`.
    out_o: str
        Target output transformed block model or prototype file name.
        Can also be passed as `out`, `modelout_o`, `proto_o`, or `prototype_o`.
    dx_p: float
        Translation offset along X axis (dx). Can also be passed as `dx`, `x_offset`, or `offset_x`.
    dy_p: float
        Translation offset along Y axis (dy). Can also be passed as `dy`, `y_offset`, or `offset_y`.
    dz_p: float
        Translation offset along Z axis (dz). Default: 0.0.
        Can also be passed as `dz`, `z_offset`, or `offset_z`.
    angle_p: float
        Primary rotation angle clockwise in degrees (-360 to 360). Default: 0.0.
        Can also be passed as `angle`, `angle1`, `angle1_p`, `rotation`, or `rot_angle`.
    axis_p: int
        Primary rotation axis (1=X, 2=Y, 3=Z, 0=None). Default: 3 (Z-axis / horizontal strike rotation).
        Can also be passed as `axis`, `axis1`, `axis1_p`, `rotaxis`, or `rotaxis_p`.
    angle2_p: float
        Secondary rotation angle clockwise in degrees. Default: 0.0.
    axis2_p: int
        Secondary rotation axis (0, 1, 2, 3). Default: 0.
    angle3_p: float
        Tertiary rotation angle clockwise in degrees. Default: 0.0.
    axis3_p: int
        Tertiary rotation axis (0, 1, 2, 3). Default: 0.
    rotmod_p: Optional[int]
        Model rotation mode (0 = non-rotated, 1 = rotated). If None, automatically inferred
        as 1 if angle_p != 0.0 or angle2_p != 0.0 or angle3_p != 0.0, else 0.
    xworld_f, yworld_f, zworld_f: Optional[str]
        Optional field names to store world coordinates in output rotated model.
    is_prototype: Optional[bool]
        Whether the input is a 0-record prototype. If None, auto-detected via header inspection.
    method: Optional[str]
        Transformation method: 'auto' (default), 'copymod', or 'protom'.
    adjust_cells: bool
        Whether to adjust cell center coordinates (XC, YC, ZC) via EXTRA. Default: False.
    x_orig_p, y_orig_p, z_orig_p: Optional[float]
        Explicit base model origin coordinates. If None, inspected from input table header.
    xinc_p, yinc_p, zinc_p: Optional[float]
        Explicit cell increments (XINC, YINC, ZINC). If None, inspected from input table header.
    nx_p, ny_p, nz_p: Optional[int]
        Explicit cell counts (NX, NY, NZ). If None, inspected from input table header.
    cmd: Optional[Any]
        Studio RM command engine instance (e.g. from dmcommands.init()).
        If None, initializes a new command engine via dmcommands.init().

    Returns:
    --------
    str:
        The target output table name (out_o).
    '''
    if model_i is None:
        model_i = (
            kwargs.pop('model', None)
            or kwargs.pop('in_i', None)
            or kwargs.pop('modelin_i', None)
            or kwargs.pop('proto_i', None)
            or kwargs.pop('prototype_i', None)
        )
    if out_o is None:
        out_o = (
            kwargs.pop('out', None)
            or kwargs.pop('modelout_o', None)
            or kwargs.pop('proto_o', None)
            or kwargs.pop('prototype_o', None)
        )
    if dx_p is None:
        dx_p = kwargs.pop('dx', None) or kwargs.pop('x_offset', None) or kwargs.pop('offset_x', None)
    if dy_p is None:
        dy_p = kwargs.pop('dy', None) or kwargs.pop('y_offset', None) or kwargs.pop('offset_y', None)
    if dz_p == 0.0:
        dz_p = kwargs.pop('dz', None) or kwargs.pop('z_offset', None) or kwargs.pop('offset_z', dz_p)
    if angle_p == 0.0:
        angle_p = (
            kwargs.pop('angle', None)
            or kwargs.pop('angle1', None)
            or kwargs.pop('angle1_p', None)
            or kwargs.pop('rotation', None)
            or kwargs.pop('rot_angle', angle_p)
        )
    if axis_p == 3:
        axis_p = (
            kwargs.pop('axis', None)
            or kwargs.pop('axis1', None)
            or kwargs.pop('axis1_p', None)
            or kwargs.pop('rotaxis', None)
            or kwargs.pop('rotaxis_p', axis_p)
        )

    if is_prototype_p is None:
        is_prototype_p = kwargs.pop('is_prototype', None)
    if method_p is None:
        method_p = kwargs.pop('method', None)
    if not adjust_cells_p:
        adjust_cells_p = bool(kwargs.pop('adjust_cells', adjust_cells_p))

    if kwargs:
        raise TypeError(f"transform_model() got unexpected keyword argument(s): {', '.join(kwargs.keys())}")

    # Validate table names
    if model_i is None or not isinstance(model_i, str):
        raise ValueError(
            f"model_i is required and must be a non-empty string, got {type(model_i).__name__ if model_i is not None else 'None'}."
        )
    clean_model = model_i.strip()
    if not clean_model:
        raise ValueError("model_i cannot be empty or whitespace.")
    if '\\' in clean_model:
        raise ValueError(
            f"model_i '{clean_model}' contains Windows backslashes. "
            "Datamine command parser breaks on backslashes. Register files with ActiveProject.AddFile() and use logical names."
        )
    if ' ' in clean_model:
        raise ValueError(
            f"model_i '{clean_model}' contains spaces. "
            "Spaces break the Datamine command parser. Register files with ActiveProject.AddFile() and use logical names without spaces."
        )

    if out_o is None or not isinstance(out_o, str):
        raise ValueError(
            f"out_o is required and must be a non-empty string, got {type(out_o).__name__ if out_o is not None else 'None'}."
        )
    clean_out = out_o.strip()
    if not clean_out:
        raise ValueError("out_o cannot be empty or whitespace.")
    if '\\' in clean_out:
        raise ValueError(
            f"out_o '{clean_out}' contains Windows backslashes. "
            "Datamine command parser breaks on backslashes. Use a logical name residing in the active project."
        )
    if ' ' in clean_out:
        raise ValueError(
            f"out_o '{clean_out}' contains spaces. "
            "Spaces break the Datamine command parser. Use a logical name without spaces."
        )

    # Validate numeric parameters
    clean_dx = _validate_numeric_param(dx_p, 'dx_p')
    clean_dy = _validate_numeric_param(dy_p, 'dy_p')
    clean_dz = _validate_numeric_param(dz_p, 'dz_p')

    clean_angle1 = _validate_numeric_param(angle_p, 'angle_p', min_val=-360.0, max_val=360.0)
    clean_angle2 = _validate_numeric_param(angle2_p, 'angle2_p', min_val=-360.0, max_val=360.0)
    clean_angle3 = _validate_numeric_param(angle3_p, 'angle3_p', min_val=-360.0, max_val=360.0)

    for ax_val, ax_name in [(axis_p, 'axis_p'), (axis2_p, 'axis2_p'), (axis3_p, 'axis3_p')]:
        if isinstance(ax_val, bool) or not isinstance(ax_val, int):
            raise ValueError(f"{ax_name} must be an integer in {{0, 1, 2, 3}}, got {type(ax_val).__name__}.")
        if ax_val not in (0, 1, 2, 3):
            raise ValueError(f"{ax_name} must be in {{0, 1, 2, 3}}, got {ax_val}.")

    # Determine base origin, cell sizes, and counts
    x_orig = x_orig_p
    y_orig = y_orig_p
    z_orig = z_orig_p
    xinc = xinc_p
    yinc = yinc_p
    zinc = zinc_p
    nx = nx_p
    ny = ny_p
    nz = nz_p
    auto_proto = is_prototype_p

    # Inspect input table header if any parameter is missing
    if any(v is None for v in [x_orig, y_orig, z_orig, xinc, yinc, zinc, nx, ny, nz]):
        hdr = None
        try:
            hdr = read_datamine_header(clean_model, cmd=cmd)
        except Exception as e:
            pass

        if hdr:
            if auto_proto is None and hdr.get('record_count', 0) == 0:
                auto_proto = True
            if 'attributes' in hdr:
                attrs = hdr['attributes']
                if x_orig is None:
                    x_orig = float(attrs.get('XMORIG', attrs.get('X0', 0.0)))
                if y_orig is None:
                    y_orig = float(attrs.get('YMORIG', attrs.get('Y0', 0.0)))
                if z_orig is None:
                    z_orig = float(attrs.get('ZMORIG', attrs.get('Z0', 0.0)))
                if xinc is None:
                    xinc = float(attrs.get('XINC', 10.0))
                if yinc is None:
                    yinc = float(attrs.get('YINC', 10.0))
                if zinc is None:
                    zinc = float(attrs.get('ZINC', 10.0))
                if nx is None:
                    nx = int(attrs.get('NX', 10))
                if ny is None:
                    ny = int(attrs.get('NY', 10))
                if nz is None:
                    nz = int(attrs.get('NZ', 10))

    # Defaults for unassigned origin/increments
    x_orig = 0.0 if x_orig is None else float(x_orig)
    y_orig = 0.0 if y_orig is None else float(y_orig)
    z_orig = 0.0 if z_orig is None else float(z_orig)
    xinc = 10.0 if xinc is None else float(xinc)
    yinc = 10.0 if yinc is None else float(yinc)
    zinc = 10.0 if zinc is None else float(zinc)
    nx = 10 if nx is None else int(nx)
    ny = 10 if ny is None else int(ny)
    nz = 10 if nz is None else int(nz)

    # Calculate transformed origin
    new_x = x_orig + clean_dx
    new_y = y_orig + clean_dy
    new_z = z_orig + clean_dz

    # Determine rotation mode
    is_rotated = (clean_angle1 != 0.0 or clean_angle2 != 0.0 or clean_angle3 != 0.0 or rotmod_p == 1)
    clean_rotmod = 1 if is_rotated else 0
    if rotmod_p is not None:
        clean_rotmod = int(rotmod_p)

    if cmd is None:
        cmd = dmcommands.init()

    with scratch_context(cmd=cmd, auto_cleanup=True) as sc:
        # Prototype definition workflow (PROTOM)
        if auto_proto or method_p == 'protom':
            sc_proto = sc.temp(suffix='proto')
            if clean_rotmod == 0:
                protom_args = (
                    f" 'N' 'Y' '{new_x}' '{new_y}' '{new_z}' '{xinc}' '{yinc}' '{zinc}' '{nx}' '{ny}' '{nz}'"
                )
            else:
                protom_args = (
                    f" 'N' 'Y' '{new_x}' '{new_y}' '{new_z}' '0' '0' '0' "
                    f"'{clean_angle1}' '{axis_p}' '{clean_angle2}' '{axis2_p}' '{clean_angle3}' '{axis3_p}' "
                    f"'{xinc}' '{yinc}' '{zinc}' '{nx}' '{ny}' '{nz}'"
                )

            with dialog_dismiss_context():
                if hasattr(cmd, 'protom'):
                    cmd.protom(out_o=sc_proto, rotmod_p=clean_rotmod, arguments=protom_args)
                else:
                    dmfiles.init().protom(out_o=sc_proto, rotmod_p=clean_rotmod, arguments=protom_args)

            cmd.copy(in_i=sc_proto, out_o=clean_out)
            return clean_out

        # Direct EXTRA cell translation workflow
        if method_p == 'extra':
            sc_extra = sc.temp(suffix='extra')
            extra_args = f" 'XC = XC + {clean_dx}' 'YC = YC + {clean_dy}' 'ZC = ZC + {clean_dz}' 'GO' "
            cmd.extra(in_i=clean_model, out_o=sc_extra, arguments=extra_args)
            cmd.copy(in_i=sc_extra, out_o=clean_out)
            return clean_out

        # Block model transformation workflow (COPYMOD)
        modtype = kwargs.pop('modtype_p', None) or kwargs.pop('modtype', None)
        if modtype is None:
            modtype = 2 if clean_rotmod == 1 else 1
        else:
            modtype = int(modtype)

        cm_tokens = [
            f"@xneworig={new_x}",
            f"@yneworig={new_y}",
            f"@zneworig={new_z}",
        ]
        if clean_rotmod == 1 or modtype in (2, 4):
            cm_tokens.append(f"@angle1={clean_angle1}")
            cm_tokens.append(f"@axis1={axis_p}")
            if clean_angle2 != 0.0:
                cm_tokens.append(f"@angle2={clean_angle2}")
                cm_tokens.append(f"@axis2={axis2_p}")
            if clean_angle3 != 0.0:
                cm_tokens.append(f"@angle3={clean_angle3}")
                cm_tokens.append(f"@axis3={axis3_p}")

        cm_args = " " + " ".join(cm_tokens)

        sc_trans = sc.temp(suffix='copymod')
        cmd.copymod(
            modelin_i=clean_model,
            modelout_o=sc_trans,
            xworld_f=xworld_f if xworld_f is not None else 'optional',
            yworld_f=yworld_f if yworld_f is not None else 'optional',
            zworld_f=zworld_f if zworld_f is not None else 'optional',
            modtype_p=modtype,
            arguments=cm_args,
        )

        curr = sc_trans

        # If adjust_cells is requested, chain EXTRA to update cell coordinates
        if adjust_cells_p:
            sc_extra = sc.temp(suffix='extra')
            extra_args = f" 'XC = XC + {clean_dx}' 'YC = YC + {clean_dy}' 'ZC = ZC + {clean_dz}' 'GO' "
            cmd.extra(in_i=curr, out_o=sc_extra, arguments=extra_args)
            curr = sc_extra

        cmd.copy(in_i=curr, out_o=clean_out)
        return clean_out


# Backward compatibility and semantic aliases
transform_block_model = transform_model
coordinate_transform = transform_model

