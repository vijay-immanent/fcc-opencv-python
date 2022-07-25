import cv2 as cv
from img import show

img = cv.imread("photos/group 1.jpg")
# show(img, "RGB")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# show(gray, "GRAY")  

haar_cascade = cv.CascadeClassifier("haar_face.xml")

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)
print(f'{len(faces_rect)} face(s) found.')

for (x, y, w, h) in faces_rect:
  cv.rectangle(img, (x,y), (x+w, y+h), (50, 20, 230), 3)

show(img, "FACE DETECTED")
cv.waitKey(0)