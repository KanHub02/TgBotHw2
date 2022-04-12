from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import bot


async def vetka_quiz_space_1(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_11 = InlineKeyboardButton("Черный дыры",
                                          callback_data="button_call_11")
    button_call_12 = InlineKeyboardButton("Квазар",
                                          callback_data="button_call_12")
    markup.add(button_call_11, button_call_12)
    await bot.send_message(call.message.chat.id, 'Космом это интересно',
                           reply_markup=markup)


async def vetka_quiz_space_1_1(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_13 = InlineKeyboardButton('Еще!',
                                          callback_data="button_call_13")
    markup.add(button_call_13)
    photo = open('media/bh.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo)
    await bot.send_message(call.message.chat.id,
                           '"Чёрная дыра́ — область пространства-времени, гравитационное притяжение которой настолько велико, что покинуть её не могут даже объекты, движущиеся со скоростью света!"',
                           reply_markup=markup)


async def vetka_quiz_space_2_1_1(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_14 = InlineKeyboardButton("GN-z11 Galaxy :|",
                                          callback_data="button_call_14")
    button_call_15 = InlineKeyboardButton("Milky Way Galaxy ;)",
                                          callback_data="button_call_15")
    markup.add(button_call_14, button_call_15)
    photo = open('media/kvz.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo)
    await bot.send_message(call.message.chat.id,
                           'Кваза́р — класс астрономических объектов, являющихся одними из самых ярких в видимой Вселенной.',
                           reply_markup=markup)


async def vetka_quiz_space_2_1_2(call: types.CallbackQuery):
    photo = open('media/milkyway.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo)
    await bot.send_message(call.message.chat.id,
                           'Млечный Путь — спиральная галактика, в которой находится Земля и вся Солнечная система. Млечный Путь также называют Галактикой.', )


async def vetka_quiz_space_2_1_3(call: types.CallbackQuery):
    photo = open('media/elder.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo)
    await bot.send_message(call.message.chat.id,
                           ' GN-z11, находящейся на расстоянии 13,37 млрд световых лет от Земли. Она существует со времени, когда Вселенной было 420 млн лет.', )


def register_handler_callback(dp: Dispatcher):
    dp.register_callback_query_handler(vetka_quiz_space_1,
                                       lambda call: call.data == "button_call_6")
    dp.register_callback_query_handler(vetka_quiz_space_1_1,
                                       lambda call: call.data == "button_call_11")
    dp.register_callback_query_handler(vetka_quiz_space_2_1_1,
                                       lambda call: call.data == "button_call_12")
    dp.register_callback_query_handler(vetka_quiz_space_2_1_2,
                                       lambda call: call.data == "button_call_15")
    dp.register_callback_query_handler(vetka_quiz_space_2_1_3,
                                       lambda call: call.data == "button_call_14")
