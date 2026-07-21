# Difference between RB-SUMMIT (simulation) and RB-THERON (physical robot )

RB-SUMMIT (simulation)  
<img width="336" height="343" alt="Robot" src="https://github.com/user-attachments/assets/857773f9-25b0-49f8-8926-befd3679834b" />

RB-THERON (physical robot)  
<img width="684" height="715" alt="rbtheron" src="https://github.com/user-attachments/assets/89f02d65-7c1e-4115-ac46-3146c655eaf7" />

First of all, it’s important to note that both robots run on the same software (ROS2, Nav2), but their architectures differ in terms of weight, linear speed, intended uses, and so on.  


### Differences in Software Architecture  
From a technical standpoint, we had noticed that on the RB-SUMMIT, an inspection of the ROS2 graph revealed the absence of a twist_mux node to send the final commands to the robot.  

However, on the RB-THERON, there is a twist_mux node that allows us to prioritize the actions sent to the robot and thus control those actions in a highly secure manner.  

<img width="973" height="383" alt="rbtherongraphe" src="https://github.com/user-attachments/assets/c2d4f5c8-a1e2-440a-9ed5-8b1f4798477e" />

This photo shows the priorities and the control chain.  

This diagram clearly illustrates the robot’s architecture: the four sources (blue) converge on the twist_mux according to their priority—the physical pad (100) can always override autonomous navigation (20), while hardware safety signals can cut off the signal at any time. The validated command then passes through `robotnik_base_control`, which applies the native speed limit of 1.2 m/s, before reaching the motors.  


This architecture ensures the robot’s safety because the operator has various means to regain control over autonomous navigation (priority order, emergency stop).  


