import cv2
from deepface import DeepFace
import numpy as np


face_cascade = cv2.CascadeClassifier('C://Users//DELL//PycharmProjects//OpencvPython//harass//haarcascade_frontalface_dafault.xml')


video = cv2.VideoCapture(0)

while video.isOpened():
    _, frame = video.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    Face = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    
    for x,y,w,h in Face:
        img=cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 1)
        try:
            analyze = DeepFace.analyze(frame, actions=['emotion'])
            print(analyze['dominant_emotion'])
        except:
            print("no face")
            
    
    cv2.imshow('video', frame)
    key=cv2.waitKey(1)
    if key == ord('q'):
 
        break            

video.release()


'''

imgpath = "C:\Coding\Python Projects\s.jpg"
image = cv2.imread(imgpath)

Analyze = DeepFace.analyze(image, actions = ['emotion']) 

#DeepFace have various emotions like age, gender, emotions, race
print(Analyze)
print(analyze['dominant_emotion'])
   '''