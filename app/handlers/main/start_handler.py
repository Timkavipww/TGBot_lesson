from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from shared.services import UserService
from shared.utils import logger

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message, user_service: UserService):

    tg_id = message.from_user.id

    user = await user_service.get_by_id(tg_id)
    if user:
        logger.info("[start handler] user from db")
        await message.answer(f'Hello, {user.username}')
        return
    
    else:
        logger.info("[start handler] user created")
        user = await user_service.create_user(tg_id, message.from_user.username)
        await message.answer(f'Hello, {user.username}')
        return
