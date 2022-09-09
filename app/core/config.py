from pydantic import BaseSettings

from sqlalchemy.orm import declarative_base

from dotenv import load_dotenv

import os


class Settings(BaseSettings):
    load_dotenv()

    Base = declarative_base()
    
    USER = os.getenv("USER_DB")
    PASSWORD = os.getenv("PASSWORD")
    HOST = os.getenv("HOST")
    JWT_SECRET: str = os.getenv("JWT_KEY")
    DB: str = os.getenv("DB")
    PORT: str = os.getenv("PORT")

    DB_URL: str = f'postgresql+asyncpg://{USER}:{PASSWORD}@{HOST}/{DB}'

    if PORT != "":
        DB_URL = f"postgresql+asyncpg://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"


    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60*24*7 # uma semana

    class Config:
        case_sensitive = True

settings: Settings = Settings()