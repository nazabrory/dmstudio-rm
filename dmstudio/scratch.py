'''
dmstudio.scratch
----------------

Managed in-memory scratch file context manager for Datamine Studio RM scripting.

In Datamine Studio RM, file names beginning with a leading underscore (_) are held
in memory as scratch tables and are not written to disk as permanent project files.
This module issues unique, collision-resistant scratch names (with optional human-readable
suffixes for debugging), tracks all scratch files created during the context lifecycle,
and guarantees clean intermediate workflows without polluting project folders.
'''

import re
import uuid
import contextlib
from typing import Optional, List, Dict, Any


def _ensure_scratch_prefix(name: str) -> str:
    '''Ensure name has strictly one leading underscore and no double underscores.'''
    if not name.startswith('_'):
        name = '_' + name
    while name.startswith('__'):
        name = name[1:]
    return name


class ScratchManager:
    '''
    Manager for generating and tracking unique in-memory Datamine scratch file names.
    '''

    def __init__(self, prefix: str = '_') -> None:
        self._prefix = _ensure_scratch_prefix(prefix)
        self._tracked: List[str] = []

    def temp(self, suffix: Optional[str] = None) -> str:
        '''
        Generate a unique in-memory scratch file name prefixed with an underscore.

        Parameters:
        -----------
        suffix: Optional[str]
            Optional human-readable label or suffix to describe the intermediate step.

        Returns:
        --------
        str:
            Unique scratch table name starting with a single underscore.
        '''
        raw_suffix = suffix or ''

        # Strip any leading underscores provided in suffix to avoid double underscore '__'
        cleaned = raw_suffix.lstrip('_')

        # Sanitize characters: allow only alphanumeric and underscore
        sanitized = re.sub(r'[^a-zA-Z0-9_]', '_', cleaned)
        # Collapse multiple consecutive underscores into one
        sanitized = re.sub(r'_+', '_', sanitized).strip('_')

        uid = uuid.uuid4().hex[:8]

        if sanitized:
            name = f'{self._prefix}{sanitized}_{uid}'
        else:
            name = f'{self._prefix}sc_{uid}'

        self._tracked.append(name)
        return name

    @property
    def tracked_names(self) -> List[str]:
        '''Return a shallow copy of all tracked scratch file names in order of generation.'''
        return list(self._tracked)

    def __len__(self) -> int:
        '''Return the count of tracked scratch file names.'''
        return len(self._tracked)

    def __contains__(self, name: object) -> bool:
        '''Check if a given scratch file name is currently tracked.'''
        return name in self._tracked

    def register(self, name: str) -> str:
        '''
        Manually register a custom scratch table name under this manager.
        Enforces a single leading underscore prefix.

        Parameters:
        -----------
        name: str
            Table name to register.

        Returns:
        --------
        str:
            Sanitized name starting with an underscore.
        '''
        name = _ensure_scratch_prefix(name)
        if name not in self._tracked:
            self._tracked.append(name)
        return name

    def report(self) -> Dict[str, Any]:
        '''
        Return a diagnostic summary report of all tracked scratch tables.

        Returns:
        --------
        dict:
            Diagnostic report with total table count and tracked table names.
        '''
        return {
            'count': len(self._tracked),
            'tables': list(self._tracked),
        }

    def cleanup(self, cmd: Optional[Any] = None, strict: bool = False) -> List[str]:
        '''
        Clean up all tracked in-memory scratch tables via Datamine command engine.

        Parameters:
        -----------
        cmd: Optional[Any]
            Studio RM command engine (e.g. from `dmcommands.init()`).
            If provided, calls `cmd.delete(in_i=table_name, confirm_p=0)` on each tracked table.
            If None, no Datamine deletion commands can be issued; returns empty list.
        strict: bool
            If True, re-raise any exception encountered during table deletion,
            or raise ValueError if cmd is None while tracked tables exist.
            If False (default), suppress errors (e.g. table was never materialized in memory).

        Returns:
        --------
        List[str]:
            List of successfully deleted scratch table names.
        '''
        if cmd is None:
            if strict and self._tracked:
                raise ValueError('Datamine command engine (cmd) is required for strict scratch cleanup.')
            return []

        deleted = []
        for name in list(self._tracked):
            try:
                cmd.delete(in_i=name, confirm_p=0)
                deleted.append(name)
            except Exception as e:
                if strict:
                    raise e

        # Remove successfully deleted tables from tracking
        for name in deleted:
            if name in self._tracked:
                self._tracked.remove(name)

        return deleted


@contextlib.contextmanager
def scratch_context(
    cmd: Optional[Any] = None,
    auto_cleanup: bool = False,
    prefix: str = '_',
    strict: bool = False,
):
    '''
    Context manager that provides managed, unique in-memory scratch file names
    for Datamine Studio RM automation.

    Intermediate Datamine steps using leading underscores are kept in memory
    and do not pollute the project folder on disk.

    Parameters:
    -----------
    cmd: Optional[Any]
        Datamine command engine instance (e.g. `dmcommands.init()`) used for auto-cleanup.
    auto_cleanup: bool
        If True, automatically deletes all generated scratch tables when exiting the context.
    prefix: str
        Prefix for scratch file names. Defaults to '_'.
    strict: bool
        If True, re-raises any deletion errors during cleanup.

    Yields:
    -------
    ScratchManager:
        Manager instance with `.temp(suffix=...)`, `.tracked_names`, and `.cleanup()`.

    Example:
    --------
    >>> with scratch_context() as sc:
    ...     temp_holes = sc.temp(suffix='dh_sort')
    ...     # Use temp_holes as intermediate table in cmd.mgsort(...)
    '''
    mgr = ScratchManager(prefix=prefix)
    try:
        yield mgr
    finally:
        if auto_cleanup and cmd is not None:
            mgr.cleanup(cmd=cmd, strict=strict)
