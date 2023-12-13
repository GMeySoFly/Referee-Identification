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

        result_frame, roi = process_frame(frame)
        cv2.imshow('Referee Detection', result_frame)

        if cv2.waitKey(1000) & 0xFF == ord('q'): #waitKey value is in millisconds per frame
            break

    cap.release()
    cv2.destroyAllWindows()

def process_frame(frame):
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_shirt_color = np.array([20, 200, 200])  #Low HSV Values for Yellow
    upper_shirt_color = np.array([100, 255, 255])  #High HSV Values for Yellow

    mask = cv2.inRange(hsv_frame, lower_shirt_color, upper_shirt_color)

    edges = cv2.Canny(mask, 50, 150)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    filtered_contours = filter_contours(contours, min_area=10)

    if filtered_contours:
        referee_contour = max(filtered_contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(referee_contour) #Allows for bounding box to be around the contour
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), 3) #Black Rectangle
        roi = frame[y:y + h, x:x + w]
    else:
        roi = None

    return frame, roi

def filter_contours(contours, min_area):
    return [cnt for cnt in contours if cv2.contourArea(cnt) > min_area]

video_path = 'Recording4.mp4'
detect_referee(video_path)