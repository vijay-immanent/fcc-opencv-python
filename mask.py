import cv2 as cv
import numpy as np
import plt

img = cv.imread('photos/cats 2.jpg')
img = cv.cvtColor(img, cv.COLOR_BGRA2RGB)
plt.image(231, img, "RGB")

blank = np.zeros(img.shape[:2], dtype="uint8")

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
plt.image(232, mask, "MASK")

masked = cv.bitwise_and(img, img, mask=mask)
plt.image(233, masked, "MASKED IMG")

plt.show()