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

# Shortcuts
from dmstudio.bootstrap import download_tutorials, install_agent_skills
from dmstudio.validator import lint_command, validate_command
from dmstudio.scratch import scratch_context, ScratchManager
from dmstudio.dm_io import (
    read_datamine_header,
    read_datamine_summary,
    read_dm_header,
    read_dm_summary,
)