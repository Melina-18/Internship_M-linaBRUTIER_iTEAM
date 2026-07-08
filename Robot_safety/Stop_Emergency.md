# Stop Emergency 

I add stop emergency at the security filter.   

The safety filter has been activated; I'm going to send a command to the robot to move forward. 
<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/20cb07c1-ac59-4f6c-b61b-4fd783f5b882" />


When i execute this command in a new terminal :   
```bash 
ros2 topic pub /robot/safety_filter/emergency_stop std_msgs/msg/Bool "data: true" --once
```

The result :  
The robot stops immediately   
<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/6ee03df0-0d0c-455b-bdbd-39ca79f2547c" />



To launch again the robot, I execute this command :   
```bash 
ros2 topic pub /robot/safety_filter/emergency_stop std_msgs/msg/Bool "data: false" --once
```

The result :  
<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/73aa546f-c55f-42d5-9eb4-c77444e1e01c" />
<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/0ade8986-b518-4c14-b8ce-fe62a8897391" />

The robot continued moving forward and stopped just before the wall 


