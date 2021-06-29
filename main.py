import cv2 
import mediapipe as mp 

mp_drawing = mp.solutions.drawing_utils 
mp_holistic = mp.solutions.holistic

cam = cv2.VideoCapture(1) 

while cam.isOpened():
    _, frame = cam.read()
    cv2.imshow("Camera feed", frame)

    if cv2.waitKey(0) & 0xff == ord('q'):
        break 

cam.release()
cv2.destroyAllWindows()