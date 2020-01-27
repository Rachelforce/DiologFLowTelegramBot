import telebot
import analysis
import config
import diaoloflowAPI


bot = telebot.TeleBot(config.Config.BOT_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    analysis.user_save(message.from_user)
    bot.reply_to(message, "Connect")


@bot.message_handler(func=lambda message: message)
def echo_all(message):
    analysis.user_save(message.from_user.to_json())
    bot.reply_to(message, diaoloflowAPI.get_response(message.text, message.chat.id))


bot.polling()
