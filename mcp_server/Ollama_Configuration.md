## Local LLM : Ollama Desktop Configuration

PC 1 (Ollama)                    PC 2 (Linux/ROS)
┌─────────────────┐              ┌──────────────────────┐
│  Ollama Server  │◄────HTTP────►│  Script Python/ROS   │
│  localhost:11434│              │  Gazebo + Rviz       │
└─────────────────┘              └──────────────────────┘
<img width="1377" height="586" alt="image" src="https://github.com/user-attachments/assets/b2e5b8e4-cd0d-43f3-a96b-bec208c7a784" />
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

```json
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

