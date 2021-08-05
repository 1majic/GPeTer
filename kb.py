from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from emoji import emojize
posts_cb = CallbackData('post', 'id', 'action')

button_Porfirevich = KeyboardButton('Порфирьевич')
button_Sber = KeyboardButton('GPT3 от Сбера')
button_Balaboba = KeyboardButton('Балабоба')
button_Settings = KeyboardButton('Параметры')
button_TPDNE = KeyboardButton('this person does not exist')

button_change = KeyboardButton('Изменить')
button_cancel = KeyboardButton('Назад')

settings_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(button_cancel, button_change)

choose_ii = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(button_Porfirevich, button_Sber, button_Balaboba).row(button_TPDNE).row(button_Settings)
