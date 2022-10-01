# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 15:49:30 2022

@author: Marlou
"""
import os
from random import randint

from PIL import Image, ImageEnhance, ImageDraw

        
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
        listImage.append(Image.open(item).convert("RGBA"))
    return listImage

# def get_convasSize(listContent):
#     intImageCount = len(listContent)
#     intMaxWidth  = 0
#     intMaxHeight = 0
#     for image in listContent:
#         intMaxWidth = max(image.size[0],intMaxWidth)
#         intMaxHeight = max(image.size[1],intMaxHeight)
        
#     return  intMaxWidth, intMaxHeight

def make_imageMask(imageObj):
    imageObj.show()
    intConvasWidth, intConvasHeight = imageObj.size
    print(intConvasWidth, intConvasHeight)
    convas = Image.new('RGBA', (intConvasWidth, intConvasHeight))
    draw = ImageDraw.Draw(convas)
    
    tupleCoordinate = ( (0, randint(0, intConvasHeight),
                        (0,intConvasHeight),
                        (intConvasWidth, intConvasHeight),
                        (intConvasWidth, randint(0, intConvasHeight)) ))
    
    draw.polygon(tupleCoordinate, fill='blue', outline=(0, 0, 0))
    convas.show()
    

class listBuffer():
    listBuffer = []
    
    def __init__(self, listBufferContent):
        self.listBuffer = listBufferContent
        
    def get_LastItem(self):
        buffer = self.listBuffer[-1]
        self.listBuffer.pop(-1)
        return buffer

def main(strPhotoFolderName = 'photos', ):
    listFolderContent = get_listFolderContent(strPhotoFolderName)
    listImage = get_listOfImage(listFolderContent)
    make_imageMask(listImage[0])

main()