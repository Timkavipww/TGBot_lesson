from aiogram import Dispatcher
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app.middlewares import DbSessionMiddleware

def register_middlewares(
    dp: Dispatcher,
    async_session_maker: async_sessionmaker[AsyncSession],
):
    dp.update.middleware(DbSessionMiddleware(async_session_maker))