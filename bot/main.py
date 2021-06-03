# # our module
# telegram bot
from aiogram.utils import executor
from bot import BotTelegram


def main():
    bot_telegram = BotTelegram()
    executor.start_polling(bot_telegram.disp)


if __name__ == '__main__':
    main()
