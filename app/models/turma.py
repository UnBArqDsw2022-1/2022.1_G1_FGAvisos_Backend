from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from app.core.config import settings

import datetime


class TurmaModel(settings.Base):
    __tablename__ = 'turma'

    id = Column(Integer, primary_key=True, autoincrement=True)
    professor = Column(Integer, ForeignKey('professor.id'))
    ano = Column(Integer, nullable=False)
    semestre = Column(Integer, nullable=False)
    nome_disciplina = Column(String(75))
    created_at = Column(DateTime, default=datetime.datetime.now())