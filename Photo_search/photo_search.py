
import requests as R
from bs4 import BeautifulSoup as BS
from fake_useragent import UserAgent
# import re
# import os
import json
from random import randint

class photo():
    strName : str
    strURL  : str
    
    def __init__(self, strName, strURL):
        self.strName = strName
        self.strURL  = strURL
    
    def get_name(self):
        return self.strName
    
    def get_URL(self):
        return self.strURL
    
    def print_info(self):
        print(self.strName)
        print(self.strURL)
        
    
# 'MMImage-Origin'
# 'serp-item__thumb justifier__thumb'
    
def get_Photos_objs(strURL, strTagName='img' ,strClassName = 'serp-item__thumb justifier__thumb'):
    response = R.get(strURL, headers={'User-Agent': UserAgent().chrome})
    # print(response)
    soup = BS(response.content, "html.parser")
    # print(soup)
    elementsOfSoup = soup.find_all(strTagName, class_= strClassName)
    # print(elementsOfSoup)

    listPhotoObjs = []    
    
    for element in elementsOfSoup:
        # print(element)
        # get_subtext(str(element),'src')
        subPhoto = photo(get_subtext(str(element), 'alt'),'https:' + get_subtext(str(element), 'src'))
        # subPhoto.print_info()
        listPhotoObjs.append(subPhoto)
        
    return listPhotoObjs

def dictFromList(listPhotoObjs):
    dictPhotoObjs = {}
    for Obj in listPhotoObjs:
        dictPhotoObjs[Obj.get_name()] = Obj.get_URL()
        
    # print(dictPhotoObjs)
    return dictPhotoObjs


def get_subtext(strText, strPattern):
    intFirstIndex = strText.find(strPattern)
    # print(strText[intFirstIndex:])
    intSecondIndex = intFirstIndex + strText[intFirstIndex:].find('"')+1
    # print(strText[intSecondIndex:])
    intLastIndex = intSecondIndex + strText[intSecondIndex:].find('"')
    # print(strText[intSecondIndex:intLastIndex])
    # print(strText[intSecondIndex:intLastIndex])
    return strText[intSecondIndex:intLastIndex]

def get_oldJSONContent(strPath):
    with open(strPath, "r", encoding='utf-8') as file:
        dictData = json.load(file)
        # print(dictData)
    return dictData



def create_json_file(dictContent ,strPath = ''):
    
    try:
        dictOldData = get_oldJSONContent(strPath)
        dictContent = dict(list(dictOldData.items()) + list(dictContent.items()))
    except Exception:
        print('No old content')
    
    with open(strPath, "w",encoding='utf-8') as file:
        json.dump(dictContent, file, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))


def get_randomDict(dictContent):
    strKeys = list(dictContent)[randint(0,len(list(dictContent)))]
    return {strKeys:dictContent[strKeys]}

def main(strText, strPath = "photos.json"):
    strText = 'https://yandex.ru/images/search?from=tabbar&text=' + strText
    # print(strText)

    listPhotoObjs = get_Photos_objs(strText)
    dictPhotoObjs = dictFromList(listPhotoObjs)
    dictPhotoObj = get_randomDict(dictPhotoObjs)
    create_json_file(dictPhotoObj, strPath)
    
    
main('олег')