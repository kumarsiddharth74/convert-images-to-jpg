# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 22:57:55 2021

@author: kumar
"""

from PIL import Image
import os
path1="C:/Users/kumar/Desktop/axmind works/image_download_clean/test/Toyota_sienna"
os.chdir(path1)
arr = os.listdir()
i1=int(0)
for i in arr:
    no_samples=len(arr)
    i1=i1+1
    im = Image.open(i)
    
    rgb_im = im.convert("RGB")
    x = i.split('.')
    name=x[0]
    name=name+"_jpg"+'.jpg'
    im.close()
    rgb_im.save(name)
    os.remove(i)
    rgb_im.close()
    
    percentage=(i1/no_samples)*100
    print("converting to JPG")
    print(percentage,"% Done")