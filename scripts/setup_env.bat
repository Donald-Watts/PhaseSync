@echo off
setlocal enabledelayedexpansion

:: Get the absolute path to the scripts directory (where this script lives)
set "SCRIPTS_DIR=%~dp0"
:: Remove trailing backslash if present
if "%SCRIPTS_DIR:~-1%"=="\\" set "SCRIPTS_DIR=%SCRIPTS_DIR:~0,-1%"

:: The project root is the parent of the scripts directory
for %%I in ("%SCRIPTS_DIR%\..") do set "WORKSPACE_ROOT=%%~fI"

:: Check if required directories exist
if not exist "%WORKSPACE_ROOT%\scripts" (
    echo Error: scripts directory not found!
    echo Please make sure your project structure is correct.
    pause
    exit /b 1
)

if not exist "%WORKSPACE_ROOT%\src" (
    echo Error: src directory not found!
    echo Please make sure your project structure is correct.
    pause
    exit /b 1
)

:: Check if weight_analysis.py exists
if not exist "%WORKSPACE_ROOT%\scripts\weight_analysis.py" (
    echo Error: weight_analysis.py not found in scripts directory!
    echo Please make sure all required files are present.
    pause
    exit /b 1
)

:: Create a temporary file for the environment variables
echo @echo off > "%TEMP%\phasesync_env.bat"
echo set PHASESYNC_HOME=%WORKSPACE_ROOT% >> "%TEMP%\phasesync_env.bat"
echo set PYTHONPATH=%WORKSPACE_ROOT%;%WORKSPACE_ROOT%\src >> "%TEMP%\phasesync_env.bat"

:: Set the environment variables for the current session
set "PHASESYNC_HOME=%WORKSPACE_ROOT%"
set "PYTHONPATH=%WORKSPACE_ROOT%;%WORKSPACE_ROOT%\src"

:: Create a desktop shortcut to set environment variables
echo Set oWS = WScript.CreateObject("WScript.Shell") > "%TEMP%\CreateShortcut.vbs"
echo sLinkFile = oWS.SpecialFolders("Desktop") ^& "\PhaseSync Environment.bat" >> "%TEMP%\CreateShortcut.vbs"
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> "%TEMP%\CreateShortcut.vbs"
echo oLink.TargetPath = "%TEMP%\phasesync_env.bat" >> "%TEMP%\CreateShortcut.vbs"
echo oLink.Description = "Set PhaseSync Environment Variables" >> "%TEMP%\CreateShortcut.vbs"
echo oLink.WorkingDirectory = "%WORKSPACE_ROOT%" >> "%TEMP%\CreateShortcut.vbs"
echo oLink.Save >> "%TEMP%\CreateShortcut.vbs"
cscript //nologo "%TEMP%\CreateShortcut.vbs"
del "%TEMP%\CreateShortcut.vbs"

echo.
echo PhaseSync Environment Setup Complete!
echo.
echo A shortcut has been created on your desktop called "PhaseSync Environment.bat"
echo Double-click this shortcut whenever you need to set up the environment variables.
echo.
echo Current environment variables:
echo PHASESYNC_HOME: %WORKSPACE_ROOT%
echo PYTHONPATH: %WORKSPACE_ROOT%;%WORKSPACE_ROOT%\src
echo.
echo Press any key to exit...
pause > nul

endlocal 