# Summary of the Situation and Constraints in the Nav2 Architecture / Security

The aim was to develop and test a ROS 2 safety node (robotnik_safety_filter, coded in safety_node.py) responsible for monitoring the robot’s speed commands and other safety rules. 
I wanted the robot to intercept movement commands that were too high and apply a strict limit of $0.4\text{ m/s}$, thereby ensuring its physical safety.


Following the instructions in the *Robotnik development manual*, I realised that I shouldn’t modify any files within the robot’s interface. I therefore created a folder alongside it, allowing me to modify or create files that the robot will be able to access.  



### The problem encountered 
In autonomous navigation (Nav2): As soon as a position target (goal_pose) was sent to the Nav2 autonomous stack, the robot completely ignored the $0.4\text{ m/s}$ limit, moved at its nominal speed ($0.47\text{ m/s}$ to $0.6\text{ m/s}$), and the filter terminal remained completely silent. Nothing was intercepted.  

**Explanation:**
During our initial tests, I configured the safety filter (robotnik_safety_filter) in isolation: it waited for messages on a neutral topic (such as /cmd_vel_raw) to apply the speed limit of $0.4\text{ m/s}$.
However, dynamic analysis of the ROS 2 graph showed that in the simulation’s factory architecture, the Nav2 autonomous navigation node sent its commands directly to the multiplexer’s official input topic: /robot/robotnik_base_control/cmd_vel. 
The twist_mux node received this stream in real time and relayed it directly to the motors in Gazebo, with no intermediate filter to stop it. 
Since using Nav2 is mandatory during simulations to prevent the robot from colliding with obstacles, my safety filter was completely bypassed.To resolve this, I tried to insert our filter by modifying the launch file (safety_launch.py) and applying topic remappings. 
However, because the factory configuration of the robot's multiplexer was hardwired to the original topics, the ROS 2 graph did not route the commands through my filter. The virtual robot’s drive base remained firmly and directly connected to Nav2.  


**Solution:**
I’m now going to try out a new method: inserting our filter directly into the robot’s multiplexing node (twist_mux) and assigning it a higher priority.

