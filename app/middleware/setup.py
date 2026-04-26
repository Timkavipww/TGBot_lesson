from aiogram import Dispatcher
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from .db_session_middleware import DbSessionMiddleware
from .service_middleware import ServiceMiddleware

def register_middlewares(
    dp: Dispatcher,
    async_session_maker: async_sessionmaker[AsyncSession],
):
    dp.update.middleware(DbSessionMiddleware(async_session_maker))
    dp.update.middleware(ServiceMiddleware())