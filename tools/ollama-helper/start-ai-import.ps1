$ErrorActionPreference = "Stop"

$projectRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$ollamaPath = Join-Path $env:LOCALAPPDATA "Programs\Ollama\ollama.exe"
$helperPath = Join-Path $PSScriptRoot "server.js"
$adminUrl = "https://quoczai22.github.io/trac-nghiem-test/admin/import-export.html"

function Test-OllamaRunning {
  try {
    Invoke-WebRequest -UseBasicParsing "http://localhost:11434/api/tags" -TimeoutSec 2 | Out-Null
    return $true
  } catch {
    return $false
  }
}

function Get-HelperHealth {
  try {
    return Invoke-RestMethod "http://localhost:3100/" -TimeoutSec 2
  } catch {
    return $null
  }
}

function Test-CurrentHelper {
  $health = Get-HelperHealth
  return $null -ne $health -and $health.features -contains "parse-questions-v2"
}

if (-not (Test-Path $ollamaPath)) {
  throw "Khong tim thay Ollama. Hay cai Ollama truoc khi chay AI Import."
}

if (-not (Test-OllamaRunning)) {
  Write-Host "Dang khoi dong Ollama/Qwen..."
  Start-Process -FilePath $ollamaPath -ArgumentList "serve" -WindowStyle Hidden
  Start-Sleep -Seconds 3
}

if (-not (Test-CurrentHelper)) {
  $oldHealth = Get-HelperHealth
  if ($null -ne $oldHealth -and $oldHealth.message -eq "Ollama helper is running.") {
    Write-Host "Dang thay helper cu bang phien ban moi..."
    Get-NetTCPConnection -LocalPort 3100 -State Listen -ErrorAction SilentlyContinue |
      ForEach-Object { Stop-Process -Id $_.OwningProcess -Force }
    Start-Sleep -Seconds 1
  }

  $node = (Get-Command node -ErrorAction SilentlyContinue).Source
  if (-not $node) {
    $node = Join-Path $env:USERPROFILE "nodejs\node.exe"
  }
  if (-not (Test-Path $node)) {
    throw "Khong tim thay Node.js. Hay cai Node.js truoc khi chay AI Import."
  }

  Write-Host "Dang khoi dong Ollama helper..."
  Start-Process -FilePath $node -ArgumentList $helperPath -WorkingDirectory $projectRoot -WindowStyle Hidden
  Start-Sleep -Seconds 2
}

if (-not (Test-CurrentHelper)) {
  throw "Ollama helper chua khoi dong dung phien ban moi."
}

Start-Process $adminUrl
Write-Host "Ollama va helper da san sang. Da mo trang Admin."
