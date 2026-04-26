import asyncio

from shared.utils import logger

from app.bot import bot, dp
from app.lifespan import app_lifespan

async def main():
    async with app_lifespan():
        await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.warning("Выключен вручную")