# Interpretation of his condition - Test 3 


We conducted a test in which we placed an obstacle behind the robot, but the LLM tells me that it didn't see the obstacle because the rear sensors aren't detecting anything. 
However, the robot suggests turning around to tell me if it sees anything, since the front sensors are working as we just saw in Test 2.

Here is a photo of the obstacle behind the robot: 
<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/2a09f801-ae1b-4b81-93e1-59bf2c406711" />


And the AI's result  
<img width="1027" height="647" alt="image" src="https://github.com/user-attachments/assets/1598fbde-118b-4271-b3d7-e1ce329f9b96" />
<img width="1033" height="374" alt="image" src="https://github.com/user-attachments/assets/fda151e6-c7fb-4348-82f2-67606c49e33d" />



Once the robot has turned, you can immediately see that it detects the obstacle because, in RViz, we can see the obstacle as soon as the robot has turned a little more than 90°. 
Before 
<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/ab487d15-6008-4cd6-8539-7342631c8484" />

After 
<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/fec528c4-7ec2-4644-97db-b8295749224f" />
<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/604dfc61-55a1-41f8-ad29-1fbed4b9b6bc" />


**Conclusion**
The robot can see everything that's happening with a field of view of about 180°; the object was in its blind spot, which is why it couldn't see it. 


