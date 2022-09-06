from unittest import result
from fastapi import APIRouter, status, Depends

from typing import List

from app.schemas.professor import ProfessorSchema
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.professor import ProfessorRepository

from core.database import get_session


router = APIRouter()

professor_repository = ProfessorRepository()


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ProfessorSchema)
async def create_professor(professor: ProfessorSchema, 
                            db: AsyncSession=Depends(get_session)):
    professor = await professor_repository.create(professor=professor, db=db)
    return professor


@router.delete('/{professor_id}', status_code=status.HTTP_202_ACCEPTED)
async def delete_professor(professor_id: int, db: AsyncSession=Depends(get_session)):
    result = await professor_repository.delete(id=professor_id, db=db)
    return result


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=ProfessorSchema)
async def put_professor(id: int, professor_atualizado: ProfessorSchema, 
                        db: AsyncSession = Depends(get_session)):
    result = await professor_repository.update(id=id, body=professor_atualizado, db=db)
    return result

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=ProfessorSchema)
async def get_professor(id: int, db: AsyncSession = Depends(get_session)):
    return await professor_repository.show(id, db)

@router.get('/', status_code=status.HTTP_200_OK, response_model=List[ProfessorSchema])
async def get_professores(db: AsyncSession = Depends(get_session)):
    return await professor_repository.list(db)