from typing import Optional
from sqlalchemy import select

from shared.models import User

from .base_repo import BaseRepository

class UserRepository(BaseRepository):
    
    async def get_user_by_id(self, tg_id: int) -> Optional[User]:
        return await self.session.scalar(select(User).where(User.id == tg_id))
    
    async def create_user(self, tg_id: int, username: str = None) -> User:

        existing = await self.session.scalar(
            select(User).where(User.id == tg_id)
        )

        if existing:
            return existing
        
        user = User(id=tg_id, username=username)

        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user
