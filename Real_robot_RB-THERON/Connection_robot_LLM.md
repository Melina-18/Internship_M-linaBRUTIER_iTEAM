# Connection LLM ↔ RB-THERON

This describes the connection between Claude Desktop (via an MCP server + rosbridge) and the RB-THERON physical robot, following a simulation-based development phase on the RB-SUMMIT.

Rosbridge runs directly on the robot's onboard computer (`THER0`), which is reachable on the university network via the IP address `10.45.26.22:9090`.

```
Claude Desktop (Windows) → MCP Server (ros-mcp-theron) → ws://10.45.26.22:9090 → rosbridge (on THER0) → robot's native ROS2 graph
```

I added the following entry to my `claude_desktop_config.json`:

```json
"ros-mcp-theron": {
  "command": "uvx",
  "args": ["ros-mcp", "--transport=stdio"],
  "env": {
    "ROSBRIDGE_HOST": "10.45.26.22",
    "ROSBRIDGE_PORT": "9090"
  }
}
```

> `ROSBRIDGE_HOST` is the robot's IP address on the university network.

## Validation

Once rosbridge was running on `THER0` and the config above was loaded, Claude Desktop successfully listed all ~140 native topics of the robot (navigation, motor control, sensors, system state, TF), confirming the full chain works end-to-end.

<img width="1183" height="874" alt="image" src="https://github.com/user-attachments/assets/150dc0ca-0669-4332-89f4-171e6c27457b" />


---

# On the Linux PC 
To establish a connection between the robot and the Linux PC, start by turning on the robot, and then enter these commands in the Linux terminal: 
```bash
ping 10.45.26.22
```
then, Ctrl +C, then : 

```bash
ssh robot@10.45.26.22
```
The robot is now connected; next, we run rosbridge on this terminal to communicate with the Windows PC that hosts the LLM.
```bash
ros2 launch rosbridge_server rosbridge_websocket_launch.xml
```
We can now run Claude and run our tests. 
