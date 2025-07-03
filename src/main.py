from codepush_mcp import mcp


if __name__ == "__main__":
    mcp.run(
        transport="stramable-http",
        host="0.0.0.0",
        port=4200,
        log_level="debug",
    )
