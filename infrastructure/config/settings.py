from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    BOT_TOKEN: str
    DATABASE_URL: str

    _env_file = ".env"

config = Settings()
