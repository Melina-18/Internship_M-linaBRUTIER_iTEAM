# Simulation Results & LLM Comparison
We will ask the chatbot to perform the same actions on two different LLMs: ChatGPT and Claude.  
First, we instruct the robot to move to a specific position using coordinates. 
AAnd after moving forward 10 meters, it must be able to plot a path that avoids the walls. 



--- 

## Chat GPT Simulation 

<img width="1218" height="470" alt="image" src="https://github.com/user-attachments/assets/165c43d5-3459-4314-a43d-0ffd2ee33cb6" />
<img width="1253" height="761" alt="image" src="https://github.com/user-attachments/assets/b0edc5d2-7ae5-49bd-9768-f8957420d264" />
<img width="1236" height="662" alt="image" src="https://github.com/user-attachments/assets/342c3a0e-21f8-4d89-9db7-4be8f3a91202" />
<img width="1202" height="499" alt="image" src="https://github.com/user-attachments/assets/b67c91ab-ca7e-4c25-8641-aabc5afca68d" />
<img width="1221" height="524" alt="image" src="https://github.com/user-attachments/assets/cc39e692-ff9d-4a8b-8cc1-c27be9f68759" />
<img width="1288" height="630" alt="image" src="https://github.com/user-attachments/assets/320b810a-9d1e-40c8-8d62-7bebdeba6022" />

<img width="1600" height="900" alt="WhatsApp Image 2026-05-22 at 12 27 29" src="https://github.com/user-attachments/assets/cda1a5cf-ad2f-4234-bd86-91adfbbe7311" />
<img width="1600" height="900" alt="WhatsApp Image 2026-05-22 at 12 26 58" src="https://github.com/user-attachments/assets/0bd45e14-7a09-4952-a673-04ca428c0407" />
<img width="1600" height="900" alt="WhatsApp Image 2026-05-22 at 12 54 44" src="https://github.com/user-attachments/assets/2c6086a3-97d1-4df9-a215-5a8a09277043" />




# Conclusion 
It is truly difficult to get a simulation where everything works perfectly right out of the box, whether you are using ChatGPT or Claude. After running several simulations to optimize performance, I noticed that you must explicitly specify the robot's initial starting position; otherwise, it throws a TF (Transform) error. Furthermore, you have to instruct it to use Nav2, as it would sometimes clip or go through walls without it. Since implementing this, that specific issue has been resolved.

However, during many of these simulation runs—as shown above—the robot frequently claims it has arrived at its destination when it hasn't actually moved, or it only completes half of the path. When pointed out, it does correct its mistake, but this troubleshooting process takes a significant amount of time and defeats the purpose of it being autonomous.

This is just one example among many; Claude is more comprehensive in its explanations and procedures, but it is slower.

I think we'll need to change some settings to improve performance. 


All the information are here : https://docs.google.com/spreadsheets/d/1-6duBYCitYhOyMOqxkJYvgAtaIOxp_dguyQsaNE2UYo/edit?gid=0#gid=0
