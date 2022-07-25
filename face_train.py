import os
from typing import Tuple
import cv2 as cv
import numpy as np


haar_cascade = cv.CascadeClassifier('haar_face.xml')

def create_train(DIR: str, people: list) -> Tuple[list, list]:
  features = []
  labels = []
  for person in people:
    path = os.path.join(DIR, person)
    label = people.index(person)
    for img in os.listdir(path):
      img_path = os.path.join(path, img)

      img_array = cv.imread(img_path)
      gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

      faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

      for (x, y, w, h) in faces_rect:
        faces_roi = gray[y:y+h, x:x+w]
        features.append(faces_roi)
        labels.append(label)
  return (features, labels)


if __name__ == "__main__":

  people = []
  DIR = r'D:\opencv\fcc\faces\train'
  for i in os.listdir(DIR):
    people.append(i)

  features, labels = create_train(DIR, people)
  print(f"Initialized training set.")
  features, labels = np.array(features, dtype="object"), np.array(labels)

  face_recognizer = cv.face.LBPHFaceRecognizer_create()
  face_recognizer.train(features, labels)

  face_recognizer.save("face_trained.yml")
  np.save("face_features.npy", features)
  np.save("face_labels.npy", labels)






