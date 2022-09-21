import os
import numpy as np
from PIL import Image
import config


def load_picture(src_path: str) -> np.array:
    """Load and resize picture and return is as np.array"""

    img = Image.open(src_path)
    resized = img.resize(config.PICTURE_SIZE)
    img_arr = np.array(resized)
    return img_arr


def save_picture_rgb(dest_path: str, img_arr: np.array):
    result = Image.fromarray(np.uint8(img_arr)).convert('RGB')
    result.save(f'{dest_path}.jpg')
    return


def clear_last_bit(N, K):
    """Clear last K bit(s) from number N"""

    # Create a mask
    mask = (-1 << K + 1)

    # Bitwise AND operation with
    # the number and the mask
    N = N & mask

    return N


def filter_bitwise(N, K):
    # Create a mask
    mask = 1 << K

    # Bitwise AND operation with
    # the number and the mask
    N = N & mask

    return N


def get_clear_last_bit(img, bit):
    vfunc = np.vectorize(clear_last_bit)
    return vfunc(img, bit)


def get_filter_bitwise(img, bit):
    vfunc = np.vectorize(filter_bitwise)
    return vfunc(img, bit)
