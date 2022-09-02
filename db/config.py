from pydantic import BaseSettings

from sqlalchemy.orm import declarative_base


class Settings(BaseSettings):

    Base = declarative_base()
    
    user = 'postgres'
    password = 'postgres'
    host = 'fgaaviso_db'

    DB_URL: str = f'postgresql+asyncpg://{user}:{password}@{host}:5432/fgavisos'


    class Config:
        case_sensitive = True

settings: Settings() = Settings()