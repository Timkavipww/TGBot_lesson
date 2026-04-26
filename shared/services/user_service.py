from typing import Optional

from shared.models import User
from shared.repositories import UserRepository


class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    async def get_by_id(self, tg_id: int) -> Optional[User]:
        return await self.user_repo.get_user_by_id(tg_id)

    async def create_user(self, tg_id: int, username: str = None) -> User:
        return await self.user_repo.create_user(
            tg_id=tg_id, 
            username=username, 
        )