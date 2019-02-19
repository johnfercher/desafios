import subprocess
from subprocess import run, PIPE
import telebot

token = "739503645:AAH25It8nhC4sSUNGsn_LMNAevuyRFZ1aQs"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['NadaPraFazer'])
def send_welcome(message):
    args = message.text.split(" ")[1]

    command = 'scrapy crawl votes -s LOG_ENABLED=False -a subs=' + args
    output = subprocess.getoutput(command)

    bot.reply_to(message, output)


bot.polling()
