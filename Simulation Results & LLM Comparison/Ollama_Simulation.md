## Ollama Simulation

With this code in the file:  
```cmd
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from nav2_msgs.action import NavigateToPose
from geometry_msgs.msg import PoseStamped
import requests
import json

OLLAMA_URL = "http://192.168.10.106:11434/api/chat"
MODEL = "llama3.2"

SYSTEM_PROMPT = """
You are an assistant that controls a ROS2 robot in a simulation.
When the user gives you a navigation instruction, you must respond ONLY in JSON, with no text around it.
Response format:
{
  "action": "navigate",
  "x": 0.0,
  "y": 0.0,
  "description": "short explanation"
}
The STRICT map limits are:
- x between -18.0 and +18.0
- y between -15.0 and +15.0
Never exceed these limits!
Examples:
- "go to the center" -> x=0.0, y=0.0
- "go to the top right" -> x=10.0, y=8.0
- "go to the bottom left" -> x=-10.0, y=-8.0
- "go up" -> x=0.0, y=8.0
- "go right" -> x=10.0, y=0.0
If the user says "stop", respond with:
{"action": "stop", "x": 0.0, "y": 0.0, "description": "stop"}
"""

class RobotOllamaNode(Node):
    def __init__(self):
        super().__init__('robot_ollama_node')
        self.nav_client = ActionClient(self, NavigateToPose, 'robot/navigate_to_pose')
        self.conversation = []
        print("Robot Ollama Node started!")
        print("You can talk to the robot in English.")
        print("Type 'quit' to stop.\n")

    def ask_ollama(self, user_input):
        self.conversation.append({"role": "user", "content": user_input})
        payload = {
            "model": MODEL,
            "messages": [{"role": "system", "content": SYSTEM_PROMPT}] + self.conversation,
            "stream": False
        }
        response = requests.post(OLLAMA_URL, json=payload)
        result = response.json()
        reply = result["message"]["content"]
        self.conversation.append({"role": "assistant", "content": reply})
        return reply

    def send_goal(self, x, y):
        goal_msg = NavigateToPose.Goal()
        goal_msg.pose = PoseStamped()
        goal_msg.pose.header.frame_id = "robot_map"
        goal_msg.pose.pose.position.x = x
        goal_msg.pose.pose.position.y = y
        goal_msg.pose.pose.orientation.w = 1.0
        self.nav_client.wait_for_server()
        self.nav_client.send_goal_async(goal_msg)
        print(f"Navigating to x={x}, y={y} !")

    def run(self):
        while True:
            user_input = input("\nYou: ")
            if user_input.lower() == "quit":
                print("Goodbye!")
                break
            print("Ollama is thinking...")
            reply = self.ask_ollama(user_input)
            print(f"Ollama: {reply}")
            try:
                command = json.loads(reply)
                if command["action"] == "navigate":
                    print(f"-> {command['description']}")
                    self.send_goal(command["x"], command["y"])
                elif command["action"] == "stop":
                    print("-> Robot stopped")
            except:
                print("(non-JSON response — no command sent)")

def main():
    rclpy.init()
    node = RobotOllamaNode()
    node.run()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
```

By executing this command: **va en bas à gauche**
<img width="1600" height="900" alt="WhatsApp Image 2026-05-26 at 17 04 50" src="https://github.com/user-attachments/assets/08cc4015-6f29-4407-b05d-87691f833738" />

We get : 
<img width="1600" height="900" alt="WhatsApp Image 2026-05-26 at 17 04 50" src="https://github.com/user-attachments/assets/09edde4b-48cb-4e3d-b77a-31988a94fbd9" />

By executing this command: **va en haut à droite**
<img width="1600" height="900" alt="WhatsApp Image 2026-05-26 at 17 08 07" src="https://github.com/user-attachments/assets/53f238d3-18aa-415d-b1f2-e2fdb5465567" />


