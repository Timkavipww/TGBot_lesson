from pydantic_settings import BaseSettings

# from dotenv import load_dotenv
# load_dotenv() # FOR TESTING | NO NEED IN DOCKER

class Config(BaseSettings):
    BOT_TOKEN: str
    DATABASE_URL: str

    _env_file = ".env"

    
config = Config()
