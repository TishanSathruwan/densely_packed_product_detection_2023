# 🛍️ SKU110K Dataset

Here you will find the images and annotations (labels) for the SKU110K dataset. Also included is a notebook containing the process to download the SKU110K dataset and convert the annotations to a variety of formats (e.g., YOLOv5).

## Files

This dataset contains the labels comprising the bounding boxes (only one class for all detections), as well as all images for the SKU110K dataset. The included notebook is meant to be run locally, and the code shows how to use the Kaggle CLI for downloading the images to their corresponding location.

In order to use YOLOv5, the included notebook shows how to save the annotations in the correct format:
- One row per object
- Each row is `class` &nbsp; `x_center` &nbsp; `y_center` &nbsp; `width` &nbsp; `height` format
- Box coordinates must be in **normalized xywh** format (from 0 - 1). If your boxes are in pixels:
    - Divide `x_center` and `width` by image width
    - Divive `y_center` and `height` by image height
- Class numbers are zero-indexed (start from 0)

Although the included annotations use my preferred directory structure for organization (as detailed below), they can all be contained in a single file as well.

    .
    ├── convert_yolov5.ipynb
    ├── data_kaggle.yaml
    ├── README.md
    ├── SKU110K_fixed    
        ├── images
            ├── test
            ├── train
            ├── val
        ├── labels
            ├── test
            ├── train
            ├── val

## Acknowledgements

I'd love to acknowledge the original authors: https://github.com/eg4000/SKU110K_CVPR19

---

🐞 If you find any bugs or have any questions regarding these notebooks, please open an issue. I'll address it as soon as I can. 

🐦 Reach out on [Twitter](https://twitter.com/datasith) if you have any questions. 

🔗 Please cite the original authors if you use this version of the dataset for your work.