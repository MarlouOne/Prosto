# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 15:49:30 2022

@author: Marlou
"""
import json

def get_listPhotoPath(strPhotoFolder):
    with open(strPhotoFolder, 'r') as file:
        listPhotosPaths = json.load(file) 

def main():
    
    pass

main()