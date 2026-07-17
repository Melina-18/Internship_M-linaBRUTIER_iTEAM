# Connexion LLM ↔ RB-THERON

We describe the connection between Claude Desktop (via an MCP server + rosbridge) and the RB-THERON physical robot, following a simulation-based development phase on RB-SUMMIT.
 I ran Rosbridge directly on the robot's computer (THER0), which is accessible on the university network via the IP address 10.45.26.22:9090. 

$$\text{Claude Desktop (Windows)} \longrightarrow \text{MCP Server (ros-mcp-theron} \longrightarrow \text{ws://10.45.26.22:9090} \longrightarrow \text{rosbridge (in THERO) \longrightarrow \text{robot's native ROS2 graph}$$

I added this code to my "claude_desktop_config.json" folder : 
```json
"ros-mcp-theron": {
  "command": "uvx",
  "args": ["ros-mcp", "--transport=stdio"],
  "env": {
    "ROSBRIDGE_HOST": "10.45.26.22",    #(the robot's IP address)
    "ROSBRIDGE_PORT": "9090"
  }
}
```




