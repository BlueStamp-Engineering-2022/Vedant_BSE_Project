Facial Recognition Door Lock:
The facial recognition door lock uses stored images of people's faces as a database to open a door lock. When the "bell" is rung, the raspberry pi takes a picture and stores the image into a bucket. The program automatically extracts a face from the newly added image and compares it with the faces stored in the dynamoDB collection. If a match is detected, the lock will open for five seconds to let the guest in. If no match is detected, the image is sent as an email to the user and the lock won't trigger.

| **Engineer** | **School** | **Area of Interest** | **Grade** |
|:--:|:--:|:--:|:--:|
| Vedant Agarwal | Mountain View Highschool | Electrical Engineering | Incoming Sophomore

![Headstone Image](https://user-images.githubusercontent.com/66533979/174888201-acb4436d-4e3d-412d-8f3d-747ebf61c085.png)



# Final Milestone
My second milestone is the combination of all my project pieces together. It includes the physical lock, arduino, and the raspberry pi. When the facial recognition code is run the code waits for an image.  When the “bell” is pressed a picture of the guest is taken and the lock uses facial recognition to compare them to people who are allowed to pass. If they match one of those people in the dynamo database then the lock unlocks and they are let through. If a new guest is at the door then the code states the arrival of a new guest and alerts me by sending an email. 

[![Final Milestone](https://i3.ytimg.com/vi/gFGa062yHeE/maxresdefault.jpg)](https://www.youtube.com/watch?v=gFGa062yHeE)

# First Milestone

My first milestone was setting up and hooking up the Raspberry Pi and all the necessary components onto my tv. I added the SD card and camera to the raspberry pi and installed the OS as well to finish setting it up. After that I installed necesarry libraries and packages such as OpenCV and Boto3. After I finished a large part of setting up the AWS I moved on to hardware. I built the lock using the 3d printed parts, a servo, and an arduino. The arduino controls the servo which spins a gear and turns the lock. 

[![First Milestone](https://i3.ytimg.com/vi/8Fhbh7BDEjU/maxresdefault.jpg )](https://www.youtube.com/watch?v=8Fhbh7BDEjU "First Milestone")

 ![image](https://user-images.githubusercontent.com/66533979/176495001-1fa68a17-369a-4858-9d6f-eea62105b61b.png)



# Starter Project 
My starter project was the TV-B-GONE. The components include IR LEDS, a microcontroller, button, batteries, transistors, and controllers for the LEDs. The device works when the IR LEDs are activated which sends out pulsing IR signals. TVs are programmed to detect certain patterns which tell them different commands. The TV B GONE just emits the IR patterns for power control which is what turns the TV off.

[![Starter Project](https://i3.ytimg.com/vi/J4jJOibp8ZE/maxresdefault.jpg)](https://www.youtube.com/watch?v=J4jJOibp8ZE)
