from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from shared.core import config
from aiogram.enums import ParseMode

bot = Bot(
    token=config.BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher()