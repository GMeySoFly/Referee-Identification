import cv2
import numpy as np

def detect_referee(video_path):

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_shirt_color = np.array([20,200,200]) #Low HSV Values for Yellow
        upper_shirt_color = np.array([90,255,255]) #High HSV Values for Yellow

        mask = cv2.inRange(hsv_frame,lower_shirt_color, upper_shirt_color)

        edges=cv2.Canny(mask,50,150)
        contours, _ =cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(frame, contours, -1, (0,255,0), 3)

        cv2.imshow('Referee Detection', frame)

        if cv2.waitKey(5) & 0xFF ==ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

video_path = 'Recording4.mp4'
detect_referee(video_path)