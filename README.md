# HoyaHacks24

Check out the project we did for HoyaHacks 2024:
https://devpost.com/software/scout-campus-security

<h2>Description</h2>
Scout is Hackathon project we built with goal of tackling the demand and need for campus security in the form of an inexpensive, mobile emergency alert system. Scout autonomously navigates campus while paying attention to its surroundings through a camera, GPS, and a microphone. The camera uses a deep learning machine learning model to process the visual data into a depth map. Using the depth map and a handful of filters, we designed a probabilistic algorithm that helps Scout identify obstacles as it traverses from one GPS waypoint to the next

<h2>Parts of the Project:</h2>
<h4>React Native Mobile App</h4>-> under directory client/
<h4>Go Web Server</h4>-> under directory server/
<h4>Python Autonomous Robot Code</h4>-> under directory robot/
<h4>Speech recognition</h4>
->under wake_word_NEW/
<hr>

<h3>To run the server:</h3>
<code>
cd server/
build go
./server
cd ..
</code>

<h3>To run the robot code:</h3>
<code>
1) cd robot/
2) python robot.py
</code>
<hr>

<h3>Python Requirements:</h3>
gpiozero==2.0
matplotlib==3.6.3
numpy==1.24.2
perlin_noise==1.12
pygame==2.1.2
pyserial==3.5
Requests==2.31.0
scipy==1.12.0
SpeechRecognition==3.10.1
torch==2.1.2
