from telegram.ext import Application, MessageHandler, filters
from django.conf import settings


async def log_update(update):
    print(f"Received update: {update}")


application = Application.builder().token(settings.TELEGRAM_BOT_TOKEN).build()
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, log_update))
