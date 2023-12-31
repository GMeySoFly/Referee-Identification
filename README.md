# Referee-Identification
Computer Vision Final Project Objective - Referee Identification

Note: PyCharm was the Python editor used for this project. This is due to it friendly UI and its ability to easily install Python packages.

Prior to running the script, install the following Python Packages:
    1) cv2box
    2) numpy

Ensure that the mp4 recordings and images supplied with the code are part of the same root in the project tree. Otherwise, the video can not open.

Below are the shirt color HSV values needed for their respective colors:

    lower_shirt_color = np.array([20,200,200]) #Low HSV Values for Yellow
    upper_shirt_color = np.array([90,255,255]) #High HSV Values for Yellow

    lower_shirt_color = np.array([70,0,30]) #Low HSV Values for Black
    upper_shirt_color = np.array([90,50,70]) #High HSV Values for Black

    lower_shirt_color = np.array([60,140,100]) #Low HSV Values for Light Blue
    upper_shirt_color = np.array([105,255,200]) #High HSV Values for Light Blue

     The following website was used to help identify the HSV ranges: https://web.cs.uni-paderborn.de/cgvb/colormaster/web/color-systems/hsv.html
    
To make the video play at a slower rate, increase the number within the waitKey:
    if cv2.waitKey(5) & 0xFF == ord('q'): #waitKey value is in milliseconds per frame. So cv2.waitKey(1000) would be 1 second per frame
Clicking on "q" while the video or image is running will immediately close the window.

video_path = 'Recording4.mp4' #Make sure that the file is listed in the same root as the .py script.
