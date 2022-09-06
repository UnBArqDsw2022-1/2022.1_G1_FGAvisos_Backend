from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from core.config import settings

import datetime

class AvisoModel(settings.Base):
    __tablename__ = 'aviso'

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(30), nullable=False)
    corpo = Column(String(2000), nullable=False)
    autor = Column(Integer, ForeignKey('professor.id'), nullable=False)
    tag = Column(String(20))
    created_at = Column(DateTime, default=datetime.datetime.now())
    turma = Column(Integer, ForeignKey('turma.id'), nullable=False)