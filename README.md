# Project Architecture and Environment Setup

#### Linux PC :
Ubuntu 22.04, ROS 2 Jazzy  
Installtion of Gazebo Harmonic (version 8), Rviz (version 14.1.20.) and Rosbridge (version 2.6.0)  
Rosbridge WebSocket server started on port 9090  
IP address (command :  hostname -I) : 192.168.10.108  

#### Windows PC :
Installation of LLM --> Claude Desktop / Chat GPT / Local LLM


```text

[ Windows PC ]                                      [ Linux PC ]
+-------------------+                              +----------------------+
|  Claude Desktop   |                              |   Rosbridge Server   |
|        |          |                              |   (Port 9090)        |
|  (MCP Client)     |                              |        |             |
|        v          |      Network Connection      |        v             |
|  MCP Server       |============================> |  ROS 2 Environment   |
|  (Python/JS)      |       (WebSocket/JSON)       |  (Gazebo / Nav2)     |
+-------------------+                              +----------------------+

```

---


