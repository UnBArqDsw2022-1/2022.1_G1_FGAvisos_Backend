import sqlalchemy as sa
from sqlalchemy import Column, Integer, ForeignKey

from app.core.config import settings


class AlunoTurmaModel(settings.Base):
    __tablename__ = 'aluno_turma'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_aluno = Column(Integer, ForeignKey('aluno.id'))
    id_turma = Column(Integer, ForeignKey('turma.id'))

    sa.UniqueConstraint(id_aluno, id_turma)