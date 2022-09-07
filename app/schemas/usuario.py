from enum import Enum
from typing import Any, Optional

from pydantic import BaseModel

from datetime import datetime


class TipoUsuario(str, Enum):
    PROFESSOR = "PROFESSOR"
    ALUNO = "ALUNO"


class UsuarioSchemaCreate(BaseModel):
    id: Optional[int]
    nome: str
    email: str
    senha: str
    matricula: int
    numero_telefone: Optional[str]
    dt_nascimento: Optional[datetime]
    tipo_usuario: TipoUsuario
    created_at: Optional[datetime]

    class Config:
        orm_mode=True