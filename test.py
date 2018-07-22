import skimage.data
import numpy as np
import selectivesearch
from matplotlib.image import imread
import matplotlib.pyplot as plt

#%matplotlib inline

img2 = imread('vendor_dw/8009-0092-20-MR-042-D01-00001-E_Rev.I1_tmp.jpg')
img1 = imread('vendor_dw/Drawing.jpg')
img3 = imread('vendor_dw/Drawing_2.jpg')

#ima2 = img1.reshape(100,100)
#plt.imshow(img1)

#plt.imshow(img2)


#img1.shape

from __future__ import (
    division,
    print_function,
)

import skimage.data
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import selectivesearch


def main():

    # loading astronaut image
    img = imread('vendor_dw/Drawing_2.jpg')

    # perform selective search
    img_lbl, regions = selectivesearch.selective_search(
        img, scale=20, sigma=0.9, min_size=3)

    candidates = set()
    for r in regions:
        # excluding same rectangle (with different segments)
        if r['rect'] in candidates:
            continue
        # excluding regions smaller than 2000 pixels
        if r['size'] < 2000:
            continue
        # distorted rects
        x, y, w, h = r['rect']
        if w / h > 1.2 or h / w > 1.2:
            continue
        candidates.add(r['rect'])

    # draw rectangles on the original image
    fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(6, 6))
    ax.imshow(img)
    for x, y, w, h in candidates:
        print(x, y, w, h)
        rect = mpatches.Rectangle(
            (x, y), w, h, fill=False, edgecolor='red', linewidth=1)
        ax.add_patch(rect)

    plt.show()
    
if __name__ == "__main__":
    main()
