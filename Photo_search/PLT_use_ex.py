# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 17:50:14 2022

@author: Marlou
"""

import os

import PIL.Image as Image

IMAGES_PATH = 'C:\\Users\\major\\Documents\\GitHub\\CopyScript\\Prosto\\Photo_search\\photos\\'  # Адрес коллекции изображений
IMAGES_FORMAT = ['.jpg', '.JPG']  # Формат изображения
IMAGE_SIZE = 256  # Размер каждой маленькой картинки
IMAGE_ROW = 2  # Интервал картинки, то есть после объединения в одну картинку получается всего несколько строк
IMAGE_COLUMN = 2  # Картинка интервал, то есть после слияния в одну картинку получается всего несколько столбцов
IMAGE_SAVE_PATH = r'C:\Users\major\Documents\GitHub\CopyScript\Prosto\Photo_search\final.jpg'  # Адрес после преобразования изображения

# Получить все имена изображений под адресом коллекции изображений
image_names = [name for name in os.listdir(IMAGES_PATH) for item in IMAGES_FORMAT if
               os.path.splitext(name)[1] == item]

print("image_names", image_names)
# Простая количественная оценка настройки параметров и размера фактической коллекции изображений
if len(image_names) != IMAGE_ROW * IMAGE_COLUMN:
    raise ValueError("Параметры составного изображения не могут соответствовать необходимому количеству!")


# Определить функцию сшивания изображений
def image_compose():
    to_image = Image.new('RGB', (IMAGE_COLUMN * IMAGE_SIZE, IMAGE_ROW * IMAGE_SIZE))  # Создать новую картинку
    # Прокрутите, вставьте каждое изображение по порядку в соответствующую позицию
    for y in range(1, IMAGE_ROW + 1):
        for x in range(1, IMAGE_COLUMN + 1):
            from_image = Image.open(IMAGES_PATH + image_names[IMAGE_COLUMN * (y - 1) + x - 1]).resize(
                (IMAGE_SIZE, IMAGE_SIZE), Image.ANTIALIAS)
            to_image.paste(from_image, ((x - 1) * IMAGE_SIZE, (y - 1) * IMAGE_SIZE))
    return to_image.save(IMAGE_SAVE_PATH)  # Сохранить новое изображение


image_compose()  # Функции вызова