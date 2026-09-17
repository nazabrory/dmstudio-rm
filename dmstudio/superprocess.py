'''
Superprocess module - multi-command Studio RM workflows.
'''
from typing import List, Dict, Optional, Union, Any

from dmstudio import initialize
from dmstudio import dmcommands
from dmstudio.scratch import scratch_context


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

