# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 11:16:10 2022

@author: Marlou
"""

import telebot
import photo_search
import photos_download
import simple_calage




bot = telebot.TeleBot('1783334306:AAF2tQGG8wO09U_eqqIxoBwQuSZ9fwicka0')

bot.polling(none_stop=True, interval=0)


@bot.message_handler(content_types=['text'])

def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Заряжай");
        bot.register_next_step_handler(message, main); #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши /go');



def main(message):
    photo_search.main(message)
    photos_download.main()
    simple_calage.main('photos\\',  150, 2, 2, 'final_calage.jpg')
    bot.send_photo('final_calage.jpg')