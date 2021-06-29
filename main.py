import cv2 
import mediapipe as mp 

mp_drawing = mp.solutions.drawing_utils 
mp_holistic = mp.solutions.holistic

cam = cv2.VideoCapture(1) 

with mp_holistic.Holistic(min_detection_confidence = 0.5, min_tracking_confidence = 0.5) as holistic:
    while True:
        _, frame = cam.read()
        cv2.imshow("Camera feed", frame)
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = holistic.process(image)
        
        if cv2.waitKey(1) & 0xff == ord('q'):
            break 

cam.release()
cv2.destroyAllWindows()