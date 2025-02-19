'''
Author: daniel
Date: 2025-02-19 15:17:40
LastEditTime: 2025-02-19 15:25:27
LastEditors: daniel
Description: 
FilePath: /daniellli.github.io/resize.py
have a nice day
'''


from argparse import ArgumentParser
import os 

from os.path  import join, split, exists, dirname
from posixpath import dirname

import cv2



parser = ArgumentParser()

parser.add_argument('--src', type=str, help='the image path to resize')
parser.add_argument('--resize-ratio', type=float, help='the resized image ratio ')

args = parser.parse_args()



if __name__ == "__main__":


    save_dir = dirname(args.src)

    ori_name = args.src.split('/')[-1]
    real_ori_name, img_suffix = ori_name.split('.')

    print(real_ori_name, img_suffix)

    img = cv2.imread(args.src)

    resized = cv2.resize(img, None, fx = args.resize_ratio, fy= args.resize_ratio, interpolation=cv2.INTER_LINEAR )

    w,h = resized.shape[:2]

    save_name = real_ori_name+'-%dX%d'%(w,h)+ '.'+img_suffix 

    cv2.imwrite( join(save_dir,save_name),resized)

    

    
    

    

    