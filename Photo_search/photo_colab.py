# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 15:49:30 2022

@author: Marlou
"""
import os

from PIL import Image, ImageEnhance

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

# def make_boxColage():
    # collage = Image.new("RGBA", (2000,1000))
    
    
    # img = Image.open("Desktop/300.jpg")
    # img = img.resize((500,500))
    
    # filter = ImageEnhance.Brightness(img)
    
    # c=0.7
    # for i in range(0,2000,500):
    #     for j in range(0,2000,500):
    #         new_img = filter.enhance(c)
    #         collage.paste(new_img, (j,i))
    #         c+=0.1
    #         print(c)
    # new.show()

        
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

def get_convasSize(listContent):
    intImageCount = len(listContent)
    intMaxWidth  = 0
    intMaxHeight = 0
    for image in listContent:
        intMaxWidth = max(image.size[0],intMaxWidth)
        intMaxHeight = max(image.size[1],intMaxHeight)
        
    return  intMaxWidth, intMaxHeight

class listBuffer():
    listBuffer = []
    
    def __init__(self, listBufferContent):
        self.listBuffer = listBufferContent
        
    def get_LastItem(self):
        buffer = self.listBuffer[-1]
        self.listBuffer.pop(-1)
        return buffer

# def make_boxColage(listContent):
#     # intConvasWidth, intConvasHeight = get_convasSize(listContent)

#     intConvasWidth, intConvasHeight = 1000, 1000

#     convas = Image.new("RGBA", (intConvasWidth, intConvasHeight))
#     buffer = listBuffer(listContent)
    

    
    
#     for i in range(0,intConvasWidth,intConvasHeight):
#         for j in range(0,intConvasWidth,intConvasHeight):
            
#             try :
#                 img = Image.open(buffer.get_LastItem())
#                 img = img.resize((100,100))
                
#                 filter = ImageEnhance.Brightness(img)
                
                
                
#                 new_img = filter.enhance(1)
#                 convas.paste(new_img, (j,i))
                
#             except Exception:
#                 break
            
#             # c+=0.1
#             # print(c)
#     convas.show()

def qq(listContent):
            
    collage = Image.new("RGBA", (2000,1000))
    buffer = listBuffer(listContent)
    
    
    
    c=0.7
    for i in range(0,2000,500):
        for j in range(0,2000,500):
                
            img = Image.open(buffer.get_LastItem())
            img = img.resize((500,500))
            filter = ImageEnhance.Brightness(img)
            new_img = filter.enhance(c)
            collage.paste(new_img, (j,i))
            c+=0.1
                
    collage.show()
    

def main(strPhotoFolderName = 'photos', ):
    listFolderContent = get_listFolderContent(strPhotoFolderName)
    listImage = get_listOfImage(listFolderContent)
    # make_boxColage(listImage)
    qq(listImage)

main()