#!/bin/bash

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}=== Node.js Installation Script ===${NC}"
echo ""

# Prompt for custom installation directory
read -p "Enter custom installation directory (default: ~/nodejs): " INSTALL_DIR
INSTALL_DIR=${INSTALL_DIR:-~/nodejs}
INSTALL_DIR=$(eval echo "$INSTALL_DIR")

# Prompt for project directory
read -p "Enter project directory (default: ~/nodejs-project): " PROJECT_DIR
PROJECT_DIR=${PROJECT_DIR:-~/nodejs-project}
PROJECT_DIR=$(eval echo "$PROJECT_DIR")

# Prompt for Node.js version
read -p "Enter Node.js version (default: 20.11.0): " NODE_VERSION
NODE_VERSION=${NODE_VERSION:-20.11.0}

echo ""
echo -e "${YELLOW}Configuration:${NC}"
echo "Installation directory: $INSTALL_DIR"
echo "Project directory: $PROJECT_DIR"
echo "Node.js version: $NODE_VERSION"
echo ""

# Detect OS and architecture
OS=$(uname -s)
ARCH=$(uname -m)

case "$OS" in
  Darwin)
    if [ "$ARCH" = "arm64" ]; then
      NODE_URL="https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-darwin-arm64.tar.xz"
    else
      NODE_URL="https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-darwin-x64.tar.xz"
    fi
    ;;
  Linux)
    if [ "$ARCH" = "aarch64" ]; then
      NODE_URL="https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-arm64.tar.xz"
    else
      NODE_URL="https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.xz"
    fi
    ;;
  *)
    echo -e "${RED}Unsupported OS: $OS${NC}"
    exit 1
    ;;
esac

echo -e "${YELLOW}Detected OS: $OS, Architecture: $ARCH${NC}"
echo -e "${YELLOW}Download URL: $NODE_URL${NC}"
echo ""

# Create installation directory
echo -e "${YELLOW}Creating installation directory...${NC}"
mkdir -p "$INSTALL_DIR"
mkdir -p "$PROJECT_DIR"

# Download Node.js
echo -e "${YELLOW}Downloading Node.js v$NODE_VERSION...${NC}"
cd "$INSTALL_DIR" || exit 1
curl -fsSL "$NODE_URL" | tar xJ --strip-components=1

if [ $? -ne 0 ]; then
  echo -e "${RED}Failed to download or extract Node.js${NC}"
  exit 1
fi

echo -e "${GREEN}Node.js installed successfully!${NC}"
echo ""

# Update PATH
echo -e "${YELLOW}Configuring PATH...${NC}"
export PATH="$INSTALL_DIR/bin:$PATH"

# Add to shell rc files
for RC_FILE in ~/.bashrc ~/.zshrc ~/.bash_profile ~/.profile; do
  if [ -f "$RC_FILE" ]; then
    if ! grep -q "export PATH=\"$INSTALL_DIR/bin" "$RC_FILE"; then
      echo "export PATH=\"$INSTALL_DIR/bin:\$PATH\"" >> "$RC_FILE"
      echo "Added PATH to $RC_FILE"
    fi
  fi
done

echo ""
echo -e "${YELLOW}Verifying installation...${NC}"
NODE_VERSION_INSTALLED=$("$INSTALL_DIR/bin/node" --version)
NPM_VERSION_INSTALLED=$("$INSTALL_DIR/bin/npm" --version)

echo -e "${GREEN}Node.js version: $NODE_VERSION_INSTALLED${NC}"
echo -e "${GREEN}npm version: $NPM_VERSION_INSTALLED${NC}"
echo ""

# Create sample project
echo -e "${YELLOW}Creating sample project in $PROJECT_DIR...${NC}"

cat > "$PROJECT_DIR/package.json" << 'EOF'
{
  "name": "nodejs-sample",
  "version": "1.0.0",
  "description": "Sample Node.js project",
  "main": "app.js",
  "scripts": {
    "start": "node app.js",
    "dev": "node --watch app.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}
EOF

cat > "$PROJECT_DIR/app.js" << 'EOF'
const http = require('http');

const PORT = process.env.PORT || 3000;

const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end(`Hello from Node.js!\nServer running at http://localhost:${PORT}\n`);
});

server.listen(PORT, () => {
  console.log(`Server is running at http://localhost:${PORT}`);
  console.log('Press Ctrl+C to stop the server');
});
EOF

echo -e "${GREEN}Sample project created!${NC}"
echo ""

# Run sample app
echo -e "${YELLOW}Running sample app...${NC}"
echo -e "${GREEN}Starting server on port 3000...${NC}"
echo ""

cd "$PROJECT_DIR" || exit 1
"$INSTALL_DIR/bin/node" app.js &
SERVER_PID=$!

sleep 2

# Test the server
echo -e "${YELLOW}Testing server...${NC}"
if command -v curl &> /dev/null; then
  curl -s http://localhost:3000
  echo ""
fi

echo ""
echo -e "${GREEN}=== Installation Complete ===${NC}"
echo "Node.js is installed at: $INSTALL_DIR"
echo "Project directory: $PROJECT_DIR"
echo "Server PID: $SERVER_PID"
echo ""
echo -e "${YELLOW}To use Node.js in new terminal sessions, run:${NC}"
echo "  source ~/.bashrc  # or ~/.zshrc"
echo ""
echo -e "${YELLOW}To stop the server, run:${NC}"
echo "  kill $SERVER_PID"
echo ""
echo -e "${YELLOW}To run the sample app manually:${NC}"
echo "  cd $PROJECT_DIR && $INSTALL_DIR/bin/node app.js"
