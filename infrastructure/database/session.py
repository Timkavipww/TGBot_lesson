from infrastructure import config
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

engine = create_async_engine(config.DATABASE_URL, echo=False)

async_session_maker: async_sessionmaker[AsyncSession] = async_sessionmaker(
    engine, 
    class_=AsyncSession, 
    expire_on_commit=False
)
