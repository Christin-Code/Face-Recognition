The system is developed for deploying an easy and a secure way of taking down attendance. The software first captures an image of all the authorized persons and stores the information into database. The system then stores the image by mapping it into a face coordinate structure. Next time whenever the registered person enters the premises the system recognizes the person and marks his attendance along with the time. It maybe a webcam or any other attached camera. We use these to get the camera video input to our system. We then use the video data to manipulate and recognize faces in real time. Our system works as follows:
 The user needs to start the system in Pycharm.
 Now the system accepts camera input with the help of Python packages.
 We now set some parameters and start live detection using the video input.
 Our system works and manipulates live video data to identify faces in it.
 Next step is to store these faces based on a matrix form.
 Once faces are recognized and stored we can now detect them.
 Whenever the face reappears it is recognized by name in a real time video and an attendance is marked for that particular person in the database.
The project is developed using Python language and is supported by a Firebase database to store user specific details.



Modules of the project
Facial recognition login - the login and the attendance is marked through the facial recognition
Login through credentials- if the particular user is not able to login with the facial recognition he can use his unique credentials 
Attendance management 
Keeps track of the late coming and permissions 
Admin management - adding new user and authorization to make attendance manually 
