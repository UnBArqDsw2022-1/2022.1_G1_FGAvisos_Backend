from src.models.usuario import UsuarioModel

from sqlalchemy import Column, BigInteger


class AlunoModel(UsuarioModel):
    __tablename__ = 'aluno'

    matricula = Column(BigInteger, nullable=False)