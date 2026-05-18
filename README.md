# Internship schedule 

#### PC linux :
Ubuntu 22.04, ROS 2 Jazzy  
Installtion of Gazebo Harmonic (verison 8), Rviz (version 14.1.20.) and Rosbridge (version 2.6.0)  
IP address (command :  hostname -I) : 192.168.10.108  
Rosbridge WebSocket server started on port 9090  

#### PC Windows :
Installation of LLM --> Claude Desktop


```text
[ PC Windows ]                                     [ PC Linux ]
+-------------------+                              +----------------------+
|  Claude Desktop   |                              |  Rosbridge Server    |
|        |          |                              |  (Port 9090)         |
|  (Client MCP)     |                              |        |             |
|        v          |      Connexion Réseau        |        v             |
|  Serveur MCP      |============================> |  Environnement ROS 2 |
|  (Python/JS)      |   (WebSocket/JSON)           |  (Gazebo / Nav2)     |
+-------------------+                              +----------------------+
```

---


