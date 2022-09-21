import os
import numpy as np
from PIL import Image
from tqdm import tqdm
import utils
import config


WATERMARK_PIC_SRC = os.path.join(config.SRC_FOLDER, config.WATERMARK_PIC)
TARGET_PIC_SRC = os.path.join(config.SRC_FOLDER, config.TARGET_PIC)


def filter_last_bit(img_arr, K, save_pic=False):
    IMG_DEST_PATH = os.path.join(
        config.DEST_FOLDER, f'remove_last_{K}_bits')
    filtered = utils.get_clear_last_bit(img_arr, K)

    if save_pic:
        utils.save_picture_rgb(IMG_DEST_PATH, filtered)

    return filtered


def main():
    watermark_arr = utils.load_picture(WATERMARK_PIC_SRC)
    target_arr = utils.load_picture(TARGET_PIC_SRC)

    for bit in tqdm(range(1, 3 + 1), desc='Filter', bar_format='{l_bar}{bar:40}{r_bar}{bar:-10b}'):
        # Iterate over last K bits and clear them
        watermark_filtered = filter_last_bit(watermark_arr, bit, True)


if __name__ == "__main__":
    main()
