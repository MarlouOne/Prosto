# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 15:49:30 2022

@author: Marlou
"""
import os

import PIL.Image as Image

# class photo():
#     width : int
#     height : int
#     content : None
    
#     def get_size(self):
        
    
#     def set_width(self, width):
#         self.width = width
        
#     def set_height(self, height):
#         self.height = height
        
#     def set_content(self, content):
#         self.content = content
        
        
def get_listFolderContent(strFolderName):
    strFolderPath = os.getcwd()
    strFolderPath += '\\' + strFolderName
    print(strFolderPath)
    listFolderContent = []
    for filename in os.listdir(strFolderPath):
        listFolderContent.append(strFolderPath + '\\' + filename)
    
    print(listFolderContent)
    return listFolderContent

def get_listOfImage(listContent):
    listImage = []
    for item in listContent:
        listImage.append(Image.open(item))
    return listImage

def main(strPhotoFolderName = 'photos', ):
    listFolderContent = get_listFolderContent(strPhotoFolderName)
    listImage = get_listOfImage(listFolderContent)

main()