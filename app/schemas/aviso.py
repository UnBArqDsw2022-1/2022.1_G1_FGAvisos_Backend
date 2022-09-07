from typing import Any, Optional

from pydantic import BaseModel

from datetime import datetime


class AvissoSchemaCreate(BaseModel):
    id: Optional[int]
    titulo: str
    corpo: str
    tag: Optional[str]
    aviso_geral: Optional[bool]
    created_at: Optional[datetime]
    turma: int

    class Config:
        orm_mode=True


class AvisoSchema(AvissoSchemaCreate):
    autor: int


class AvisoSchemaUp(AvisoSchema):
    titulo: Optional[str]
    corpo: Optional[str]
    tag: Optional[str]
    aviso_geral: Optional[bool]
    turma: Optional[int]
    autor: Optional[int]
