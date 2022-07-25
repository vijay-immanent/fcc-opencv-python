import cv2 as cv
from img import show

img = cv.imread("photos/cats.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Simple Threshold
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
show(thresh, "Threshold")

threshold_inv, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
show(thresh_inv, "Threshold Inverse")

# Adaptive Threshold
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
show(adaptive_thresh, "Adaptive Threshold")

cv.waitKey(0)