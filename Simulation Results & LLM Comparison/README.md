# Simulation Results & LLM Comparison
We will ask the chatbot to perform the same actions on two different LLMs: ChatGPT and Claude.  
First, we instruct the robot to move to a specific position using coordinates. 
AAnd after moving forward 10 meters, it must be able to plot a path that avoids the walls. 

## Claude Simulation 

<img width="1319" height="707" alt="image" src="https://github.com/user-attachments/assets/792f7a2e-f82c-4127-bfb9-8a7e4a040d8f" />
<img width="1291" height="685" alt="image" src="https://github.com/user-attachments/assets/97bf8532-2747-47a6-a39c-b568fe65d462" />
<img width="1304" height="390" alt="image" src="https://github.com/user-attachments/assets/8a2c2ee7-195e-467c-a997-af2c4b88e16d" />


<img width="1600" height="900" alt="WhatsApp Image 2026-05-22 at 11 11 37" src="https://github.com/user-attachments/assets/e1c61a76-ddfd-47ff-80ef-6d1879071845" />
<img width="1600" height="900" alt="WhatsApp Image 2026-05-22 at 11 10 35" src="https://github.com/user-attachments/assets/82e0da2c-7e67-4786-8331-cc3dba07796a" />

<img width="1366" height="718" alt="image" src="https://github.com/user-attachments/assets/937e0c95-97af-4e67-b0a5-89b92e058dea" />
<img width="1314" height="520" alt="image" src="https://github.com/user-attachments/assets/d8fe3bdd-4170-448a-b435-0cf0ba0da8a0" />
<img width="1309" height="629" alt="image" src="https://github.com/user-attachments/assets/bd9629eb-fc81-43d2-b5e3-1124d505ff86" />

<img width="1600" height="900" alt="WhatsApp Image 2026-05-22 at 11 10 35" src="https://github.com/user-attachments/assets/82e0da2c-7e67-4786-8331-cc3dba07796a" />
<img width="1600" height="900" alt="WhatsApp Image 2026-05-22 at 11 27 45" src="https://github.com/user-attachments/assets/1052c520-3aca-4ab9-8e57-8aec4aa13dfe" />
Here, the robot paused halfway through the journey before resuming its journey to reach its final destination 
<img width="1600" height="900" alt="WhatsApp Image 2026-05-22 at 11 27 13" src="https://github.com/user-attachments/assets/2c0e625d-1941-4a20-adcf-22645fd800fc" />



--- 

## Chat GPT Simulation 

<img width="1218" height="470" alt="image" src="https://github.com/user-attachments/assets/165c43d5-3459-4314-a43d-0ffd2ee33cb6" />
<img width="1253" height="761" alt="image" src="https://github.com/user-attachments/assets/b0edc5d2-7ae5-49bd-9768-f8957420d264" />

<img width="1600" height="900" alt="WhatsApp Image 2026-05-22 at 12 27 29" src="https://github.com/user-attachments/assets/cda1a5cf-ad2f-4234-bd86-91adfbbe7311" />
<img width="1600" height="900" alt="WhatsApp Image 2026-05-22 at 12 26 58" src="https://github.com/user-attachments/assets/0bd45e14-7a09-4952-a673-04ca428c0407" />




# Conclusion 
It is truly difficult to get a simulation where everything works perfectly right out of the box, whether you are using ChatGPT or Claude. After running several simulations to optimize performance, I noticed that you must explicitly specify the robot's initial starting position; otherwise, it throws a TF (Transform) error. Furthermore, you have to instruct it to use Nav2, as it would sometimes clip or go through walls without it. Since implementing this, that specific issue has been resolved.

However, during many of these simulation runs—as shown above—the robot frequently claims it has arrived at its destination when it hasn't actually moved, or it only completes half of the path. When pointed out, it does correct its mistake, but this troubleshooting process takes a significant amount of time and defeats the purpose of it being autonomous.

This is just one example among many; Claude is more comprehensive in its explanations and procedures, but it is slower.
