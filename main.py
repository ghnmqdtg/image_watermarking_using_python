import os
import numpy as np
from tqdm import tqdm
import utils
import config


def encode(watermark: np.array, target: np.array, K: int, save_pic: bool = False) -> np.array:
    """
    Encode a watermark into the target image

    Parameters
    ----------
    watermark: np.array
        The np.array object of the watermark
    target: np.array
        The np.array object of the target image
    K: int
        Indicates how many last K bits to be encode into
    save_pic: bool
        Save the image or not
    """

    # Filter the last (7 - K) bits of every pixel of the watermark
    watermark_filterd = utils.filter_last_bit(watermark, 7 - K)
    # Shift (7 - K) bits and keep the first K bits data of watermark
    watermark_shifted = watermark_filterd >> (7 - K)
    # Filter the last K bits of every pixel of the target image
    # So that we can encode the watermark into it
    target_filtered = utils.filter_last_bit(target, K)
    # Add the watermark into target
    target_encoded = target_filtered | watermark_shifted

    if save_pic:
        # The path to save the pic
        dest_path = os.path.join(
            config.DEST_FOLDER, f'encode_last_{K}_bits')
        # Save the picture
        utils.save_picture_rgb(dest_path, target_encoded)

    return target_encoded


def decode(target: np.array, K: int, save_pic: bool = False) -> np.array:
    """
    Decode a watermark from a encode image

    Parameters
    ----------
    target: np.array
        The np.array object of the target image
    K: int
        Indicates how many last K bits were the watermark encode
    save_pic: bool
        Save the image or not
    """

    # Extract the last K bits data from the target
    target_decoded = utils.get_last_bit(target, K)
    # Shift the extracted K bits data to restore the watermark
    target_restored = target_decoded << (7 - K)

    if save_pic:
        # The path to save the picture
        dest_path = os.path.join(
            config.DEST_FOLDER, f'decode_last_{K}_bits')
        # Save the picture
        utils.save_picture_rgb(dest_path, target_restored)

    return target_restored


def main():
    """
    Encode the first K bits of watermark into a target image, and then decode it.
    """

    # Create folder if it doesn't exist
    utils.create_folder(config.SRC_FOLDER)
    utils.create_folder(config.DEST_FOLDER)

    # Get the path to the watermark and target files
    WATERMARK_PIC_SRC = os.path.join(config.SRC_FOLDER, config.WATERMARK_PIC)
    TARGET_PIC_SRC = os.path.join(config.SRC_FOLDER, config.TARGET_PIC)

    # Load files as np.array objects
    watermark_arr = utils.load_picture(WATERMARK_PIC_SRC)
    target_arr = utils.load_picture(TARGET_PIC_SRC)
    # Set the encode range
    encode_range = range(
        1, config.ENCODE_RANGE + 1) if config.ITER_FROM_LSB else [config.ENCODE_RANGE]
    # Save the image or not
    save_img = config.SAVE_IMG

    for bit in tqdm(encode_range, desc='Encode & Decode the watermark', bar_format='{l_bar}{bar:40}{r_bar}{bar:-10b}'):
        # Encode the watermark
        target_encoded = encode(watermark_arr, target_arr, bit, save_img)
        # Decode the watermark
        target_decode = decode(target_encoded, bit, save_img)


if __name__ == "__main__":
    # Run the process
    main()
