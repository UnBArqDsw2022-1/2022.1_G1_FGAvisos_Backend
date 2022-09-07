from typing import Any, Optional

from pydantic import BaseModel

from datetime import datetime


class TurmaSchemaCreate(BaseModel):
    id: Optional[int]
    ano: int
    semestre: int
    nome_disciplina: str
    created_at: Optional[datetime]

    class Config:
        orm_mode=True


class TurmaSchema(TurmaSchemaCreate):
    professor: int


class TurmaSchemaUp(TurmaSchema):
    ano: Optional[int]
    semestre: Optional[int]
    nome_disciplina: Optional[str]
    professor: Optional[int]