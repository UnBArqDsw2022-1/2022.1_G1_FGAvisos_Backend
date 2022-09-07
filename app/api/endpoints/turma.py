from fastapi import APIRouter, status, Depends, HTTPException

from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.professor import ProfessorModel
from app.schemas.turma import TurmaSchema, TurmaSchemaCreate, TurmaSchemaUp
from app.repositories.turma import TurmaRepository
from app.core.database import get_session
from app.core.deps import obter_professor_atual


router = APIRouter()

repository_turma = TurmaRepository()

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=TurmaSchema)
async def post_turma(
            turma: TurmaSchemaCreate, 
            criador: ProfessorModel = Depends(obter_professor_atual),
            db: AsyncSession=Depends(get_session)):
    return await repository_turma.create(criador.id, turma, db)


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[TurmaSchema])
async def get_turmas(db: AsyncSession=Depends(get_session)):
    return await repository_turma.list(db)


@router.get('/professor/{id_professor}', status_code=status.HTTP_200_OK, response_model=List[TurmaSchema])
async def get_turmas_professor(
            id_professor: int, 
            db: AsyncSession=Depends(get_session)):
    return await repository_turma.show_turmas_professor(id_professor, db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=TurmaSchema)
async def get_turma(id: int, db: AsyncSession=Depends(get_session)):
    turma = await repository_turma.turma_existe(id, db)
    if not turma:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Turma não encontrada")
    return turma


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=TurmaSchema)
async def alterar_turma(
    id: int, 
    turma_alterada: TurmaSchemaUp,
    professor_atual: ProfessorModel = Depends(obter_professor_atual),
    db: AsyncSession=Depends(get_session)
):
    return await repository_turma.update(
        id, 
        turma_alterada, 
        professor_atual.id, 
        db
    )


@router.delete('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def apagar_turma(
    id: int,
    professor_atual: ProfessorModel = Depends(obter_professor_atual),
    db: AsyncSession=Depends(get_session)
):
    return await repository_turma.delete(id, professor_atual.id, db)
