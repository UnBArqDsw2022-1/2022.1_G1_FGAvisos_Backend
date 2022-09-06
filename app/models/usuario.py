from sqlalchemy import Column, Integer, String, DateTime

from app.core.config import settings

import datetime


class UsuarioModel(settings.Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(150), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    senha = Column(String(256), nullable=False)
    numero_telefone = Column(String(20))
    dt_nascimento = Column(DateTime)
    created_at = Column(DateTime, default=datetime.datetime.now())