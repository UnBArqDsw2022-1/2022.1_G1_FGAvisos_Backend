from typing import Any, Optional

from pydantic import BaseModel

from datetime import datetime


class AlunoSchema(BaseModel):
    id: Optional[int]
    nome: str
    email: str
    numero_telefone: Optional[str]
    dt_nascimento: Optional[datetime]
    created_at: Optional[datetime]
    matricula: int

    class Config:
        orm_mode=True


class AlunoSchemaCreate(AlunoSchema):
    senha: str


class AlunoSchemaUp(AlunoSchema):
    nome: Optional[str]
    email: Optional[str]
    senha: Optional[str]
    numero_telefone: Optional[str]
    dt_nascimento: Optional[datetime]
    created_at: Optional[datetime]
    matricula: Optional[int]