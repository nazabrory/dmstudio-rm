'''
dmstudio.agent
--------------

AI agent helper module for Datamine Studio RM scripting.

Command discovery (list_commands, get_command_schema, search_commands) is
implemented in dmstudio.command_registry and re-exported here for backwards
compatibility. Import directly from command_registry when you need discovery
without COM, threading, or pandas side-effects.

Provides:
- list_commands()         : Return all available Datamine command names and descriptions.
- get_command_schema()    : Return the JSON schema (parameters, types) for a given command.
- search_commands()       : Fuzzy-search commands by name or keyword.
- read_datamine()         : Read a .dm or .dmx binary file into a pandas DataFrame using
                            the DmFile.DmTableADO COM object — no proprietary deps required.
- dialog_dismiss_context(): Context manager that auto-dismisses blocking Studio RM modal
                            dialogs in a background thread (opt-in).
'''


# ---------------------------------------------------------------------------
# Command discovery — re-exported from command_registry for backwards compat
# ---------------------------------------------------------------------------
from dmstudio.command_registry import (  # noqa: F401
    list_commands,
    get_command_schema,
    search_commands,
)

# ---------------------------------------------------------------------------
# DataFrame I/O — re-exported from dm_io for backwards compat
# ---------------------------------------------------------------------------
from dmstudio.dm_io import (  # noqa: F401
    read_datamine,
    to_datamine,
    patch_dataframe,
)
patch_dataframe()


# ---------------------------------------------------------------------------
# Auto-dialog dismissal context manager — re-exported from dialog for compat
# ---------------------------------------------------------------------------
from dmstudio.dialog import dialog_dismiss_context  # noqa: F401


# ---------------------------------------------------------------------------
# Sandbox management — re-exported from sandbox for backwards compat
# ---------------------------------------------------------------------------
from dmstudio.sandbox import (  # noqa: F401
    copy_database_files,
    initialize_sandbox,
)


# ---------------------------------------------------------------------------
# Tutorial bootstrapping — re-exported from bootstrap for backwards compat
# ---------------------------------------------------------------------------
from dmstudio.bootstrap import download_tutorials  # noqa: F401

