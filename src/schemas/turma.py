from typing import Any, Optional

from pydantic import BaseModel

from datetime import datetime


class TurmaSchema(BaseModel):
    id: Optional[int]
    professor: str
    ano: str
    semestre: int
    nome_disciplina: Optional[str]
    created_at: Optional[datetime]

    class Config:
        orm_mode=True