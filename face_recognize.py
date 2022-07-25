import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier('haar_face.xml')

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
features = np.load("features.npy", allow_pickle=True)
labels = np.load("labels.npy")

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('trained_face.yml')

img = cv.imread(r'D:\opencv\fcc\faces\val\jerry_seinfeld\3.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Person", gray)

faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)
for (x, y, w, h) in faces_rect:
  faces_roi = gray[y:y+h, x:x+w]

  label, confidence = face_recognizer.predict(faces_roi)
  print(f'Person is {people[label]} with {confidence} confidence')