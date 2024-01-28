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

<h3>To run the server:<h3>
1) cd server/
2) build go
3) ./server
4) cd ..

<h3>To run the robot code:<h3>
1) cd robot/
2) python robot.py
