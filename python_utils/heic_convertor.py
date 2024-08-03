'''
Author: daniel
Date: 2024-08-04 01:05:02
LastEditTime: 2024-08-04 01:13:52
LastEditors: daniel
Description: 
FilePath: /daniellli.github.io/python_utils/heic_convertor.py
have a nice day
'''






import shutil
from PIL import Image
import os
import pillow_heif
from os.path import join, split, exists, isdir, isfile, dirname
from tqdm import tqdm 

def convert_heic_to_jpg(heic_folder, jpg_folder):
    # 检查输出文件夹是否存在，如果不存在则创建
    if not os.path.exists(jpg_folder):
        os.makedirs(jpg_folder)

    # 遍历 HEIC 文件夹中的所有文件
    for file in tqdm(os.listdir(heic_folder)):
        if file.endswith('.HEIC'):
            heic_path = os.path.join(heic_folder, file)
            image = pillow_heif.read_heif(heic_path)
            jpg_path = os.path.join(jpg_folder, os.path.splitext(file)[0] + '.jpg')
            image.save(jpg_path)
            os.remove(heic_path)
            print(heic_path, ' is removed!')




if __name__ == "__main__":
    heic_folder = 'photos/XMU_graduation'
    png_folder = 'photos/XMU_graduation'

    convert_heic_to_jpg(heic_folder, png_folder)