from typing import Any, Optional

from pydantic import BaseModel

from datetime import datetime


class ProfessorSchema(BaseModel):
    id: Optional[int]
    nome: str
    email: str
    numero_telefone: Optional[str]
    dt_nascimento: Optional[datetime]
    matricula: int
    is_coordenador: Optional[bool]
    created_at: Optional[datetime]

    class Config:
        orm_mode=True


class ProfessorSchemaCreate(ProfessorSchema):
    created_at: Optional[datetime]
    senha: str


class ProfessorSchemaUp(ProfessorSchema):
    nome: Optional[str]
    email: Optional[str]
    numero_telefone: Optional[str]
    dt_nascimento: Optional[datetime]
    matricula: Optional[int]
    is_coordenador: Optional[bool]