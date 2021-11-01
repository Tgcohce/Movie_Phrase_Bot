import telebot
import info
from random import randint

# Import token from the botfather
bot = telebot.TeleBot("TOKEN", parse_mode=None)

cmd_list = "/mphrase - To get a randomized catchphrase from a movie"

url = "https://www.kaggle.com/thomaskonstantin/150-famous-movie-catchphrases-with-context"

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f"Command List: \n {cmd_list} \n /about")

@bot.message_handler(commands=['mphrase'])
def movie_phrase(message):
    y = randint(1, 149)
    bot.reply_to(message, info.mane(y))

@bot.message_handler(commands=['about'])
def send_welcome(message):
    bot.reply_to(message, f" Datasets used: \n\n /mphrase - {url} \n author: Thomas Konstantin")


bot.infinity_polling()