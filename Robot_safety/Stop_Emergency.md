# Stop Emergency 

I add stop emergency at the security filter. 


When i execute this command : 
```bash 
ros2 topic pub /robot/safety_filter/emergency_stop std_msgs/msg/Bool "data: true" --once
```

The result : 
The robot stops immediately 
<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/5ca7f451-8367-420e-87d4-045902be610c" />



To launch again the filter : 
I execute this command : 
```bash 
ros2 topic pub /robot/safety_filter/emergency_stop std_msgs/msg/Bool "data: false" --once
```
