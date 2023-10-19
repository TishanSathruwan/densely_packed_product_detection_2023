import cv2
from matplotlib import pyplot as plt



path = '/kaggle/input/sku110k-annotations/SKU110K_fixed/images/train/train_1039.jpg'

# Read image
img = cv2.imread(path)

#plot image
plt.imshow(img)
plt.show()