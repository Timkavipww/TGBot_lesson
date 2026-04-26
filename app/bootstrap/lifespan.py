from contextlib import asynccontextmanager

from infrastructure import logger, setup_logger
from infrastructure.database import async_session_maker, init_models

from app.bootstrap.bot import dp
from .middlewares import register_middlewares
from .handlers import router

@asynccontextmanager
async def app_lifespan():
    setup_logger()
    await init_models()
    register_middlewares(dp, async_session_maker)

    dp.include_router(router)
    try: 
        yield
    except Exception as ex:
        logger.exception(ex)