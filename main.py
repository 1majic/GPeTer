from aiogram import Bot, Dispatcher, executor, types
from time import sleep
from aiogram.types import ParseMode
from emoji import emojize
from aiogram.types import callback_query

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from aiogram.dispatcher.filters.state import StatesGroup, State
import Balaboba_generator
import Porfirevich_generator
import SberGPT3_generator
import TPDNE_generator
import kb

API_TOKEN = "1896637723:AAEQfju2nNVxtxAaFhpdgLk8acKUaLpNWZ4"

bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())
Gen = ''
words = 60


class GeneratorsStates(StatesGroup):
    TEXT_STATE = State()
    DEFAULT_STATE = State()
    SETTINGS_STATE = State()


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Выбери Нейросеть', reply_markup=kb.choose_ii)
    await GeneratorsStates.DEFAULT_STATE.set()


@dp.message_handler(state=GeneratorsStates.TEXT_STATE)
async def loading(message: types.Message):
    msg = await message.answer('Загрузка...')
    text = await getText(message.text)
    await msg.edit_text(text)


@dp.message_handler(lambda message: message.text == "Порфирьевич" or message.text == "GPT3 от Сбера" or message.text == "Балабоба", state=GeneratorsStates.DEFAULT_STATE)
async def TextGenerators(message: types.Message):
    await message.answer("Придумай начало истории")
    await GeneratorsStates.TEXT_STATE.set()
    global Gen
    if message.text == "Порфирьевич":
        Gen = 'P'
    elif message.text == "GPT3 от Сбера":
        Gen = 'S'
    elif message.text == "Балабоба":
        Gen = 'B'


@dp.message_handler(lambda message: message.text == "this person does not exist", state=GeneratorsStates.DEFAULT_STATE)
async def ImageGenerators(message: types.Message):
    await bot.send_photo(message.from_user.id, TPDNE_generator.makeRequest())


@dp.message_handler(lambda message: message.text == "Параметры", state=GeneratorsStates.DEFAULT_STATE)
async def Settings(message: types.Message):
    global words
    await message.answer(f"Текущие настройки:\nПорфирьевич:{words}", reply_markup=kb.settings_kb)


@dp.message_handler(lambda message: message.text == "Изменить", state=GeneratorsStates.DEFAULT_STATE)
async def change(message: types.Message):
    # await bot.answer_callback_query(query.id)
    await message.answer('Введите новое значение от 1 до 150')
    await GeneratorsStates.SETTINGS_STATE.set()


@dp.message_handler(lambda message: message.text != 'Введите новое значение от 1 до 150', state=GeneratorsStates.SETTINGS_STATE)
async def newWordsValue(message: types.Message):
    global words
    text = message.text
    if text.isdigit():
        if 0 < int(text) < 151:
            words = int(text)
        elif int(text) > 150:
            words = 150
        elif int(text) < 0:
            words = 1
        await GeneratorsStates.DEFAULT_STATE.set()
        await Settings(message)
    else:
        await message.answer('Введите новое значение от 1 до 150')


# @dp.callback_query_handler(func=lambda c: c.data == 'variant')
# async def anotherVariant(callback_query: types.CallbackQuery):
#     loading()

@dp.message_handler(lambda message: message.text == "Назад", state=GeneratorsStates.DEFAULT_STATE)
async def cancel(message: types.Message):
    await start(message)


async def getText(text):
    global Gen, words
    if Gen == 'P':
        await GeneratorsStates.DEFAULT_STATE.set()
        return Porfirevich_generator.makeRequest(text, words)
    elif Gen == 'S':
        await GeneratorsStates.DEFAULT_STATE.set()
        return SberGPT3_generator.makeRequest(text)
    elif Gen == 'B':
        await GeneratorsStates.DEFAULT_STATE.set()
        return Balaboba_generator.makeRequest(text)


async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


if __name__ == '__main__':
    executor.start_polling(dp, on_shutdown=shutdown)
