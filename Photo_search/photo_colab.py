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
    elif intCount == 4:
        listImage[2], listImage[3] = listImage[3], listImage[2]
    return listImage

def get_ConvasSize(intImageCount = 4):
    # print(intImageCount)
    if intImageCount == 4 or intImageCount == 3: 
        return 150, 150
    else: 
        return 100, 150

def make_imageMask(intImageCount=4):
    intConvasWidth, intConvasHeight = get_ConvasSize(intImageCount)
    print(intConvasWidth, intConvasHeight)
    # convas = Image.new('RGBA', (intConvasWidth, intConvasHeight))
    # draw = ImageDraw.Draw(convas)
    
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
    
    listCoordinateTyples = listCoordinateTyples[:intImageCount] # Test
    
    # for i in range(len(listCoordinateTyples)):
    #     # print(listCoordinateTyples[i])
    #     draw.polygon(listCoordinateTyples[i], fill=listFillCalour[i], outline=(0, 0, 0))
        
    # convas.show()
    
    return listCoordinateTyples
    
def make_calage(listImages , listCoordinateTyples):
    # pass
    intCount = len(listImages)
    intConvasWidth, intConvasHeight = get_ConvasSize(intCount)
    
    back_convas = Image.new('RGBA', (intConvasWidth, intConvasHeight))

    image_X, image_Y = 0,0
    
    for i in range(intCount):
        im_size_X, im_size_Y = listImages[i].size
        imagePart = make_segmentedImage(listImages[i],  image_X, image_Y, listCoordinateTyples[i], intConvasWidth, intConvasHeight)
        back_convas.paste(imagePart, (image_X, image_Y))
        back_convas.show()
        # if  ((image_Y + im_size_Y < intConvasWidth) and image_X == 0) or image_Y == 0:
        #     image_X += 75
        # elif (image_Y + im_size_Y > intConvasWidth):
        #     image_Y = 0
            
        # elif ((image_X  + im_size_X < intConvasWidth) and (image_Y == 0)):
        #     image_Y += 75
        # else:
        #     image_X = 0
        
        if  ((image_Y + im_size_Y < intConvasWidth) and image_X == 0) or image_Y == 0:
            if ((image_X  + im_size_X < intConvasWidth) and (image_Y == 0)):
                image_X += 75
            else:
                image_X = 0
                if ((image_Y + im_size_Y < intConvasWidth) and image_X == 0) or image_Y == 0:
                    image_Y += 75
        else: 
            image_Y = 0
    back_convas.show()
        
    
    # cat_segmented = Image.composite(img_cat, blank, cat_mask)

def make_segmentedImage(image, image_X, image_Y, typlesCoordinateTyples, intConvasWidth, intConvasHeight):
    
    mask_convas = Image.new('RGBA', (intConvasWidth, intConvasHeight))
    mask_draw = ImageDraw.Draw(mask_convas)
    imagesMask = mask_draw.polygon(typlesCoordinateTyples, fill='white', outline=(0, 0, 0))
    # mask_convas.show()
    
    back_convas = Image.new('RGBA', (intConvasWidth, intConvasHeight))
    back_draw = ImageDraw.Draw(back_convas)
    
    print(image_X, image_Y)
    back_convas.paste(image, (image_X, image_Y))
    # back_convas.show()
    
    
    
    
    
    blank = back_convas.point(lambda _: 0)
    imageSegment = Image.composite(back_convas, blank, mask_convas)
    # imageSegment.show()
    return imageSegment

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
    make_calage(listImages[:intCountImages], listCoordinateTyples)

main()