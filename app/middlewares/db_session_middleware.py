from aiogram import BaseMiddleware
from app.di import Container

class DbSessionMiddleware(BaseMiddleware):
    def __init__(self, session_maker):
        self.session_maker = session_maker

    async def __call__(self, handler, event, data):
        async with self.session_maker() as session:
            data["container"] = Container(session)
            return await handler(event, data)