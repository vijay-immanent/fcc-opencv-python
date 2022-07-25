import cv2 as cv
import plt

img = cv.imread("photos/park.jpg")
plt.image(241, img, "ORIGINAL")

# Conversion to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
plt.image(242, gray, "GRAY")

# Blur
blurred = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
plt.image(243, blurred, "BLUR")

# Edge Cascade
# Edges can be reduced by using a blurred image as input
edges = cv.Canny(blurred, 125, 175)
plt.image(244, edges, "EDGES")

# Dilate Image
dilated = cv.dilate(edges, (3,3), iterations=1)
plt.image(245, dilated, "DILATE")

# Erode Image
eroded = cv.erode(edges, (3, 3), iterations=1)
plt.image(246, eroded, "ERODE")

# Resize
resized = cv.resize(img, (400, 300))
plt.image(247, resized, "RESIZE")

# Crop
cropped = img[50:200, 200:400]
plt.image(248, cropped, "CROP")

plt.show()