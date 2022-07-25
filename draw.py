import cv2 as cv
import numpy as np
import plt

# create a blank image
blank = np.zeros((500, 500, 3), dtype='uint8')
plt.image(241, blank, "BLANK")

# paint the entire image
blank[:] = 100, 200, 0
plt.image(242, blank, "COLOR")

# paint a subsection of the image
blank[100:200, 300:400] = 0, 100, 200
plt.image(243, blank, "SUBSECTION")

# draw a rectangle
cv.rectangle(blank, (200, 200), (300, 300), (200, 100, 0), thickness=15)
plt.image(244, blank, "RECTANGLE")

# draw a circle
cv.circle(blank, (100, 100), 50, (230, 100, 90), thickness=-1)
plt.image(245, blank, "CIRCLE")

# draw a line
cv.line(blank, (0, 420), (500, 420), (230, 240, 250), thickness=15)
plt.image(246, blank, "LINE")

# display text
cv.putText(blank, "Hello Vijay!", (50, 400), cv.FONT_HERSHEY_COMPLEX, 1.0, (10, 8, 12), 2)
plt.image(247, blank, "TEXT")

plt.show()