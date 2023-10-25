from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def example_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("Option 1", callback_data="1"),
            InlineKeyboardButton("Option 2", callback_data="2"),
        ],
        [InlineKeyboardButton("Option 3", callback_data="3")],
    ]
    return InlineKeyboardMarkup(keyboard)
