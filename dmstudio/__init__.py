'''
dmstudio package
----------------

Python package for Datamine Studio RM scripting via Windows COM automation.

Submodules:
    dmcommands      - Auto-generated wrappers for all Studio RM commands.
    dmfiles         - Studio commands that generate Datamine files (INPFIL etc).
    initialize      - COM initialization helpers.
    special         - Special/adapted Studio command helpers.
    superprocess    - Multi-command workflow helpers.
    agent           - Backward compatibility re-export layer for legacy AI agent scripts.
    notebook_builder- Jupyter Notebook builder for auditable agent workflows.
    sandbox         - Sandbox management and dataset copy helpers.
    dm_io           - High-level DataFrame ↔ Datamine file I/O operations.
    dialog          - Windows modal dialog auto-dismissal context.
    bootstrap       - Tutorial bootstrapping and download helpers.
    validator       - Pre-flight CLI command parser linter and safe validator.
    scratch         - Managed in-memory scratch file context manager.
    command_registry- Command discovery without COM or threading dependencies.
'''

# Proactively import pandas at the package root to avoid Python 3.14 / Cython circular import conflicts in debuggers
try:
    import pandas as _pd
except ImportError:
    pass

from dmstudio import dmcommands
from dmstudio import dmfiles
from dmstudio import initialize
from dmstudio import special
from dmstudio import superprocess
from dmstudio import agent
from dmstudio import notebook_builder
from dmstudio import sandbox
from dmstudio import dm_io
from dmstudio import dialog
from dmstudio import bootstrap
from dmstudio import validator
from dmstudio import scratch
from dmstudio import command_registry

# Shortcuts
from dmstudio.superprocess import batch_append, transform_model, transform_block_model, coordinate_transform
from dmstudio.bootstrap import download_tutorials, install_agent_skills
from dmstudio.validator import lint_command, validate_command
from dmstudio.scratch import scratch_context, ScratchManager
from dmstudio.dialog import dialog_dismiss_context
from dmstudio.notebook_builder import NotebookBuilder
from dmstudio.sandbox import copy_database_files, initialize_sandbox
from dmstudio.command_registry import list_commands, get_command_schema, search_commands
from dmstudio.dm_io import (
    read_datamine,
    to_datamine,
    read_datamine_header,
    read_datamine_summary,
    read_dm_header,
    read_dm_summary,
    resolve_table_path,
    patch_dataframe,
)

__all__ = [
    # Canonical submodules
    'agent',
    'bootstrap',
    'command_registry',
    'dialog',
    'dm_io',
    'dmcommands',
    'dmfiles',
    'initialize',
    'notebook_builder',
    'sandbox',
    'scratch',
    'special',
    'superprocess',
    'validator',
    # Datamine binary table I/O
    'read_datamine',
    'to_datamine',
    'read_datamine_header',
    'read_datamine_summary',
    'read_dm_header',
    'read_dm_summary',
    'resolve_table_path',
    'patch_dataframe',
    # Command discovery
    'list_commands',
    'get_command_schema',
    'search_commands',
    # Scratch file management
    'scratch_context',
    'ScratchManager',
    # CLI command validation & linting
    'lint_command',
    'validate_command',
    # Modal dialog handling
    'dialog_dismiss_context',
    # Multi-command superprocesses
    'batch_append',
    'transform_model',
    'transform_block_model',
    'coordinate_transform',
    # Bootstrapping & sandboxing
    'download_tutorials',
    'install_agent_skills',
    'copy_database_files',
    'initialize_sandbox',
    # Notebook builder
    'NotebookBuilder',
]