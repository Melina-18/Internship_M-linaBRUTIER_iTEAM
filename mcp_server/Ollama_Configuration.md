## Local LLM : Ollama Desktop Configuration

```text
PC 1 (Windows - Ollama)                    PC 2 (Linux - ROS)
┌─────────────────┐              ┌──────────────────────┐
│  Ollama Server  │◄────HTTP────►│  Script Python/ROS   │
│  localhost:11434│              │  Gazebo + Rviz       │
└─────────────────┘              └──────────────────────┘
```

All control and routing are handled from the Linux PC.  
The Windows PC is used solely to run the Ollama engine because it didn't have enough RAM to run Ollama AND an interface at the same time. 

#### 1. Ollama installation
- llama3.2 : Main model (lightweight)  
- llama3 : Secondary model (more accurate)  

#### 2. Ollama Configuration  
By default, Ollama only listens on localhost. You need to configure it to accept connections from the local network.
```cmd
$env:OLLAMA_HOST="0.0.0.0:11434"
ollama serve
```

#### 3. Installation on a Linux PC  
```bash
sudo apt install curl -y
sudo apt install python3 -y
sudo apt install python3-requests -y
```

#### 4. Test 
```bash
import requests

response = requests.post(
    "http://192.168.10.106:11434/api/chat",
    json={
        "model": "llama3.2",
        "messages": [{"role": "user", "content": "Dis bonjour en français"}],
        "stream": False
    }
)

print(response.status_code)
print(response.text)
```

**Run the test:**
```bash
python3 test_ollama.py
```

#### 5. Configuration Ollama on a ROS2 node

