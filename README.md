# FaceTrackingRobot
<<FaceDetect.py>>
(1)FaceDetect.py is used to process the image received by IP Webcam
 (2)FaceDetect uses openCv for face detction and sends corresponding command to esp32's server

<<WebServer>>
(1) WebServer initiates server on port 80 and recevies request on that port
(2) According to the made request ESP32 and L239d(Motor Driver Ic) controls the bot  
