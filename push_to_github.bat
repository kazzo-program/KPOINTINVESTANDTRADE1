@echo off
echo ========================================================
echo   QUANTO MACRO TERMINAL - PUSH TO GITHUB
echo   Repository: https://github.com/kazzo-program/KPOINTINVESTANDTRADE1
echo ========================================================
echo.
cd /d "%~dp0"
echo Checking remote...
git remote -v
echo.
echo Pushing branch 'main' to GitHub...
git push -u origin main
echo.
if %ERRORLEVEL% equ 0 (
    echo ========================================================
    echo   SUCCESS! All files are now live on GitHub:
    echo   https://github.com/kazzo-program/KPOINTINVESTANDTRADE1
    echo ========================================================
) else (
    echo [ERROR] Push did not complete. Please see message above.
)
echo.
pause
