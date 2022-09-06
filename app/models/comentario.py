from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from app.core.config import settings

import datetime


class ComentarioModel(settings.Base):
    __tablename__ = 'comentario'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_aviso = Column(Integer, ForeignKey('aviso.id'))
    autor_aluno = Column(Integer, ForeignKey('aluno.id'))
    autor_professor = Column(Integer, ForeignKey('professor.id'))
