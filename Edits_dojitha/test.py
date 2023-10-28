import cv2
from matplotlib import pyplot as plt



test0_path_labels = "/kaggle/input/sku110k-annotations/SKU110K_fixed/labels/test/test_0.txt"
test0_path_image = "/kaggle/input/sku110k/SKU110K_fixed/test/test_0.jpg"


#plot image with bounding boxes
# text file format: class x_center y_center width height (all values are relative to image size, i.e. in [0,1])

def plot_image_with_boxes(image_path, text_file_path):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    f = open(text_file_path, "r")
    for line in f:
        line = line.split()
        x_center = float(line[1])
        y_center = float(line[2])
        width = float(line[3])
        height = float(line[4])
        x1 = int((x_center - width / 2) * img.shape[1])
        y1 = int((y_center - height / 2) * img.shape[0])
        x2 = int((x_center + width / 2) * img.shape[1])
        y2 = int((y_center + height / 2) * img.shape[0])
        img = cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    plt.figure(figsize=(20, 20))
    plt.imshow(img)
    plt.show()

plot_image_with_boxes(test0_path_image, test0_path_labels)