import cv2 as cv
import plt
import vid
import img

def rescaleFrame(frame, scale=0.75):
  width = int(frame.shape[1] * scale)
  height = int(frame.shape[0] * scale)
  dimensions = (width, height)

  return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def demo_rescale_image():
  img = cv.imread('photos/cat_large.jpg')
  plt.image(121, img, "ORIGINAL")
  scaled_down_img = rescaleFrame(img, 0.3)
  plt.image(122, scaled_down_img, "RESCALED")
  plt.show()

def demo_rescale_video():
  capture = cv.VideoCapture(0)
  #capture.set(3, 400)
  rescale = lambda frame : img.show(rescaleFrame(frame, 0.5), "RESCALED")
  vid.show(capture, "ORIGINAL", rescale)

if __name__ == "__main__":
  demo_rescale_video()