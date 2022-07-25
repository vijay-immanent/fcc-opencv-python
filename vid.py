import cv2 as cv


def show(capture, title="Video", on_frame=None):
  while True:
    isTrue, frame = capture.read()
    
    if (on_frame != None):
      on_frame(frame)
    
    if isTrue:
      cv.imshow(title, frame)
    
    if cv.waitKey(20) & 0xff == ord('d'):
      capture.release()
      break
