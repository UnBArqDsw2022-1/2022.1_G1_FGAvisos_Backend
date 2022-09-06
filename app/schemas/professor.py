from typing import Any, Optional

from pydantic import BaseModel

from datetime import datetime


class ProfessorSchema(BaseModel):
    id: Optional[int]
    nome: str
    email: str
    senha: str
    numero_telefone: Optional[str]
    dt_nascimento: Optional[datetime]
    created_at: Optional[datetime]
    matricula: int
    is_coordenador: Optional[bool]

    class Config:
        orm_mode=True