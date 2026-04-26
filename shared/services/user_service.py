from typing import List, Optional

from shared.models import User
from shared.repositories import UserRepository


class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    async def get_by_id(self, user_id: str) -> Optional[User]:
        return await self.user_repo.get_user_by_id(user_id)

    async def create_user(self, telegram_id: int, username: str = None) -> User:
        return await self.user_repo.create_user(
            tg_id=telegram_id, 
            username=username, 
        )