from django.conf import settings
from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

bot = Bot(token=settings.TELEGRAM_TOKEN)
updater = Updater(token=settings.TELEGRAM_TOKEN, use_context=True)
dispatcher = updater.dispatcher

from .handlers import start, handle_message, handle_callback

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
dispatcher.add_handler(CallbackQueryHandler(handle_callback))

def run_bot():
    updater.start_polling()
    updater.idle()
