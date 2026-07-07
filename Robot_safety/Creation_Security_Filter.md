# Creation of the security filter 

I tried one last method to configure the safety filter with a speed limit of 0.4 m/s, and it worked perfectly. 

I decided to create my own ROS2 package (mcp_robot_safety) so I wouldn't have to modify the robot's code. 
I used the nav2_task.launch.py launch file, modifying only the cmd_vel remappings, which are now redirected to an intermediate topic (cmd_vel_raw). 
The original file from the Robotnik package has not been modified, deleted, or overwritten—it remains intact in the `install/` directory, as specified in the Robotnik documentation. 
A new launch file, located in a new package, is used instead of the original when the system is launched.


One thing to note about this filter is that we have to use nav2 for it to work, but that's not a problem because that's the command that allows our robot to avoid walls. 
Next, we'll try to configure the LLM so that it uses only the “nav2” navigation mode, since up until now it has been prioritizing the mode that is most appropriate based on the command. 



Filter launch : 
```bash 
cd ~/myws
colcon build --packages-select mcp_robot_safety
source install/setup.bash
ros2 launch mcp_robot_safety safety_navigation.launch.py      #remplaces the : ros2 launch robotnik_simulation_navigation navigation.launch.py
```

In the Terminal, you can see that the filter has indeed been started : 
<img width="768" height="448" alt="image" src="https://github.com/user-attachments/assets/3761758b-f6ee-4ca5-bbae-301f85905fde" />


Tests Conducted :  
I simply asked the robot to move forward 5 meters at 0.8 meters per second, and it carried out this operation exactly as instructed without going through the filter or using nav2, because the LLM considers that nav is not necessary for this command. 
<img width="756" height="425" alt="image" src="https://github.com/user-attachments/assets/9985b734-847d-4a8a-b897-3e63eb83674e" />


After a rotation, we instruct the robot to use nav2, and we send the same command back to the robot:  
<img width="470" height="267" alt="image" src="https://github.com/user-attachments/assets/232bd06f-f7bf-4dc0-820b-e75901b1f2b9" />
<img width="506" height="264" alt="image" src="https://github.com/user-attachments/assets/d01b0c1e-08c8-4f2b-8d9f-b8a28b889fab" />
<img width="914" height="514" alt="image" src="https://github.com/user-attachments/assets/30037d21-1a8a-4314-973d-bafd25b6bd03" />

This time, the robot used the filter. The filter correctly displayed the applied speed limit in the terminal, and the robot moved at a maximum speed of 0.4 m/s. 




We rotate the robot, and now issue a command at normal speed, which should not be limited: 
<img width="1093" height="615" alt="image" src="https://github.com/user-attachments/assets/f40e5d14-f260-4f0c-862e-e25a911f49b9" />












