from codepush_mcp import mcp
import subprocess
import sys


def ensure_codepush_cli():
    try:
        subprocess.run(
            ["code-push", "--version"],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Installing @codemagic/code-push-cli globally...")
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "nodeenv"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        # Optionally, set up nodeenv if Node.js/npm is not available
        subprocess.run(["npm", "install", "-g", "@codemagic/code-push-cli"], check=True)
        print("@codemagic/code-push-cli installed.")


def main():
    ensure_codepush_cli()
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
