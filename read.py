import cv2 as cv

# reading images
# img = cv.imread("photos/cat.jpg")
# cv.imshow("Cat", img)
# cv.waitKey(0)

# reading videos
capture = cv.VideoCapture("videos/dog.mp4")
while True:
  isTrue, frame = capture.read()
  if isTrue:
    cv.imshow("Video", frame)
  if cv.waitKey(20) & 0xff == ord('d'):
    break
capture.release()

cv.destroyAllWindows()
