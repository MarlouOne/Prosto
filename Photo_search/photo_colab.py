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
    # print(strFolderPath)
    listFolderContent = []
    for filename in os.listdir(strFolderPath):
        listFolderContent.append(strFolderPath + '\\' + filename)
    
    # print(listFolderContent)
    return listFolderContent

def get_listOfImage(listContent, intConvasWidth=100, intConvasHeight=100, intCount = 4):
    listImage = []
    for item in listContent:
        obj = Image.open(item).convert("RGBA")
        obj = obj.resize((intConvasWidth,intConvasHeight))
        listImage.append(obj)
    if intCount == 3:
        listImage[2].resize((150,100))
    # elif intCount == 4:
    #     listImage[1], listImage[2], listImage[3] = listImage[3], listImage[1], listImage[1]
    return listImage

def get_ConvasSize(intImageCount = 4):
    # print(intImageCount)
    if intImageCount == 4 or intImageCount == 3: 
        return 175, 175
    else: 
        return 100, 150

def get_listPhotoCoordinate(intImageCount = 4):
    if intImageCount == 4 :
        return [(0,0), (0,75), (75,0), (75,75)]
    elif intImageCount == 3: 
        return [(0,0), (75,0), (0,75)]
    else: 
        return [(0,0), (75,0)]

def make_imageMask(intImageCount=4):
    intConvasWidth, intConvasHeight = get_ConvasSize(intImageCount)
    print(intConvasWidth, intConvasHeight)
    # convas = Image.new('RGBA', (intConvasWidth, intConvasHeight))
    # draw = ImageDraw.Draw(convas)
    
    # listFillCalour = ['blue','red', 'yellow', 'green']
    
    
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
    
    listCoordinateTyples = listCoordinateTyples[:intImageCount] # Test
    
    # for i in range(len(listCoordinateTyples)):
    #     # print(listCoordinateTyples[i])
    #     draw.polygon(listCoordinateTyples[i], fill=listFillCalour[i], outline=(0, 0, 0))
        
    # convas.show()
    
    return listCoordinateTyples

def get_MaskImage(typleCoordinateTyple, intConvasWidth, intConvasHeight):
    convas = Image.new('RGBA', (intConvasWidth, intConvasHeight))
    draw = ImageDraw.Draw(convas)
    draw.polygon(typleCoordinateTyple, fill='white', outline=(0, 0, 0))
    # convas.show()
    return convas

def get_listMask(listCoordinateTyples):
    listMaskImages = []
    intConvasWidth, intConvasHeight = get_ConvasSize(len(listCoordinateTyples))
    for i in range(len(listCoordinateTyples)):
        listMaskImages.append(get_MaskImage(listCoordinateTyples[i], intConvasWidth, intConvasHeight))
    
    # show_images(listMaskImages)
    return listMaskImages

def get_cropedMasks(listMaskImages):
    # show_images(listMaskImages)
    print(get_ConvasSize())
    # listPhotoCoordinate = get_listPhotoCoordinate(len(listMaskImages))
    listMaskImages[0] = listMaskImages[0].crop( (0,0,100,100) )
    listMaskImages[1] = listMaskImages[1].crop( (75,0,175,100) )
    listMaskImages[2] = listMaskImages[2].crop( (0,75,100,175) )
    listMaskImages[3] = listMaskImages[3].crop( (75,75,175,175) )
    # show_images(listMaskImages)
    return listMaskImages

def get_calage(listImages, listMaskImages):
    intConvasWidth, intConvasHeight = get_ConvasSize(len(listImages))
    listPhotoCoordinate = get_listPhotoCoordinate(len(listImages))
    
    convas = Image.new('RGBA', (intConvasWidth, intConvasHeight))
    draw = ImageDraw.Draw(convas)
    draw.polygon(((0,0),(0,175),(175,175),(175,0)), fill='white', outline=(0, 0, 0))
    convas.show()
    # a, b, c = listImages[0], listPhotoCoordinate[0], listMaskImages[0]
    # convas.paste(listImages[0], listPhotoCoordinate[0],listMaskImages[0])
    # convas.paste(listImages[1], listPhotoCoordinate[1],listMaskImages[1])
    # convas.paste(listImages[2], listPhotoCoordinate[2],listMaskImages[2])
    # convas.paste(listImages[3], listPhotoCoordinate[3],listMaskImages[3])
    for i in range(len(listImages)):
        convas.paste(listImages[i], listPhotoCoordinate[i],listMaskImages[i],)
        convas.show()
    # convas.show()
    
def show_images(listImages):
    for image in listImages:
        image.show()

class listBuffer():
    listBuffer = []
    
    def __init__(self, listBufferContent):
        self.listBuffer = listBufferContent
        
    def get_LastItem(self):
        buffer = self.listBuffer[-1]
        self.listBuffer.pop(-1)
        return buffer

def main(strPhotoFolderName = 'photos', intCountImages = 4):
    listFolderContent = get_listFolderContent(strPhotoFolderName)
    listImages = get_listOfImage(listFolderContent)
    listCoordinateTyples = make_imageMask(intCountImages)
    # show_images(listImages)
    listMaskImage = get_listMask(listCoordinateTyples)
    listMaskImage = get_cropedMasks(listMaskImage)
    # make_calage(listImages[:intCountImages], listCoordinateTyples)
    get_calage(listImages, listMaskImage)

main()