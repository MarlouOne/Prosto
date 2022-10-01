
import requests as R
from bs4 import BeautifulSoup as BS
from fake_useragent import UserAgent
import re

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

    
def getSoup(strURL, strTagName='img' ,strClassName = 'serp-item__thumb justifier__thumb'):
    response = R.get(strURL, headers={'User-Agent': UserAgent().chrome})
    soup = BS(response.content, "html.parser")
    elementsOfSoup = soup.find_all(strTagName, class_= strClassName)
    
    for element in elementsOfSoup:
        # print(element)
        get_subtext(str(element),'src')
        
    
        
    return soup

def get_subtext(strText, strPattern):
    intFirstIndex = strText.find(strPattern)
    # print(strText[intFirstIndex:])
    intSecondIndex = intFirstIndex + strText[intFirstIndex:].find('"')+1
    # print(strText[intSecondIndex:])
    intLastIndex = intSecondIndex + strText[intSecondIndex:].find('"')
    # print(strText[intSecondIndex:intLastIndex])
    print('https:' + strText[intSecondIndex:intLastIndex])
    return 'https:' + strText[intSecondIndex:intLastIndex]

def main(strText):
    strText = 'https://yandex.ru/images/search?from=tabbar&text=' + strText
    # print(strText)
    getSoup(strText)
    
main('олег')

# def get_url(strText):
    
#     r = requests.get("https://yandex.ru/images/search?text=олег")
#     soup = BeautifulSoup(r.content)
#     print(soup)

# def main(strText):
#     get_url(strText)

# https://yandex.ru/images/search?text=олег
# main('oleg')



# class data():
#     strURL : str
#     soup : None
#     listPhotoLinks = []
    
#     def __init__(self, strURL):
#         self.strURL = strURL
#         self.getSoup()
    
#     def getSoup(self):
#         response = R.get(self.strURL, headers={'User-Agent': UserAgent().chrome})
#         self.soup = BS(response.content, "html.parser")
#         print(self.soup)
    
#     def getClassContent(self, strTagName = 'img', strClassName = 'MMImage-Origin'):
#         soupTitle = self.soup.find_all(strTagName, class_=strClassName)
#         for element in soupTitle:
#             print(element)

# def main(strText):
#     strText = 'https://yandex.ru/images/search?from=tabbar&text=' + strText
#     dataOBj = data(strText)
#     dataOBj.getSoup()
#     dataOBj.getClassContent()
    