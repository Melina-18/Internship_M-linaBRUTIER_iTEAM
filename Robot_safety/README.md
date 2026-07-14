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

**The speed “saturator”:** If the AI instructs the robot to move at a linear speed of $v_x = 0.6\text{ m/s}$, the script will intercept the message, then check if it exceeds the safety limit (e.g., $0.4\text{ m/s}$), and automatically adjust the value to $0.4\text{ m/s}$ before sending it to the robot.   
The robot velocity is clamped when moving forward(0.4 m/s), backward(0.4 m/s), and rotating(0.8 rad/s).  
```text
Nav2 publishes 0.6 m/s on cmd_vel_raw
       ↓
safety filter receives the command
       ↓
filter detects 0.6 > 0.4 → replaces with 0.4
       ↓
publishes 0.4 m/s on cmd_vel
       ↓
robotnik_base_control receives 0.4 m/s → motors
 ```

**Stop Emergency :** An emergency stop feature has been built into the safety filter: by publishing ‘True’ to the /robot/safety_filter/emergency_stop topic, all motion commands are immediately blocked, and the robot continuously receives a speed of zero until a ”False" signal is published to resume control.




This safety filter only works when the robot is moving via Nav2, because it is integrated directly into the navigation pipeline—commands must pass through the filter before reaching the motors. Any command sent outside of Nav2 (direct teleoperation, raw command via `cmd_vel`) will not pass through this filter and therefore will not be speed-limited.
