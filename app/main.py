import asyncio

from infrastructure import logger

from app.bootstrap import app_lifespan, bot, dp



async def main():
    async with app_lifespan():
        await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.warning("Выключен вручную")