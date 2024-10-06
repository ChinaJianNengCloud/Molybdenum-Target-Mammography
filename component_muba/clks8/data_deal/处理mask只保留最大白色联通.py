import numpy as np
from scipy.ndimage import label, find_objects


def keep_largest_white_region(image):
    labeled_array, num_features = label(image == 255)
    if num_features == 0:
        return image
    else:
        sizes = np.bincount(labeled_array.ravel())
        sizes[0] = 0
        largest_label = np.argmax(sizes)
        new_image = np.zeros_like(image)
        new_image[labeled_array == largest_label] = 255

        return new_image