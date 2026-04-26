import asyncio
from contextlib import asynccontextmanager
from app.bot import bot, dp
from shared.utils import logger, setup_logger
from app.handlers import router

@asynccontextmanager
async def app_lifespan():
    
    setup_logger()
    dp.include_router(router)
    try: 
        yield
    except Exception as ex:
        logger.exception(ex)

async def main():
    async with app_lifespan():
        await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.warning("Выключен вручную")