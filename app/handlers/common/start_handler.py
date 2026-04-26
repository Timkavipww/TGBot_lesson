from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from infrastructure import logger

from app.di.container import Container

router = Router()

@router.message(CommandStart())
async def cmd_start(
    message: Message,
    container: Container,
):

    tg_id = message.from_user.id

    user = await container.user_service.get_by_id(tg_id)
    if user:
        logger.info("[start handler] user from db")
        await message.answer(f'Hello, {user.username}')
        return
    
    else:
        logger.info("[start handler] user created")
        user = await container.user_service.create_user(tg_id, message.from_user.username)
        await message.answer(f'Hello, {user.username}')
        return
