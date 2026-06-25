# Simultaneous command 

We're going to try giving the robot a series of commands to see how it performs. 



**Simulation**  
Here is the command for the robot : *"Use nav2 and move the robot forward 4 m, then 3 m to the left, then turn 9 degrees, and move forward 10 m"*

<img width="1011" height="649" alt="image" src="https://github.com/user-attachments/assets/be8e2320-3c42-415f-af06-f72259424672" />

<img width="1245" height="872" alt="image" src="https://github.com/user-attachments/assets/22643fe6-aceb-4284-abb9-f015ce856361" />

<img width="1090" height="738" alt="image" src="https://github.com/user-attachments/assets/c215b20d-6c93-451d-9645-e2f7ec878b59" />

The robot moved 2 meters straight ahead and then turned slightly to the left to reach position (4,3); the robot does not go all the way to the first position—it heads directly to the second one.  
The robot hadn't finished its path, so I told it to, and it moved forward:  
<img width="818" height="549" alt="image" src="https://github.com/user-attachments/assets/158ef0ae-ad6a-42a6-a5b6-7580bb14f009" />
The robot followed its path correctly, and it even hit its speed limit because I think the cruising speed set by nav2 is higher than my speed limit of 0.4 m/s. 



The result : 
