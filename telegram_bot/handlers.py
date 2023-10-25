from telegram import Update
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! I am your bot.")


def handle_message(update: Update, context: CallbackContext):
    text_received = update.message.text
    update.message.reply_text(f"You said: {text_received}")


def handle_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=f"Selected option: {query.data}")
