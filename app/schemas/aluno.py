from typing import Any, Optional

from pydantic import BaseModel

from datetime import datetime


class AlunoSchema(BaseModel):
    id: Optional[int]
    nome: str
    email: str
    senha: str
    numero_telefone: Optional[str]
    dt_nascimento: Optional[datetime]
    created_at: Optional[datetime]
    matricula: int

    class Config:
        orm_mode=True