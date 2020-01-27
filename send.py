import telebot
import config

bot = telebot.TeleBot(config.Config.BOT_TOKEN)
message = input()
while message != '0':
    bot.send_message(704159189, message)
    message = input()
