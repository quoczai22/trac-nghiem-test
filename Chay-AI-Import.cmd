@echo off
setlocal
cd /d "%~dp0"

set "NODE=node"
where node >nul 2>nul
if errorlevel 1 (
  if exist "%USERPROFILE%\nodejs\node.exe" (
    set "NODE=%USERPROFILE%\nodejs\node.exe"
  ) else (
    echo Khong tim thay Node.js. Hay cai Node.js truoc khi chay AI Import.
    pause
    exit /b 1
  )
)

powershell -NoProfile -Command "try { $health = Invoke-RestMethod http://localhost:3100/ -TimeoutSec 2; if ($health.features -contains 'parse-questions') { exit 0 }; if ($health.message -eq 'Ollama helper is running.') { exit 2 }; exit 1 } catch { exit 1 }"
if errorlevel 2 goto stop-old-helper
if errorlevel 1 goto start-helper
goto open-admin

:stop-old-helper
echo Dang thay helper cu bang phien ban moi...
powershell -NoProfile -Command "Get-NetTCPConnection -LocalPort 3100 -State Listen -ErrorAction SilentlyContinue ^| ForEach-Object { Stop-Process -Id $_.OwningProcess -Force }"
timeout /t 1 /nobreak >nul

:start-helper
echo Dang khoi dong Ollama helper...
start "Ollama helper" /min "%NODE%" "tools\ollama-helper\server.js"
timeout /t 2 /nobreak >nul

:open-admin
echo Ollama helper da san sang.

start "" "https://quoczai22.github.io/trac-nghiem-test/admin/import-export.html"
echo Da mo trang Admin. Giu cua so Ollama helper chay trong nen khi Import AI.
endlocal
