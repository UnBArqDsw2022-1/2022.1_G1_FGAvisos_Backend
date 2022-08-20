from enum import unique
from sqlalchemy import Column, Integer, ForeignKey

from db.config import settings


class AlunoPossuiTurma(settings.Base):
    __tablename__ = 'aluno_turma'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_aluno = Column(Integer, ForeignKey('aluno.id'), unique=True)
    id_turma = Column(Integer, ForeignKey('turma.id'), unique=True)