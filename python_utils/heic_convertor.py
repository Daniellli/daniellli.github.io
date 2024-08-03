'''
Author: daniel
Date: 2024-08-04 01:05:02
LastEditTime: 2024-08-04 01:58:19
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


import os
from PIL import Image
from pillow_heif import register_heif_opener
register_heif_opener()
import glob
import os



 
def GetFiles(file_dir,file_type,IsCurrent=False):
    file_list = []
    for parent, dirnames, filenames in os.walk(file_dir):
        for filename in filenames:
            if filename.endswith(('.%s'%file_type)):  # 判断文件类型
                file_list.append(os.path.join(parent, filename))
                
        if IsCurrent == True:
            break
    return file_list



if __name__ == "__main__":
    # heic_folder = 'photos/XMU_graduation'
    # png_folder = 'photos/XMU_graduation'

    heic_folder = '/Users/xushaocong/Pictures/毕业照/selected_for_homepage_done_counterpart'
    png_folder = '/Users/xushaocong/XMU/exp/daniellli.github.io/photos/XMU_graduation'

    files = GetFiles(heic_folder,"HEIC")
    for file in files:
        print(file)
        file_name = file.split('.')[0]
        file_name = file_name.split('/')[-1]

        
        original_img_path = f'{file}'
        image = Image.open(original_img_path)
        image.save(f"{join(png_folder, file_name)}.jpg", format="jpeg")


