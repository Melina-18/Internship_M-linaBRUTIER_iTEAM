## Local LLM : Ollama Desktop Configuration

All control and routing are handled from the Linux PC.  
The Windows PC is used solely to run the Ollama engine because it didn't have enough RAM to run Ollama AND an interface at the same time. 

<div align="center">

```text
PC 1 (Windows - Ollama)             PC 2 (Linux - ROS)

┌───────────────────┐               ┌───────────────────┐
│   Ollama Server   │<==== HTTP ===>│ Script Python/ROS │
│  localhost:11434  │               │   Gazebo + Rviz   │
└───────────────────┘               └───────────────────┘
```
</div>


#### 1. Ollama installation
- llama3.2 : Main model (lightweight)  
- llama3 : Secondary model (more accurate)  

#### 2. Installation on a Linux PC  
```bash
sudo apt install curl -y
sudo apt install python3 -y
sudo apt install python3-requests -y
```


### Connecting ChatGPT to the ROS 2 Server to Run the Simulation
#### 1. Windows PC Setup (Start the LLM interface)

In Windows Terminal : 
```cmd
$env:OLLAMA_HOST="0.0.0.0:11434"  
ollama serve
```


#### 2. Linux PC Setup (Robot & Rosbridge)
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

6. **Configure the folder with instruction**  
```bash
nano robot_ollama.py
```

Ctrl+O, Entrée, Ctrl+X, and lanch :
```bash
python3 robot_ollama.py
```
