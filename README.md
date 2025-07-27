# ai-agent-with-mcp
Google Gemini AI agent communicating with MCP server


## Architecture

```mermaid
graph TD;
    A(AI Agent (ADK)) -->|Tool Calls| B(MCP Toolbox for Databases)
    B -->|Database Operations| C[MySQL Database]
    C -->|Results| B
    B -->|Responses| A

```

```mermaid
graph TD;
    AI Agent (adk) -->|Tool Calls| MCP Toolbox;
    MCP Toolbox -->|Database Operations| MySQL Database;
    MySQL Database-->|Results| MCP Toolbox ;
    MCP Toolbox -->|Responses|  AI Agent (adk) ;
```