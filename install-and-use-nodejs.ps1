# Node.js Installation Script for Windows PowerShell
# Author: Node.js Installation Helper
# Description: Downloads, installs Node.js to a custom directory, creates sample project, and runs it

param(
    [string]$InstallDir = "$env:USERPROFILE\nodejs",
    [string]$ProjectDir = "$env:USERPROFILE\nodejs-project",
    [string]$NodeVersion = "20.11.0"
)

# Color-like output using Write-Host
function Write-Header {
    param([string]$Message)
    Write-Host "=== $Message ===" -ForegroundColor Yellow
}

function Write-Success {
    param([string]$Message)
    Write-Host $Message -ForegroundColor Green
}

function Write-Error-Custom {
    param([string]$Message)
    Write-Host $Message -ForegroundColor Red
}

function Write-Info {
    param([string]$Message)
    Write-Host $Message -ForegroundColor Yellow
}

Write-Header "Node.js Installation Script"
Write-Host ""

# Prompt for inputs if not provided as parameters
if ($InstallDir -eq "$env:USERPROFILE\nodejs") {
    $userInput = Read-Host "Enter custom installation directory (default: $env:USERPROFILE\nodejs)"
    if ($userInput) { $InstallDir = $userInput }
}

if ($ProjectDir -eq "$env:USERPROFILE\nodejs-project") {
    $userInput = Read-Host "Enter project directory (default: $env:USERPROFILE\nodejs-project)"
    if ($userInput) { $ProjectDir = $userInput }
}

$userInput = Read-Host "Enter Node.js version (default: 20.11.0)"
if ($userInput) { $NodeVersion = $userInput }

Write-Host ""
Write-Info "Configuration:"
Write-Info "Installation directory: $InstallDir"
Write-Info "Project directory: $ProjectDir"
Write-Info "Node.js version: $NodeVersion"
Write-Host ""

# Detect architecture
$arch = [System.Runtime.InteropServices.RuntimeInformation]::OSArchitecture
if ($arch -eq "Arm64") {
    $NODE_URL = "https://nodejs.org/dist/v$NodeVersion/node-v$NodeVersion-win-arm64.zip"
} else {
    $NODE_URL = "https://nodejs.org/dist/v$NodeVersion/node-v$NodeVersion-win-x64.zip"
}

Write-Info "Detected Architecture: $arch"
Write-Info "Download URL: $NODE_URL"
Write-Host ""

# Create directories
Write-Info "Creating installation directory..."
$null = New-Item -ItemType Directory -Force -Path $InstallDir
$null = New-Item -ItemType Directory -Force -Path $ProjectDir

# Download Node.js
Write-Info "Downloading Node.js v$NodeVersion..."
$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$zipPath = "$env:TEMP\node-v$NodeVersion-$timestamp.zip"

$maxRetries = 3
$retryCount = 0

while ($retryCount -lt $maxRetries) {
    try {
        $ProgressPreference = 'SilentlyContinue'
        Invoke-WebRequest -Uri $NODE_URL -OutFile $zipPath -ErrorAction Stop
        Write-Success "Downloaded successfully!"
        break
    } catch {
        $retryCount++
        if ($retryCount -lt $maxRetries) {
            Write-Info "Download failed, retrying ($retryCount/$maxRetries)..."
            Start-Sleep -Seconds 2
        } else {
            Write-Error-Custom "Failed to download Node.js after $maxRetries attempts: $_"
            exit 1
        }
    }
}

# Extract Node.js
Write-Info "Extracting Node.js..."
try {
    Expand-Archive -Path $zipPath -DestinationPath $env:TEMP -Force
    $extractedDir = Get-ChildItem -Path $env:TEMP -Filter "node-v$NodeVersion-win-*" -Directory | Select-Object -First 1
    
    if ($extractedDir) {
        Copy-Item -Path "$($extractedDir.FullName)\*" -Destination $InstallDir -Recurse -Force
        Write-Success "Node.js extracted and installed!"
    } else {
        Write-Error-Custom "Could not find extracted Node.js directory"
        exit 1
    }
} catch {
    Write-Error-Custom "Failed to extract Node.js: $_"
    exit 1
}

# Clean up
Remove-Item -Path $zipPath -Force -ErrorAction SilentlyContinue

Write-Host ""

# Update PATH for current session
$env:PATH = "$InstallDir;$env:PATH"

# Verify installation
Write-Info "Verifying installation..."
$nodeVersion = & "$InstallDir\node.exe" --version
$npmVersion = & "$InstallDir\npm.cmd" --version

Write-Success "Node.js version: $nodeVersion"
Write-Success "npm version: $npmVersion"
Write-Host ""

# Create sample project
Write-Info "Creating sample project in $ProjectDir..."

$packageJsonContent = @{
    name = "nodejs-sample"
    version = "1.0.0"
    description = "Sample Node.js project"
    main = "app.js"
    scripts = @{
        start = "node app.js"
        dev = "node --watch app.js"
    }
} | ConvertTo-Json

Set-Content -Path "$ProjectDir\package.json" -Value $packageJsonContent

$appJsContent = @"
const http = require('http');

const PORT = process.env.PORT || 3000;

const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end(`Hello from Node.js!\nServer running at http://localhost:`$`{PORT}\n`);
});

server.listen(PORT, () => {
  console.log(`Server is running at http://localhost:`$`{PORT}`);
  console.log('Press Ctrl+C to stop the server');
});
"@

Set-Content -Path "$ProjectDir\app.js" -Value $appJsContent

Write-Success "Sample project created!"
Write-Host ""

# Run sample app
Write-Info "Running sample app..."
Write-Success "Starting server on port 3000..."
Write-Host ""

$process = Start-Process -FilePath "$InstallDir\node.exe" -ArgumentList "$ProjectDir\app.js" -PassThru -NoNewWindow

Start-Sleep -Seconds 2

# Test the server
Write-Info "Testing server..."
try {
    $response = Invoke-WebRequest -Uri "http://localhost:3000" -TimeoutSec 2 -ErrorAction Stop
    Write-Success "Server responded:"
    Write-Host $response.Content
} catch {
    Write-Info "Could not connect to server (may still be starting)"
}

Write-Host ""
Write-Header "Installation Complete"
Write-Info "Node.js is installed at: $InstallDir"
Write-Info "Project directory: $ProjectDir"
Write-Info "Server Process ID: $($process.Id)"
Write-Host ""

Write-Info "To add Node.js to PATH permanently:"
Write-Info "  1. Search for 'Environment Variables' in Windows"
Write-Info "  2. Click 'Edit the system environment variables'"
Write-Info "  3. Click 'Environment Variables' button"
Write-Info "  4. Under 'User variables', click 'New'"
Write-Info "  5. Variable name: PATH, Variable value: $InstallDir"
Write-Info "  6. Click OK and restart PowerShell"
Write-Host ""

Write-Info "To stop the server, press Ctrl+C in this window or run:"
Write-Info "  Stop-Process -Id $($process.Id)"
Write-Host ""

Write-Info "To run the sample app manually:"
Write-Info "  & '$InstallDir\node.exe' '$ProjectDir\app.js'"

# Keep script running until user stops it
Write-Host ""
Write-Info "Press Ctrl+C to stop the server and exit..."
try {
    $process.WaitForExit()
} catch {
    # Handle Ctrl+C
}

# Cleanup
if ($process -and !$process.HasExited) {
    $process | Stop-Process -Force -ErrorAction SilentlyContinue
}
