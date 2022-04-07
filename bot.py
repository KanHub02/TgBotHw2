from aiogram import types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode

from main import bot, dp


@dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"Hello bro\nYou are welcome")


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.reply("Commands list:\n/start\n/quiz")

@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("Следующая Викторина",
                                         callback_data="button_call_1")
    markup.add(button_call_1)
    question = "Python in IT is"
    answers = [
        "Snake", "reptile", "Nuclear Weapon", "programming language", "Obama"
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="Python is PL",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup,
    )


@dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("Следующая Викторина",
                                         callback_data="button_call_2")
    markup.add(button_call_2)
    question = "By who invented Python"
    answers = [
        "Obama",
        "Putin",
        "Trump",
        "Medovodov",
        "Linus Torvalds",
        "Guido Van Rossum",
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=5,
        explanation="Python was created by Guido Van Rossum",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup,
    )
@dp.callback_query_handler(lambda call: call.data == "button_call_2")
async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton("Следующая Викторина",
                                         callback_data="button_call_3")
    markup.add(button_call_3)
    question = "Lambda is?"
    answers = [
        "Obama",
        "Putin",
        "def func",
        "anonimus func",
        "print",
        "class",
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="Lambda Function, also referred to as 'Anonymous function'",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup,
    )

@dp.callback_query_handler(lambda call: call.data == "button_call_3")
async def quiz_4(call: types.CallbackQuery):
    question = "Results of print:"
    answers = [
        "With lambda y:y + y, list[x]",
        "list1 + list2",
        "print(list1+list2)",
        "def sum_slt(lst):\nsum = lst + lst\nprint(sum)",
        "print(list1 = (list+ list2 + list3) * 2"

    ]
    photo = open('media/flex1.png', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="This is too easy for explanation",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
    )

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)