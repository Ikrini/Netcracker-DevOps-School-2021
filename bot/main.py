# # our module
# telegram bot
from aiogram.utils import executor
from bot import BotTelegram
import os
from flask import Flask

PORT = int(os.environ.get('PORT', 8080))

def main():
    bot_telegram = BotTelegram()
    executor.start_polling(bot_telegram.disp)

app = Flask(__name__)

@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    return "Hello {}!".format(name)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

#if __name__ == '__main__':
#    main()
