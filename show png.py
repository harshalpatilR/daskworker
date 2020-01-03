import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('temp.png')
plt.imshow(img)
# not required - plt.show()