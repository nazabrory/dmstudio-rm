@echo off
REM ============================================================================
REM dmstudio JupyterLab Launch Script
REM ============================================================================
REM This script activates the virtual environment and starts JupyterLab.
REM Double-click this script to run your Datamine Python automation notebooks.
REM ============================================================================

echo.
echo ============================================
echo Starting JupyterLab for dmstudio
echo ============================================
echo.

if not exist ".venv" (
    echo ERROR: Virtual environment '.venv' not found!
    echo Please double-click 'setup_env.bat' first to install dmstudio.
    echo.
    pause
    exit /b 1
)

echo Activating environment...
call .venv\Scripts\activate.bat
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment.
    pause
    exit /b 1
)

echo Starting JupyterLab server...
echo Keep this command window open while using JupyterLab.
echo.
jupyter lab
