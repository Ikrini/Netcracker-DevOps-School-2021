"""
class telegram bot
"""

# # library
# api telegram
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from time import sleep


# # our module
# telegram's api token
try:
    from config import token
except ImportError:
    from config_k8s import token
from chatbot import ChatBot


class FormLanguages(StatesGroup):
    language = State()


class FormTraining(StatesGroup):
    training = State()


def _get_version() -> str:
    """
    get version from version.txt
    :return: bot version
    """

    try:
        with open('version.txt', 'r') as file:
            result = file.read()
    except FileNotFoundError:
        with open('version_k8s.txt', 'r') as file:
            result = file.read()

    return result


class BotTelegram(object):

    def __init__(self):
        self.version = _get_version()
        self.bot = Bot(token=token)
        self.disp = Dispatcher(self.bot, storage=MemoryStorage())

        self.chat_bot = ChatBot()

        @self.disp.message_handler(commands=['start', 'help'])
        async def process_help_command(message: types.Message):
            mes = 'Chat bot with training function for DevOps course project\n\n' \
                  '*Standard command:*\n' \
                  '/start - Beginning of work\n' \
                  '/help - Command help display\n' \
                  '/version - Shows the bot version\n\n' \
                  '*Bot Settings*:\n' \
                  '/changelanguage - Change the language of communication\n\n' \
                  '*Train*:\n' \
                  '/showtraining - Show content intense.json\n' \
                  '/addtraining - Add value for learning\n' \
                  '/training - Start training'

            await message.bot.send_message(message.from_user.id, mes, parse_mode='Markdown')

        @self.disp.message_handler(commands=['version'])
        async def show_version_command(message: types.Message):
            mes = f'Bot version: {self.version}'

            await message.bot.send_message(message.from_user.id, mes)

        @self.disp.message_handler(commands=['changelanguage'])
        async def change_languages(message: types.Message):
            """
            Change our language
            """

            await FormLanguages.language.set()
            await self.bot.send_message(message.from_user.id, f'Active language: {self.chat_bot.language}\n'
                                                              f'Our language: {self.chat_bot.get_languages()}\n'
                                                              f'What language do you need?')

        @self.disp.message_handler(state=FormLanguages.language)
        async def enter_language(message: types.Message, state: FSMContext):
            await self.bot.send_message(message.from_user.id, self.chat_bot.change_language(message.text))
            await state.finish()

        @self.disp.message_handler(commands=['showtraining'])
        async def show_training(message: types.Message):
            """
            Show intense.json
            """

            message_arr = self.chat_bot.get_training()

            mes = ''
            length = len(mes)
            i = 0
            end = False
            send = True  # if it did not go beyond the limits
            for elem in message_arr:
                # limit on the number of messages per second
                if end and i % 15 == 0 and i != 0:
                    end = False
                    sleep(3)
                len_mes = len(elem)
                # limit on characters per message
                if len_mes + length < 4096:
                    mes += elem
                    length += len_mes
                else:
                    send = False
                    end = True
                    i += 1

                    await self.bot.send_message(message.from_user.id, mes)
                    mes = ''
                    length = 0
            if send:
                if mes != '':
                    await self.bot.send_message(message.from_user.id, mes)

        @self.disp.message_handler(commands=['addtraining'])
        async def add_training(message: types.Message):
            """
            Add intent in training
            """

            await FormTraining.training.set()
            mes = 'Input format:\n' \
                  '<language>:<tag>:<pat or res (pat - pattern (man writes), res - response (the bot answers))>:' \
                  '<text>\n' \
                  'Example 1:\n' \
                  'en:greeting:pat:whats up\n' \
                  'Example 2:\n' \
                  'en:greeting:res:Hey!\n' \
                  'Example 3:\n' \
                  'ru:возраст:res:мне 20 лет\n'
            await self.bot.send_message(message.from_user.id, mes)

        @self.disp.message_handler(state=FormTraining.training)
        async def enter_training(message: types.Message, state: FSMContext):
            await self.bot.send_message(message.from_user.id, self.chat_bot.add_training(message.text))
            await state.finish()

        @self.disp.message_handler(commands=['training'])
        async def training_go(message: types.Message):
            """
            Start learning
            """

            await self.bot.send_message(message.from_user.id, self.chat_bot.training())

        @self.disp.message_handler()
        async def echo_message(message: types.Message):
            intents = self.chat_bot.predict_class(message.text.lower())
            await self.bot.send_message(message.from_user.id, self.chat_bot.get_response(intents,
                                                                                         self.chat_bot.intents))
