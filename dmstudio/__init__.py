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
    agent           - AI agent helpers: command discovery, file reading, dialog dismissal.
    notebook_builder- Jupyter Notebook builder for auditable agent workflows.
'''

from dmstudio import dmcommands
from dmstudio import dmfiles
from dmstudio import initialize
from dmstudio import special
from dmstudio import superprocess
from dmstudio import agent
from dmstudio import notebook_builder

# Shortcuts
from dmstudio.agent import download_tutorials