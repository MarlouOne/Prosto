
import requests as R
from bs4 import BeautifulSoup as BS
from fake_useragent import UserAgent
# import re
# import os
import json

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


def create_json_file(dictContent ,strPath = ''):
    # json_string = json.dumps(dictContent, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))
    # print(json_string)
    
    if strPath == '':
        with open("photos.json", "w+",encoding='utf-8') as file:
            # json.dumps(dictContent, file, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))
            json.dump(dictContent, file, indent=4, ensure_ascii=False)
    else:
        with open(strPath, 'w', encoding='utf-8') as file:
            json.dump(dictContent, file, indent=4, ensure_ascii=False)
    

def main(strText):
    strText = 'https://yandex.ru/images/search?from=tabbar&text=' + strText
    # print(strText)

    listPhotoObjs = get_Photos_objs(strText)
    dictPhotoObjs = dictFromList(listPhotoObjs)
    create_json_file(dictPhotoObjs)
    
    
main('олег')