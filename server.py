# server.py

from fastmcp import FastMCP


# Create an MCP server
mcp = FastMCP("Swiss")


# Add an addition tool
@mcp.tool()
def do_something(request: str) -> str:
    """Do something"""
    return "Processing request: " + request