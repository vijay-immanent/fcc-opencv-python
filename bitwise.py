import cv2 as cv
import plt
import numpy as np

blank = np.zeros((400, 400), dtype="uint8")

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
plt.image(231, rectangle, "RECTANGLE")
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)
plt.image(232, circle, "CIRCLE")

# AND -> intersection
bitwise_and = cv.bitwise_and(rectangle, circle)
plt.image(233, bitwise_and, "AND")

# OR -> union
bitwise_or = cv.bitwise_or(rectangle, circle)
plt.image(234, bitwise_or, "OR")

# XOR -> complements
bitwise_xor = cv.bitwise_xor(rectangle, circle)
plt.image(235, bitwise_xor, "XOR")

# NOT -> inverse
bitwise_not = cv.bitwise_not(bitwise_or)
plt.image(236, bitwise_not, "NOT OR")
plt.show()