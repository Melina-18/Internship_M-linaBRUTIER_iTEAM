# ROS MCP Server

This project uses the `uvx` tool to execute the `ros-mcp` MCP server in an ephemeral and secure manner.

## Claude Desktop Configuration

To reproduce this configuration on Windows, the `%APPDATA%\Claude\claude_desktop_config.json` file must be configured as follows:

```json
{
  "mcpServers": {
    "ros-mcp": {
      "command": "uvx",
      "args": [
        "ros-mcp",
        "--transport=stdio"
      ],
      "env": {
        "ROSBRIDGE_HOST": "192.168.10.108",
        "ROSBRIDGE_PORT": "9090"
      }
    }
  }
}

```


## Chat GPT Desktop Configuration

Unlike Claude Desktop, which runs locally on the machine, **ChatGPT** (OpenAI's web platform) operates entirely in the Cloud (Internet). Consequently, OpenAI's servers cannot directly access our local MCP server, as it is hidden behind the firewall and the private IP address of our local network.  
To resolve this network communication issue, we use **ngrok**, a tool that creates a secure tunnel and temporarily exposes our local server to the Internet.


$$\text{ChatGPT (Cloud)} \longrightarrow \text{Ngrok Public Link} \longrightarrow \text{Your PC (Local)} \longrightarrow \text{MCP Server} \longrightarrow \text{ROS 2 / Gazebo}$$

ChatGPT (Cloud) ──► Ngrok Public Link ──► Your PC (Local) ──► MCP Server ──► ROS 2 / Gazebo

ChatGPT (Cloud) ──► Ngrok Public Link ──► Your PC (Local) ──► MCP Server ──► ROS 2 / Gazebo












