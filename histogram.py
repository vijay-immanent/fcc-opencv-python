import cv2 as cv
from matplotlib import pyplot as plt
from img import show as imshow
import numpy as np

img = cv.imread("photos/cats 2.jpg")
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
blank = np.zeros(img.shape[:2], dtype='uint8')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

imshow(gray, "GRAY")

circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
mask = cv.bitwise_and(gray, gray, mask=circle)
imshow(mask, "Mask")

# grayscale histogram
gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])

plt.figure("Grayscale Histogram")
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0, 256])

# color histogram
colors = ('b', 'g', 'r')
plt.figure("Color Histogram")
plt.title("Color Histogram")
plt.xlabel("Bins")
plt.ylabel('# of pixels')
for i, col in enumerate(colors):
  hist = cv.calcHist([img], [i], mask, [256], [0,256])
  plt.plot(hist, color=col)
  plt.xlim([0, 256])



plt.show()
cv.waitKey(0)