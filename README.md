# multithreadedObjectDetectionFromIPCam
A multithreaded object detection cnn, using inception_v2 and tensorflow, along with openCV, with input from IPCam

## To Use:  

1. Follow the steps here to download all system dependencies, create a python virtual environment, and compile/install openCV. This tutorial also walks you through installing keras, a higher level tensorflow wrapper, which is not needed for this project, but there is no harm in installing keras.  
https://www.pyimagesearch.com/2017/09/25/configuring-ubuntu-for-deep-learning-with-python/  

2. Download this repository, which is largely based on:  
https://github.com/datitran/object_detector_app and https://towardsdatascience.com/building-a-real-time-object-recognition-app-with-tensorflow-and-opencv-b7a2b4ebdc32  

3. Install tkinter for python3 to use the tkinter GUI

4. Download the IPCam Android app onto your Android phone, and start the IPCam server  

5. Run the object_detection_multithreading.py script (using workon dl4cv) with arguments:  
    IP addr and port of the IPCam server --source/-src='0.0.0.0:8080'  
    IP addr of the client, destination computer --destination/-des='0.0.0.0'  
    Width of the frames in the video stream --width=480  
    Height of the frames in the video stream --height=360  
    Number of workers --num-workers=2  
    Size of the queue --queue-size=5  
    
6. Run the receiver.py to listen to the correct IP address and show the object detection output with arguements:  
    IP addr of the computer broadcasting the object recognition images -src='0.0.0.0'
    
7. Run gui.py to display the object detection stream in a tkinter gui for easy editing

## Copyright

See [LICENSE](LICENSE) for details.
Copyright (c) 2017 [Dat Tran](http://www.dat-tran.com/).
