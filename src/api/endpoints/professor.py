from fastapi import APIRouter, status, Depends

from typing import List

from src.schemas.professor import ProfessorSchema
from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.professor import ProfessorRepository

from db.database import get_session


router = APIRouter()

professor_repository = ProfessorRepository()


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ProfessorSchema)
async def create_professor(
                            professor: ProfessorSchema, 
                            db: AsyncSession=Depends(get_session)):
    professor = await professor_repository.create(professor=professor, db=db)
    return professor


@router.delete('/{professor_id}', status_code=status.HTTP_202_ACCEPTED)
async def delete_professor(professor_id: int, db: AsyncSession=Depends(get_session)):
    result = await professor_repository.delete(id=professor_id, db=db)
    return result