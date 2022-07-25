import cv2 as cv
import numpy as np
import plt

img = cv.imread("photos/park.jpg")
plt.image(231, img, "ORIGINAL")

# Translation
def translate(img, x, y):
  transMat = np.float32([[1, 0, x], [0, 1, y]])
  dimensions = (img.shape[1], img.shape[0])
  return cv.warpAffine(img, transMat, dimensions)

translated = translate(img, -100, 100)
plt.image(232, translated, "TRANSLATE")

# Rotation
def rotate(img, angle, rotPoint=None):
  (height, width) = img.shape[:2]

  if rotPoint is None:
    rotPoint = (width//2, height//2)

  rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
  dimensions = (width, height)

  return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 60)
plt.image(233, rotated, "ROTATE")

# Resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
plt.image(234, resized, "RESIZE")

# Flip
flipped = cv.flip(img, flipCode=0)
plt.image(235, flipped, "FLIP")

# Crop
cropped = img[200:400, 300:400]
plt.image(236, cropped, "CROP")

plt.show()
