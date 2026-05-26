# Simulation Results & LLM Comparison
We will ask the chatbot to perform the same actions on two different LLMs: ChatGPT and Claude.  
First, we instruct the robot to move to a specific position using coordinates. 
AAnd after moving forward 10 meters, it must be able to plot a path that avoids the walls. 



--- 




# Conclusion 
It is truly difficult to get a simulation where everything works perfectly right out of the box, whether you are using ChatGPT or Claude. After running several simulations to optimize performance, I noticed that you must explicitly specify the robot's initial starting position; otherwise, it throws a TF (Transform) error. Furthermore, you have to instruct it to use Nav2, as it would sometimes clip or go through walls without it. Since implementing this, that specific issue has been resolved.

However, during many of these simulation runs—as shown above—the robot frequently claims it has arrived at its destination when it hasn't actually moved, or it only completes half of the path. When pointed out, it does correct its mistake, but this troubleshooting process takes a significant amount of time and defeats the purpose of it being autonomous.

This is just one example among many; Claude is more comprehensive in its explanations and procedures, but it is slower.

I think we'll need to change some settings to improve performance. 


All the information are here : https://docs.google.com/spreadsheets/d/1-6duBYCitYhOyMOqxkJYvgAtaIOxp_dguyQsaNE2UYo/edit?gid=0#gid=0
