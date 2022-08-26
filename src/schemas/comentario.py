from typing import Any, Optional

from pydantic import BaseModel


class ComentarioSchema(BaseModel):
    id: Optional[int]
    id_aviso: int
    autor_aluno: Optional[int]
    autor_professor: Optional[int]

    class Config:
        orm_mode=True