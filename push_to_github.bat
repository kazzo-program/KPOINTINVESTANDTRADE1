@echo off
title KPOINT Macro Terminal - Push to GitHub
echo =========================================================================
echo   KPOINT // DUAL REPOSITORY GITHUB SYNC
echo   1. https://github.com/kazzo-program/kpointpredict
echo   2. https://github.com/kazzo-program/KPOINTINVESTANDTRADE1
echo =========================================================================
echo.
cd /d "%~dp0"

echo [1/2] Pushing to kpointpredict...
git push kpointpredict main
if %ERRORLEVEL% equ 0 (
    echo [OK] Successfully synced kpointpredict!
) else (
    echo [ERROR] Failed to push to kpointpredict.
)
echo.

echo [2/2] Pushing to KPOINTINVESTANDTRADE1...
git push origin main
if %ERRORLEVEL% equ 0 (
    echo [OK] Successfully synced KPOINTINVESTANDTRADE1!
) else (
    echo [ERROR] Failed to push to KPOINTINVESTANDTRADE1.
)
echo.

echo =========================================================================
echo   ALL SYNC OPERATIONS COMPLETED!
echo =========================================================================
pause
