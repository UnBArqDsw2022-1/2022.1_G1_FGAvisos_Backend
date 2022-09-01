from fastapi import APIRouter, status, Depends

from typing import List

from src.schemas.turma import TurmaSchema
from src.repositories.turma import TurmaModel
from src.repositories.turma import TurmaRepository

from sqlalchemy.ext.asyncio import AsyncSession

from db.database import get_session


router = APIRouter()

repository_turma = TurmaRepository()

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=TurmaSchema)
async def post_turma(turma: TurmaSchema, db: AsyncSession=Depends(get_session)):
    return await repository_turma.create(turma, db)
