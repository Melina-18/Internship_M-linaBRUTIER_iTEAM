## Claude Desktop Configuration

To reproduce this configuration on Windows, the `%APPDATA%\Claude\claude_desktop_config.json` file must be configured as follows:

$$\text{Claude Desktop (Local)} \longrightarrow \text{MCP Server} \longrightarrow \text{Rosbridge (Port 9090)} \longrightarrow \text{ROS 2 / Gazebo}$$

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

### Connecting Claude to the ROS 2 Server to Run the Simulation

Follow these steps to launch the simulation environment and connect it to the LLM:

1. **Check your graphics configuration** (optional, to ensure hardware acceleration is active):
   ```bash
   glxinfo -B


2. **Launch the Gazebo world**
   ```bash
   ros2 launch robotnik_gazebo_ignition spawn_world.launch.py world:=demo gui:=true    

3. **Spawn the robot and start RViz (in a new terminal):**
   ```bash
   ros2 launch robotnik_gazebo_ignition spawn_robot.launch.py robot_id:=robot robot:=rbsummit robot_model:=rbsummit run_rviz:=true low_performance_simulation:=false

4. **Launch the sensor filters, localization, and navigation stacks (in separate terminals):**
   ```bash
   ros2 launch robotnik_simulation_bringup laser_filters.launch.py
   ros2 launch robotnik_simulation_localization localization.launch.py
   ros2 launch robotnik_simulation_navigation navigation.launch.py

5. **Launch the Rosbridge WebSocket server (in a new terminal):**

This server opens port 9090 to allow external interfaces and MCP servers to communicate with ROS 
   ```bash
   source /opt/ros/jazzy/setup.bash
   ros2 launch rosbridge_server rosbridge_websocket_launch.xml
   ```

7. **Start the LLM interface:**
 
Once the simulation is fully running, launch Claude Desktop to start interacting with the robot.  
Don't forget that both computers must be on the same network (Wi-Fi).

8. **Connecting Claude Desktop to the Robot**

Once the simulation and Claude Desktop are running, you need to instruct the LLM to connect to your local ROS 2 environment. 
Send the following prompt to **Claude**:
> "Please connect to my ROS 2 robot using this IP address: `ws://192.168.10.108:9090`."

Claude will then use the MCP server to initialize the WebSocket connection through Rosbridge and confirm that it can successfully monitor and control the robot.

