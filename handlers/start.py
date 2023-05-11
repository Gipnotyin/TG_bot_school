from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from keyboard.keyboard import create_inline_kb
from database.database import is_user

router: Router = Router()


@router.message(Command(commands=['start']))
async def info(message: Message):
    await message.answer(
        text='Давай перейдем к регистрации!',
        reply_markup=await create_inline_kb(1, **{"register": "Регистрация"}))


@router.message(Command(commands=['update']))
async def update(message: Message):
    if await is_user(message.from_user.id):
        await message.answer(
            text='Можно обновить свои данные',
            reply_markup=await create_inline_kb(1, **{'update': 'Обновить'})
        )
    else:
        await message.answer(
            text='Вы не зарегистрированы, хотите пройти регистрацию?',
            reply_markup=await create_inline_kb(1, **{"register": "Регистрация"})
        )

