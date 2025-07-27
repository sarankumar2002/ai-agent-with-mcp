# ai-agent-with-mcp
Google Gemini AI agent communicating with MCP server


## Architecture

```mermaid
graph TD;
    A(AI Agent - ADK UI) -->|Tool Calls| B(MCP Toolbox for Databases)
    B -->|Database Operations| C[MySQL Database]
    C -->|Results| B
    B -->|Responses| A

```