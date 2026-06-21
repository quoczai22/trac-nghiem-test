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

powershell -NoProfile -Command "try { Invoke-WebRequest -UseBasicParsing http://localhost:3100/ -TimeoutSec 2 ^| Out-Null; exit 0 } catch { exit 1 }"
if errorlevel 1 (
  echo Dang khoi dong Ollama helper...
  start "Ollama helper" /min "%NODE%" "tools\ollama-helper\server.js"
  timeout /t 2 /nobreak >nul
) else (
  echo Ollama helper da dang chay.
)

start "" "https://quoczai22.github.io/trac-nghiem-test/admin/import-export.html"
echo Da mo trang Admin. Giu cua so Ollama helper chay trong nen khi Import AI.
endlocal
