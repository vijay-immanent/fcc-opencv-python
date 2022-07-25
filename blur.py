import cv2 as cv
import plt

img = cv.imread("photos/cats.jpg", )
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.image(231, rgb, "RGB")

# Average
average = cv.blur(rgb, (3,3))
plt.image(232, average, "AVERAGE")

# Gaussian
gauss = cv.GaussianBlur(rgb, (3, 3), 0)
plt.image(233, gauss, "GAUSSIAN")

# Median
median = cv.medianBlur(rgb, 3)
plt.image(234, median, "MEDIAN")

# Bilateral
bilateral = cv.bilateralFilter(rgb, 10, 35, 25)
plt.image(235, bilateral, "BILATERAL")

plt.show()