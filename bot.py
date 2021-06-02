"""
class telegram bot
"""

# # library
# api telegram
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
# api chat bot
# from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer

# # our module
# telegram's api token
from config import token


class BotTelegram(object):

    def __init__(self):
        self.bot = Bot(token=token)
        self.disp = Dispatcher(self.bot)

        # self.chat_bot = ChatBot('Netcracker',
        #                         storage_adapter='chatterbot.storage.SQLStorageAdapter',
        #                         database_uri='sqlite:///database.sqlite3'
        #                         )
        # conversation = [
        #     "Hello",
        #     "Hi there!",
        #     "How are you doing?",
        #     "I'm doing great.",
        #     "That is good to hear",
        #     "Thank you.",
        #     "You're welcome."
        # ]
        #
        # trainer = ListTrainer(self.chat_bot)
        #
        # trainer.train(conversation)

        @self.disp.message_handler(commands=['start'])
        async def process_start_command(message: types.Message):
            await message.reply("Привет!\nНапиши мне что-нибудь!")

        @self.disp.message_handler()
        async def echo_message(msg: types.Message):
            await self.bot.send_message(msg.from_user.id, msg.text)
