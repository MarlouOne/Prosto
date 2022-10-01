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

# def get_inverseCoordinate(tupleCoordinate, intConvasWidth, intConvasHeight):
#     for item in 

def make_imageMask(imageObj, intImageCount=3):
    imageObj.show()
    intConvasWidth, intConvasHeight = imageObj.size
    print(intConvasWidth, intConvasHeight)
    convas = Image.new('RGBA', (intConvasWidth, intConvasHeight))
    draw = ImageDraw.Draw(convas)
    
    # listFillCalour = ['blue','red', 'yellow', 'green']
    listFillCalour = ['blue','red', 'yellow', 'green']
    
    
    tupleCoordinate_One = ( (0, 0), # 0 - 0
                            (0, int(randint(0, intConvasHeight))), # 0 - random Y
                            (intConvasWidth, int(randint(0, intConvasHeight))), # X -  random Y
                            (intConvasWidth, 0) ) # X -  Y
    
    tupleCoordinate_Two = ( tupleCoordinate_One[1], # 0 - random Y
                            (0,intConvasHeight), # 0 - Y
                            (intConvasWidth, intConvasHeight), # X - Y
                            tupleCoordinate_One[2] ) # X - random Y
    
    tupleCoordinate_Three = ( (int(randint(0, intConvasWidth)), 0), # 0 - random Y
                              (int(randint(0, intConvasWidth)), intConvasHeight), # 0 - Y
                              (intConvasWidth, intConvasHeight), # random X - Y
                              (intConvasWidth, 0 )) # 0 - random Y
    
    tupleCoordinate_Four = ( (0, 0),  # X - random Y/2
                             (0, intConvasHeight), # 0 - 0                    
                             tupleCoordinate_Three[1], # 0 - random Y
                             tupleCoordinate_Three[0]) # 0 - Y

                        
    
    listCoordinateTyples = [tupleCoordinate_One, tupleCoordinate_Two, tupleCoordinate_Three, tupleCoordinate_Four] # Test
    
    # listCoordinateTyples = [tupleCoordinate_One, tupleCoordinate_Four]
    # listCoordinateTyples = [tupleCoordinate_One]
    # listCoordinateTyples = [((0, 100), (0, 600), (400, 600), (600, 400))]
    
    listCoordinateTyples = listCoordinateTyples[:intImageCount] # Test
    
    for i in range(len(listCoordinateTyples)):
        print(listCoordinateTyples[i])
        draw.polygon(listCoordinateTyples[i], fill=listFillCalour[i], outline=(0, 0, 0))
        
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