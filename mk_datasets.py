import os
import random
import cv2
from PIL import Image, ImageChops
import numpy as np
import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise

# 入力画像（影ナシ）パス
image_dir = './data/mk_datasets/data_C'
# セグメントマスクパス
mask_dir = './data/mk_datasets/segment_mask'
# 出力画像（影アリ）パス
output_dir_A = './data/mk_datasets/data_A'
# 出力画像（影マスク）パス
output_dir_B = './data/mk_datasets/data_B'

def generate_shadow(width, height, octaves, seed):
    noise = PerlinNoise(octaves=octaves, seed=seed)
    pic = [[noise([i / width, j / height]) + 0.7 for j in range(width)] for i in range(height)]
    pic_array = np.array(pic)
    min_value = np.min(pic_array)
    max_value = np.max(pic_array)
    pic = (pic_array - min_value) / (max_value - min_value)
    pic = [[1 - val for val in row] for row in pic]
    pic = [[1 if val > 0.5 else 0.4 for val in row] for row in pic]
    return pic

# 画像の読み込みとパーリンノイズの乗算
for filename in os.listdir(image_dir):
    if filename.endswith('.png') or filename.endswith('.jpg'):
        image_path = os.path.join(image_dir, filename)
        img = Image.open(image_path)

        xpix, ypix = img.size[0], img.size[1]

        # octavesとseedのランダムな値の生成
        octaves = random.randint(1, 3)
        seed = random.randint(1, 100)
        kernel = random.randrange(11, 100, 2)

        # 対応するマスク画像の読み込み
        mask_filename = os.path.splitext(filename)[0] + '_segmented.png'
        mask_path = os.path.join(mask_dir, mask_filename)
        mask_img = Image.open(mask_path)
        mask_img = mask_img.convert('RGB')
        new_img = img.copy()
        diff_img = Image.new("RGB", (xpix, ypix), color="black")

        shadow = np.array(generate_shadow(img.size[0], img.size[1], octaves, seed))

        masked_shadow = np.ones_like(shadow)

        for y in range(img.size[1]):
            for x in range(img.size[0]):
                mask_pixel = mask_img.getpixel((x, y))
                if mask_pixel == (192, 0, 128):
                    masked_shadow[y][x] = shadow[y][x]

        masked_shadow = cv2.GaussianBlur(masked_shadow, (kernel, kernel), 0)
        plt.imshow(masked_shadow, cmap='gray')
        plt.show()

        # 入力画像にperlin_noiseを乗算
        new_img = Image.new("RGB", img.size)
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                pixel = img.getpixel((x, y))
                new_pixel = tuple(int(pixel[i] * masked_shadow[y][x]) for i in range(3))
                new_img.putpixel((x, y), new_pixel)

        diff_img = np.array([[1 - val for val in row] for row in masked_shadow])
        diff_img = Image.fromarray((diff_img * 255).astype(np.uint8))
        output_B = os.path.join(output_dir_B, filename)
        diff_img.save(output_B)

        output_A = os.path.join(output_dir_A, filename)
        new_img.save(output_A)

