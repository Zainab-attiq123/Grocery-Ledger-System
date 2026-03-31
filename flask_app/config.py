import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./store.db")
    SECRET_KEY = os.getenv("SECRET_KEY", "mysecret")
    DEBUG = os.getenv("DEBUG", "True")

settings = Settings()