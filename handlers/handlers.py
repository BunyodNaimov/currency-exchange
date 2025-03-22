from aiogram import Router, types
from aiogram.filters import CommandStart

from handlers.keyboards import start_button

router = Router()

@router.message(CommandStart())
async def command_start(message: types.Message):
    await message.answer(text="Assalomu Aleykum!\n"
                              "Valyuta Ayirboshlash botiga xush kelibsiz",
                         reply_markup=start_button)

