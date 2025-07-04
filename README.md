# Codepush MCP Server

This project provides a read-only MCP (Model Context Protocol) server for Codepush, exposing REST endpoints for app, deployment, and release information. Built with [FastMCP](https://github.com/jlowin/fastmcp).

## Features
- Authenticate with Codepush access key
- List CodePush apps
- List deployments for an app
- Get deployment history
- All endpoints are read-only

## Requirements
- Python 3.9+
- [uv](https://github.com/astral-sh/uv) (for package and virtual environment management)

## Setup

1. **Get repository**
   ```sh
   git clone https://github.com/mohammedbabelly20/codepush_mcp
   cd codepush_mcp
   ```

2. **Install uv:**
   ```sh
   pip install uv
   ```

3. **Sync dependencies:**
   ```sh
   uv sync
   ```

4. **Activate the virtual environment:**
   ```sh
   uv venv
   source .uv/bin/activate
   ```

5. **Run the server:**
   ```sh
   uv run src/main.py
   ```

## Usage
- The server exposes endpoints for authentication, listing apps, deployments, and release history.
- You must provide your Codepush access key.

## Install in client

### Claude Desktop config example

```json
{
  "mcpServers": {
    "CodePush MCP Server": {
      "command": "uv",  // or /path/to/uv
      "args": [
        "--project",
        "<path-to-cloned-repo>/codepush_mcp",
        "run",
        "python",
        "<path-to-cloned-repo>/codepush_mcp/src/main.py"
      ],
      "env": {
        "CODEPUSH_ACCESS_KEY": "<your-access-key>"  // <-- required
      }
    }
  }
}
```
restart Claude desktop to apply changes.

### MCP Inspector
You can use [MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector#pypi-package) for testing and debugging Model Context Protocol servers

```sh
npx @modelcontextprotocol/inspector \
  uv --project <path-to-cloned-repo>/codepush_mcp \
  run src/main.py
```
