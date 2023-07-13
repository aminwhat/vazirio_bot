import os

import telebot
from dotenv import load_dotenv


def init() -> str:
    load_dotenv()

    BOT_TOKEN = os.environ.get("BOT_TOKEN")

    if BOT_TOKEN == None:
        print("Failed to get the TOKEN from the .env")
        BOT_TOKEN = "6357373883:AAHeHthqvYK0YCiZPk2qAcDtYK8Pv57xfxo"

    print("BOT_TOKEN: " + BOT_TOKEN)
    return BOT_TOKEN


BOT_TOKEN = init()


bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start", "hello"])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
