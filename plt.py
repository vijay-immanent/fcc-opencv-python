from matplotlib import pyplot as plt

def image(place, image, title=None, cmap="gray"):
  plt.subplot(place), plt.imshow(image, cmap=cmap), plt.title(title)

def show():
  plt.show()