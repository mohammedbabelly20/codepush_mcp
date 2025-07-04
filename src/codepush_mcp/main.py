from codepush_mcp import mcp


def main():
    mcp.run(transport="stdio")
    # mcp.run(
    #     transport="http",
    #     host="0.0.0.0",
    #     port=4200,
    #     log_level="debug",
    # )


if __name__ == "__main__":
    main()
