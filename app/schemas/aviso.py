from typing import Any, Optional

from pydantic import BaseModel

from datetime import datetime


class AvisoSchema(BaseModel):
    id: Optional[int]
    titulo: str
    corpo: str
    autor: int
    tag: Optional[str]
    created_at: Optional[datetime]
    turma: int

    class Config:
        orm_mode=True