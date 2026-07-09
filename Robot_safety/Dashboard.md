# SAFETY FILTER DASHBOARD 

I created this dashboard to track my robot's progress using precise data.  

Here you can see my robot's linear and angular speeds, as well as whether or not the robot is in emergency stop mode. 
Within the simulation, I can't include its battery charge, but that will be the next goal when I move on to the actual robot.   

I've configured the dashboard so that it refreshes every 5 seconds.   

Here we verify that the **emergency stop** is displayed correctly, which it is:  
<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/6ebeabaf-bef0-4ce2-a9a7-880462ccec91" />
<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/f4d35bc0-dc2f-46b7-9b12-f0b74e8a67e7" />
And then he takes her away :  
<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/71e7a564-058a-47be-8f5b-dac153e43ad0" />
<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/c953b288-9185-44c5-a590-608516be74b6" />

----

Now let's test the **linear and angular speeds**. 
When the robot was moving, the dashboard correctly displayed its speed :     
<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/6f519030-9597-46fe-a8fe-f65b2640266f" />

And then the robot stopped because I had told it to move forward 5 meters :   
<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/6bc57464-0641-4826-9c03-592ec6239c3f" />




---

Problems encountered: 
Sometimes during these tests, the robot moved jerkily and at a very, very slow speed. After doing some research, I concluded that the problem was caused by the machine’s CPU load, which was causing the jerkiness. To resolve this, restarting the PC or closing RviZ was the best solution for continuing my simulations. 











