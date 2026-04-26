from sqlalchemy.ext.asyncio import AsyncSession
from infrastructure.database import UserRepository
from application.services import UserService

class Container:
    def __init__(self, session: AsyncSession):
        self.session = session

        self._user_repo = UserRepository(session)
        self._user_service = UserService(self._user_repo)

    @property
    def user_service(self):
        return self._user_service