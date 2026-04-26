from contextlib import asynccontextmanager
from app.handlers import router
from shared.utils import logger, setup_logger, init_models
from app.bot import dp

@asynccontextmanager
async def app_lifespan():
    setup_logger()
    await init_models()
    
    dp.include_router(router)
    try: 
        yield
    except Exception as ex:
        logger.exception(ex)