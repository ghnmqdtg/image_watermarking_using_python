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
        config.DEST_FOLDER, f'remove_last_{K + 1}_bits')
    filtered = utils.get_clear_last_bit(img_arr, K)

    if save_pic:
        utils.save_picture_rgb(IMG_DEST_PATH, filtered)

    return filtered


def encoded(watermark_filtered, target_arr, K, save_pic=False):
    IMG_DEST_PATH = os.path.join(
        config.DEST_FOLDER, f'encode_last_{K}_bits')
    target_filtered = utils.get_clear_last_bit(target_arr, K)
    watermark_feature = watermark_filtered >> (7 - K)
    target_encoded = target_filtered | watermark_feature

    if save_pic:
        utils.save_picture_rgb(IMG_DEST_PATH, target_encoded)

    return target_encoded


def decode(target_encoded, K, save_pic=False):
    IMG_DEST_PATH = os.path.join(
        config.DEST_FOLDER, f'decode_last_{K}_bits')
    target_decode = utils.get_last_bit(target_encoded, K)
    target_restored = target_decode << (7 - K)

    if save_pic:
        utils.save_picture_rgb(IMG_DEST_PATH, target_restored)

    return target_restored


def main():
    watermark_arr = utils.load_picture(WATERMARK_PIC_SRC)
    target_arr = utils.load_picture(TARGET_PIC_SRC)

    for bit in tqdm(range(1, 3 + 1), desc='Encode & Decode the watermark', bar_format='{l_bar}{bar:40}{r_bar}{bar:-10b}'):
        # Iterate over last K bits and clear them
        watermark_filtered = filter_last_bit(watermark_arr, 7 - bit, False)
        target_encoded = encoded(watermark_filtered, target_arr, bit, True)
        target_decode = decode(target_encoded, bit, True)


if __name__ == "__main__":
    main()
