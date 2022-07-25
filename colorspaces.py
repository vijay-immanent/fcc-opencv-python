import cv2 as cv
import plt

# BGR
img = cv.imread("photos/park.jpg")
plt.image(231, img, "BGR")

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.image(234, rgb, "BGR -> RGB")

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
plt.image(232, gray, "BGR -> GRAY")

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
plt.image(233, hsv, "BGR -> HSV")

# BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
plt.image(235, lab, "BGR -> LAB")

# Gray to RGB
gray_rgb = cv.cvtColor(gray, cv.COLOR_GRAY2RGB)
plt.image(236, gray_rgb, "GRAY -> RGB")

plt.show()