@echo off
REM ============================================================================
REM dmstudio Environment Setup Script for Windows
REM ============================================================================
REM This script creates a Python virtual environment and installs all
REM dependencies required for the dmstudio package.
REM
REM Requirements:
REM   - Python 3.9 or later installed and in PATH
REM   - Windows OS (required for pywin32 / COM automation)
REM   - Active Datamine Studio license (runtime only)
REM ============================================================================

echo.
echo ============================================
echo dmstudio Environment Setup
echo ============================================
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH.
    echo Please install Python 3.9+ from https://www.python.org/downloads/
    echo Ensure "Add Python to PATH" is checked during installation.
    pause
    exit /b 1
)

echo Python version:
python --version
echo.

REM Check Python version (minimum 3.9)
python -c "import sys; v=sys.version_info; exit(0 if v>=(3,9) else 1)" >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python 3.9 or later is required.
    pause
    exit /b 1
)

REM Check if virtual environment already exists
if exist ".venv" (
    echo Virtual environment '.venv' already exists.
    set /p RECREATE="Recreate it? (y/N): "
    if /i "!RECREATE!"=="y" (
        echo Removing existing virtual environment...
        rmdir /s /q .venv
    ) else (
        echo Using existing virtual environment.
        goto :activate
    )
)

REM Create virtual environment
echo Creating virtual environment '.venv'...
python -m venv .venv
if errorlevel 1 (
    echo ERROR: Failed to create virtual environment.
    echo Ensure the 'venv' module is available: python -m venv --help
    pause
    exit /b 1
)
echo Virtual environment created successfully.
echo.

:activate
REM Activate virtual environment
echo Activating virtual environment...
call .venv\Scripts\activate.bat
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment.
    pause
    exit /b 1
)

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

REM Install requirements
echo.
echo Installing dmstudio dependencies...
echo This may take a few minutes...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies.
    echo Check the error messages above and ensure you have internet access.
    pause
    exit /b 1
)

REM Install dmstudio in development mode
echo.
echo Installing dmstudio package in development mode...
pip install -e .
if errorlevel 1 (
    echo ERROR: Failed to install dmstudio package.
    pause
    exit /b 1
)

echo.
echo ============================================
echo Setup Complete!
echo ============================================
echo.
echo To activate the environment in the future, run:
echo   .venv\Scripts\activate.bat
echo.
echo To deactivate, run:
echo   deactivate
echo.
echo To verify installation:
echo   python -c "from dmstudio import dmcommands; print('OK')"
echo.
pause
