## Local LLM : Ollama Desktop Configuration

PC 1 (Ollama)                    PC 2 (Linux/ROS)
┌─────────────────┐              ┌──────────────────────┐
│  Ollama Server  │◄────HTTP────►│  Script Python/ROS   │
│  localhost:11434│              │  Gazebo + Rviz       │
└─────────────────┘              └──────────────────────┘


`bash 
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
