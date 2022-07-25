# Mathematically, gradients != edges
import cv2 as cv
import numpy as np
from img import show

img = cv.imread("photos/cats.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# show(gray, "GRAY")

# Laplace
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
show(lap, "Laplacian")

# Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combine_sobel = cv.bitwise_or(sobelx, sobely)
# show(sobelx, "Sobel X")
# show(sobely, "Sobel Y")
show(combine_sobel, "Sobel Combined")

canny = cv.Canny(gray, 150, 175)
show(canny, "Canny")

cv.waitKey(0)