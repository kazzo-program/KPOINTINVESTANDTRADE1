@echo off
title KPoint Equities Alpha - Push to GitHub
echo =========================================================================
echo   KPOINT EQUITIES ALPHA // INSTITUTIONAL STOCK TERMINAL - GITHUB SYNC
echo   Repository: https://github.com/kazzo-program/KPOINTINVESTANDTRADE1
echo =========================================================================
echo.
cd /d "%~dp0"

echo Pushing to KPOINTINVESTANDTRADE1 (origin)...
git push origin main
if %ERRORLEVEL% equ 0 (
    echo [OK] Successfully synced KPOINTINVESTANDTRADE1!
) else (
    echo [ERROR] Failed to push to origin.
)
echo.

echo =========================================================================
echo   ALL SYNC OPERATIONS COMPLETED!
echo =========================================================================
pause
