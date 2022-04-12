from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode

from config import bot


async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton('Следующий вопрос',
                                         callback_data="button_call_2")
    markup.add(button_call_1)
    question = 'В каком году была сделана первая фотография черной дыры?'
    answers = [
        '2019, 10 april',
        '2003, 2 november',
        '1989, 21 december',
        '2012, 21 decebmer',
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="10 апреля 2019 года впервые была «сфотографирована» сверхмассивная чёрная дыра в центре галактики Messier 87",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup,
    )


async def quiz_3(call: types.CallbackQuery):
    question = "Results of print:"
    answers = [
        "1",
        "2",
        "3",
        "4",
        "-1"
    ]
    photo = open("media/flex1.jpg", "rb")
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="This is too easy for explanation",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
    )

def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2,
                                       lambda call: call.data == "button_call_1")
    dp.register_callback_query_handler(quiz_3,
                                       lambda call: call.data == "button_call_2")
