import os
import numpy as np
from PIL import Image
import config


def create_folder(dir) -> None:
    """
    Create a folder if it doesn't already exist
    """

    if not os.path.exists(dir):
        os.makedirs(dir)


def load_picture(src_path: str) -> np.array:
    """
    Load and resize picture and return is as np.array

    Parameters
    ----------
    src_path : str
        The path to the source picture
    """

    img = Image.open(src_path)
    resized = img.resize(config.PICTURE_SIZE)
    img_arr = np.array(resized)
    return img_arr


def save_picture_rgb(dest_path: str, img_arr: np.array) -> None:
    """
    Save np.array image data in RGB JPG

    Parameters
    ----------
    dest_path : str
        The path to save the picture
    img_arr : np.array
        Image data in np.array
    """

    result = Image.fromarray(np.uint8(img_arr)).convert('RGB')
    result.save(f'{dest_path}.jpg')


def filter_last_bit(N: int or np.array, K: int) -> int or np.array:
    """
    Filter the last K bit(s) from number N

    Parameters
    ----------
    N: int or np.array
        The data to be filtered
    K: int
        Last K bit(s) to be filtered
    """

    # Create a mask
    mask = (-1 << K + 1)

    # Bitwise AND operation with
    # the number and the mask
    N = N & mask

    return N


def get_last_bit(N: int or np.array, K: int) -> int or np.array:
    """
    Get the last K bit(s) from number N

    Parameters
    ----------
    N: int or np.array
        The data to be filtered
    K: int
        Last K bit(s) to get
    """

    # Create a mask
    mask = ~ (-1 << K + 1)

    # Bitwise AND operation with
    # the number and the mask
    N = N & mask

    return N
