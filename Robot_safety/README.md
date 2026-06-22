# Robot safety 

We are going to create a new Python script (a ROS node) to add to the robot's communication process. This is a way to limit the robot's commands to prevent it from acting in a dangerous manner in the event of a problem. 

### Structure 
**Without security**  
```text
[ Your AI / MCP ]  ───(Direct command)───>  [ Robot Motors ]    ❌ (Dangerous)
 ```

**Safely**

```text
[ Your AI / MCP ] 
       │
       ▼ (Raw requested speed)
 [ Your Safety Script ]  <─── (Checks max limits and STOP button)
       │
       ▼ (Validated or corrected speed)
 [ Robot Motors ] 
       ▲
 [ Telemetry / Robot state ] (Checks battery, obstacles...)

 ```



### What will this Python file do?  
This script will perform three main tasks:  

**The speed “saturator”:** If the AI instructs the robot to move at a linear speed of $v_x = 3.0\text{ m/s}$, the script will intercept the message, then check if it exceeds the safety limit (e.g., $0.5\text{ m/s}$), and automatically adjust the value to $0.5\text{ m/s}$ before sending it to the robot.  

**The Watchdog:** If the connection with the AI suddenly drops while the robot is moving, the robot risks continuing straight ahead indefinitely. The script will check every second to see if it is receiving a signal from the AI. If the AI “stops communicating,” the script immediately issues an emergency stop command ($0\text{ m/s}$).  

**Status Management (Battery / Obstacles):** The script can read the battery status. If it drops below 15%, it can block the AI’s movement commands and force the robot to stop.


