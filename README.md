# Internship schedule 

#### PC linux :
Ubuntu 22.04, ROS 2 Jazzy
Installtion of Gazebo Harmonic (verison 8), Rviz (version 14.1.20.) and Rosbridge (version 2.6.0)  
IP adress (command :  hostname -I) : 192.168.10.108  
Rosbridge WebSocket server started on port 9090  

#### PC Windows :
Installation of LLM --> Claude Desktop




[ PC Windows ]                                     [ PC Linux ]
+-------------------+                              +----------------------+
|  Claude Desktop   |                              |  Rosbridge Server    |
|        |          |                              |  (Port 9090)         |
|  (Client MCP)     |                              |        |             |
|        v          |      Connexion Réseau        |        v             |
|  Serveur MCP      |============================> |  Environnement ROS 2 |
|  (Python/JS)      |   (WebSocket/JSON)           |  (Gazebo / Nav2)     |
+-------------------+                              +----------------------+




---

### Méthode 2 : L'outil Mermaid de GitHub (Le plus professionnel)
GitHub intègre nativement un outil génial appelé **Mermaid** qui transforme du texte en un vrai diagramme graphique moderne, propre et coloré. 

Pour avoir un rendu visuel parfait sur GitHub, remplace le dessin par ce code :

```markdown
```mermaid
graph LR
    subgraph PC_Windows [PC Windows]
        A[Claude Desktop<br>Client MCP] --> B[Serveur MCP<br>Python/JS]
    end

    subgraph PC_Linux [PC Linux]
        C[Rosbridge Server<br>Port 9090] --> D[Environnement ROS 2<br>Gazebo / Nav2]
    end

    B == Connexion Réseau<br>WebSocket/JSON ===> C

    %% Style pour rendre le schéma joli
    style PC_Windows fill:#f9fafd,stroke:#333,stroke-width:2px
    style PC_Linux fill:#f5fdf5,stroke:#333,stroke-width:2px
