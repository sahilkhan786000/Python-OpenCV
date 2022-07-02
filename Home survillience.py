import argparse
import os
from datetime import datetime

import cv2

face_cascade = cv2.CascadeClassifier("C://Users//DELL//PycharmProjects//OpencvPython//harass//haarcascade_frontalface_default.xml")

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    if frame is not None:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10)
        for x, y, w, h in faces:
            img = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            exact_time = datetime.now().strftime('%Y-%b-%d-%H-%S-%F')
            cv2.imwrite('Face detected'+str(exact_time)+'.jpg', img)
        cv2.imshow("Home surv", frame)
        key = cv2.waitKey(1)

        if key == ord('q'):
            ap = argparse.ArgumentParser()
            ap.add_argument("-ext", "--extension", required=False, default='.jpg')
            ap.add_argument("-ext", "--extension", required=False, default='output.mp4')
            args = vars(ap.parse_args())

            dir_path = "."
            ext = args['extension']
            output = args['output']

            image = []

            for f in os.listdir(dir_path):
                if f.endswith(ext):
                    image.append(f)

            image_path = os.path.join(dir_path, image[0])
            frame = cv2.imread(image_path)
            height, width, channels = frame.shape

            f = cv2.VideoWriter_fourcc(*'mp4v')
            out = cv2.VideoWriter(output, f, 5.0, (width, height))

            for t in image :
                image_path = os.path.join(dir_path, t)
                frame = cv2.imread(image_path)
                out.write(frame)

            break

video.release()
cv2.destroyAllWindows()
