from aiogram import BaseMiddleware
from sqlalchemy.ext.asyncio import AsyncSession

from shared.repositories import UserRepository
from shared.services import UserService

class ServiceMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        session: AsyncSession = data.get("session")

        if session:

            user_repo = UserRepository(session)
            data["user_service"] = UserService(user_repo)

        return await handler(event, data)