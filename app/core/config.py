from pydantic import BaseSettings

from sqlalchemy.orm import declarative_base


class Settings(BaseSettings):

    Base = declarative_base()
    
    user = 'postgres'
    password = 'postgres'
    host = 'fgaaviso_db'

    DB_URL: str = f'postgresql+asyncpg://{user}:{password}@{host}/fgavisos'

    JWT_SECRET: str = "fc05c7570c34597ddbf3a010cedd9247d5839bd74b6c5f96f770ed4b0f4dc8ff"
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60*24*7 # uma semana

    class Config:
        case_sensitive = True

settings: Settings = Settings()