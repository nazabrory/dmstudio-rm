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
'''

# Proactively import pandas at the package root to avoid Python 3.14 / Cython circular import conflicts in debuggers
try:
    import pandas as _pd
except ImportError:
    pass

from dmstudio import dmcommands
from dmstudio import dmfiles
from dmstudio import dmcommands_generated
from dmstudio import dmfiles_generated
from dmstudio import initialize
from dmstudio import special
from dmstudio import superprocess
from dmstudio import agent
from dmstudio import notebook_builder
from dmstudio import sandbox
from dmstudio import dm_io
from dmstudio import dialog
from dmstudio import bootstrap

# Shortcuts
from dmstudio.bootstrap import download_tutorials