from typing import Any, Optional

from pydantic import BaseModel

from datetime import datetime


class TurmaSchema(BaseModel):
    id: Optional[int]
    professor: int
    ano: int
    semestre: int
    nome_disciplina: str
    created_at: Optional[datetime]

    class Config:
        orm_mode=True