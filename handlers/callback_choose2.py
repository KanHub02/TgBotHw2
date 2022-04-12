from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import bot


async def vetka_quiz_mys_1(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_8 = InlineKeyboardButton("Ghost",
                                         callback_data="button_call_8")
    markup.add(button_call_8)
    await bot.send_message(call.message.chat.id, 'Only Ghosts ;3',
                           reply_markup=markup)


async def vetka_quiz_mys_2_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_9 = InlineKeyboardButton("Brown Lady.",
                                         callback_data="button_call_9")
    markup.add(button_call_9)
    await bot.send_message(call.message.chat.id, 'Hm..',
                           reply_markup=markup)


async def vetka_quiz_mys_2_3(call: types.CallbackQuery):
    photo = open('media/ghost.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo)
    await bot.send_message(call.message.chat.id,
                           'Коричневая леди Рейнхэм-холла": этот "призрак" мог образоваться из-за дрожания фотоаппарата во время длинной выдержки')


def register_handler_callback(dp: Dispatcher):
    dp.register_callback_query_handler(vetka_quiz_mys_1,
                                       lambda call: call.data == "button_call_5")

    dp.register_callback_query_handler(vetka_quiz_mys_2_2,
                                       lambda call: call.data == "button_call_8")
    dp.register_callback_query_handler(vetka_quiz_mys_2_3,
                                       lambda call: call.data == "button_call_9")
