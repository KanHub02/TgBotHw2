
from aiogram.utils import executor

from handlers import callback, client, extra, cllback_choose1, callback_choose2
from config import bot, dp
client.register_handlers_client(dp)
cllback_choose1.register_handler_callback(dp)
callback_choose2.register_handler_callback(dp)
callback.register_handlers_callback(dp)
extra.register_handlers_other(dp)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
