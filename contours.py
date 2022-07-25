import cv2 as cv
import plt
import numpy as np

img = cv.imread("photos/cats.jpg")
plt.image(231, img, "ORIGINAL")


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
plt.image(234, gray, "GRAY")

blurred = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)

canny = cv.Canny(blurred, 125, 175)
plt.image(232, canny, "CANNY EDGES")

# Mathematically, contours != edges
canny_contours, canny_hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'canny contour(s): {len(canny_contours)}')

blank = np.zeros(img.shape[:2], dtype="uint8")
cv.drawContours(blank, canny_contours, -1, 255, 1)
plt.image(235, blank, "CANNY CONTOURS")

# Thresholding  
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
plt.image(233, thresh, "THRESH")

thresh_contours, thresh_hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'thresh countour(s): {len(thresh_contours)}')

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.drawContours(blank, thresh_contours, -1, 255, 1)
plt.image(236, blank, "THRESH CONTOURS")

plt.show()