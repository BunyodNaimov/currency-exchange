from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_button = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="🇺🇿 ➡️ 💲"),
     KeyboardButton(text="💲 ➡️ 🇺🇿")]
], resize_keyboard=True)