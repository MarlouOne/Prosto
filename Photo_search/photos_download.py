# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 14:21:42 2022

@author: Marlou
"""

import requests as R
import os
import json

# strURL = 'https://avatars.mds.yandex.net/i?id=1b7f7bdb0615b44e15f6974919eb5f45-5231868-images-thumbs&amp;n=13'
# strName = '1'


# img = R.get(strURL)
# img_option = open(strName +'.jpg', 'wb')
# img_option.write(img.content)
# img_option.close()

def get_dictFromJson(strPath):
    with open(strPath,'r',encoding='utf-8') as file:
        dictData = json.load(file)
        # print(dictData)
        return dictData

def create_NewFolder(strFolderName = 'data'):
    strCurrentPath = os.getcwd()
    
    if not os.path.isdir(strFolderName):
     os.mkdir(strFolderName)
     
    # print('New folder is created and located at ', strCurrentPath + '\\' + strFolderName)
    return strCurrentPath + '\\' + strFolderName

def download_Photos(listURLs, strFolderPath):
    
    intCount = 1
    for strURL in listURLs:
        # print(strURL)
        # print(strFolderPath + '\\' + str(intCount) + '.jpg')
        with open(strFolderPath + '\\' + str(intCount) + '.jpg', 'wb') as file :
            img = R.get(strURL)
            file.write(img.content)
        intCount += 1
            
        

def main(strJSONPath = 'photos.json', strFolderName = 'photos'):
    dictPhotos = get_dictFromJson(strJSONPath)
    strFolderPath = create_NewFolder(strFolderName)
    download_Photos(dictPhotos.values(), strFolderPath)
    
    
main()