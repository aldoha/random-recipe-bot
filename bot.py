import os

import telebot
from dotenv import load_dotenv
from telebot import types

from random_link import choose_one
from data.recipe_types import meal

load_dotenv('.env')
TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)


def keyboard_markup(button_text_1, button_text_2):
    markup = types.ReplyKeyboardMarkup(
        one_time_keyboard=True, resize_keyboard=True
    )
    itembtn1 = types.KeyboardButton(button_text_1)
    itembtn2 = types.KeyboardButton(button_text_2)
    markup.add(itembtn1, itembtn2)
    return markup


@bot.message_handler(commands=['start'])
@bot.message_handler(regexp='yasss')
def choose_recipe_type_step(message):
    chat_id = message.chat.id
    msg = bot.send_message(
        chat_id, text="which one?", reply_markup=keyboard_markup('main dish', 'breakfast')
    )
    bot.register_next_step_handler(msg, choose_recipe_step)


def choose_recipe_step(message):
    chat_id = message.chat.id
    recipe = choose_one(meal[message.text])
    bot.send_message(chat_id, recipe)
    bot.send_message(
        chat_id, text="another one?", reply_markup=keyboard_markup('yasss', 'no')
    )


bot.polling(timeout=30)
