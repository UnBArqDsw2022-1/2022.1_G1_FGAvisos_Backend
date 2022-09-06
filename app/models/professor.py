from sqlalchemy import Column, BigInteger, Boolean

from app.models.usuario import UsuarioModel


class ProfessorModel(UsuarioModel):
    __tablename__ = 'professor'

    matricula = Column(BigInteger, nullable=False, unique=True)
    is_coordenador = Column(Boolean, default=False)