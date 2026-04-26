from infrastructure.database import Base, engine
from shared.utils import logger
from shared.models import *

async def init_models():
    try:
        logger.info(f"Tables in metadata: {list(Base.metadata.tables.keys())}")

        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
            # await conn.run_sync(Base.metadata.drop_all, checkfirst=False) # IF NEED TO RESET DB

        logger.info("[Database] Successfully initialized")
    except Exception as e:
        logger.error(f"[Database] fail to init models: {e}")
        logger.error(f"[Database] Error type: {type(e)}")
        raise
