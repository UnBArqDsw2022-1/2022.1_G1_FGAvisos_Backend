from typing import Any, Optional

from pydantic import BaseModel


class AlunoPossuiTurmaSchema(BaseModel):
    id: Optional[int]
    id_aluno: int
    id_turma: int

    class Config:
        orm_mode=True