from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def log(update: Update, context: CallbackContext, text):
    file = open('C:\\Users\\Asus\\Downloads\\GeekBrains\\Python\\Семинары\\Seminar 10\\Calculator\\db.csv', 'a')
    file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {text}\n')
    file.close()
