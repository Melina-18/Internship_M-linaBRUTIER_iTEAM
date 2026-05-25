# ROS MCP Server

This project uses the `uvx` tool to execute the `ros-mcp` MCP server in an ephemeral and secure manner.

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

6. **Start the LLM interface:**
Once the simulation is fully running, launch Claude Desktop to start interacting with the robot.

7. **Connecting Claude Desktop to the Robot**
Once the simulation and Claude Desktop are running, you need to instruct the LLM to connect to your local ROS 2 environment. 
Send the following prompt to **Claude**:
> "Please connect to my ROS 2 robot using this IP address: `ws://192.168.10.108:9090`."

Claude will then use the MCP server to initialize the WebSocket connection through Rosbridge and confirm that it can successfully monitor and control the robot.





## Chat GPT Desktop Configuration

Unlike Claude Desktop, which runs locally on the machine, **ChatGPT** (OpenAI's web platform) operates entirely in the Cloud (Internet). Consequently, OpenAI's servers cannot directly access our local MCP server, as it is hidden behind the firewall and the private IP address of our local network.  
To resolve this network communication issue, we use **ngrok**, a tool that creates a secure tunnel and temporarily exposes our local server to the Internet.


$$\text{ChatGPT (Cloud)} \longrightarrow \text{Ngrok Public Link} \longrightarrow \text{Your PC (Local)} \longrightarrow \text{MCP Server} \longrightarrow \text{Rosbridge (Port 9090)} \longrightarrow \text{ROS 2 / Gazebo}$$


### Connecting ChatGPT to the ROS 2 Server to Run the Simulation

To connect the ChatGPT Cloud model to your local MCP server, you need to set up a network bridge on your Windows PC and expose it using **ngrok**. 

Follow these steps in order:

#### 1. Linux PC Setup (Robot & Rosbridge)
Ensure that your ROS 2 simulation and the Rosbridge WebSocket server are up and running on your Linux machine (IP: 192.168.10.108) on port 9090.

1. **Check your graphics configuration** (optional, to ensure hardware acceleration is active):
   ```bash
   glxinfo -B
   ```

2. **Launch the Gazebo world**
   ```bash
   ros2 launch robotnik_gazebo_ignition spawn_world.launch.py world:=demo gui:=true
   ```

3. **Spawn the robot and start RViz (in a new terminal):**
   ```bash
   ros2 launch robotnik_gazebo_ignition spawn_robot.launch.py robot_id:=robot robot:=rbsummit robot_model:=rbsummit run_rviz:=true low_performance_simulation:=false
   ```

4. **Launch the sensor filters, localization, and navigation stacks (in separate terminals):**
   ```bash
   ros2 launch robotnik_simulation_bringup laser_filters.launch.py
   ros2 launch robotnik_simulation_localization localization.launch.py
   ros2 launch robotnik_simulation_navigation navigation.launch.py
   ```
   
5. **Launch the Rosbridge WebSocket server (in a new terminal):**
   This server opens port 9090 to allow external interfaces and MCP servers to communicate with ROS 
   ```bash
   source /opt/ros/jazzy/setup.bash
   ros2 launch rosbridge_server rosbridge_websocket_launch.xml
   ```

#### 2. Windows PC Setup (Start the LLM interface)

##### Step A: Port Forwarding (Command Prompt - Admin)
Open **Command Prompt as Administrator** and run the following command to route the local port to your Linux machine's IP address:
```cmd
netsh interface portproxy add v4tov4 listenport=9090 listenaddress=127.0.0.1 connectport=9090 connectaddress=192.168.10.108
```

##### Step B: Port Forwarding (Command Prompt - Admin)
Open **PowerShell** and set the environment variables to point to your Rosbridge server, then launch the ROS MCP server:
```cmd
$env:ROSBRIDGE_HOST="192.168.10.108"; $env:ROSBRIDGE_PORT="9090"; uvx ros-mcp --transport streamable-http --host 127.0.0.1 --port 9000
```

##### Step C: Expose the Server via ngrok (Terminal)
Open a new terminal and start the ngrok tunnel to make your local MCP server accessible from the cloud:
```cmd
ngrok http --url=untreated-cosmic-underfoot.ngrok-free.dev 127.0.0.1:9000
```


7. **Connecting Claude Desktop to the Robot**

Once the simulation and Chat GPT are running, you need to instruct the LLM to connect to your local ROS 2 environment. 
Send the following prompt to **Chat GPT**:
> "Please connect to my ROS 2 robot using this IP address: `ws://192.168.10.108:9090`."

The robot is now connected to the LLM (AI) and is ready to receive commands. 



