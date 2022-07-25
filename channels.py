import cv2 as cv
import numpy as np
import plt

img = cv.imread('photos/park.jpg')
rgb =cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.image(231, rgb, "RGB")



blank = np.zeros(img.shape[:2], dtype="uint8")
def merge_rgb(r=blank, g=blank, b=blank):
  return cv.merge(([r, g, b]))

b, g, r = cv.split(img)

cb, cg, cr = merge_rgb(b=b), merge_rgb(g=g), merge_rgb(r=r)


plt.image(232, cb, "BLUE")
plt.image(233, cg, "GREEN")
plt.image(234, cr, "RED")

print(img.shape), print(b.shape), print(g.shape), print(r.shape)

plt.show()