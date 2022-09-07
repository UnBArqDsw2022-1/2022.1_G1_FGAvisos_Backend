from app.core.deps import obter_professor_atual
from app.core.database import get_session
from app.schemas.aviso import AvisoSchema, AvissoSchemaCreate, AvisoSchemaUp
from app.repositories.aviso import AvisoRepository
from app.models.professor import ProfessorModel

from fastapi import APIRouter, Depends, HTTPException, status

from typing import List, Optional

from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter()

repository_aviso = AvisoRepository()


@router.post("/", status_code=201, response_model=AvisoSchema)
async def criar_aviso(
    aviso: AvissoSchemaCreate,
    professor: ProfessorModel = Depends(obter_professor_atual),
    db: AsyncSession = Depends(get_session)
):
    return await repository_aviso.inserir(aviso, professor.id, db)


@router.get("/{id_aviso}", status_code=200, response_model=AvisoSchema)
async def obter_aviso(id_aviso: int, db: AsyncSession = Depends(get_session)):
    aviso = await repository_aviso.aviso_existe(id_aviso, db)
    if not aviso:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Aviso não encontrado."
        )
    return aviso


@router.get("/", status_code=200, response_model=List[AvisoSchema])
async def obter_todos_avisos(
    id_turma: Optional[int] = None,
    id_prof: Optional[int] = None,
    db: AsyncSession = Depends(get_session)
):
    if id_turma and id_prof:
        return await repository_aviso.obter_por_professor_e_turma(
            id_prof, id_turma, db
        )
    if id_turma:
        return await repository_aviso.obter_todos_por_turma(id_turma, db)
    if id_prof:
        return await repository_aviso.obter_por_professor(id_prof, db)
    return await repository_aviso.obter_todos(db)


@router.get("/{id_prof}", status_code=200, response_model=List[AvisoSchema])
async def obter_todos_avisos_por_professor(
    id_prof: int,
    db: AsyncSession = Depends(get_session)
):
    return await repository_aviso.obter_por_professor(id_prof, db)


@router.delete("/{id_aviso}", status_code=status.HTTP_202_ACCEPTED)
async def deletar_aviso(
    id_aviso: int,
    professor: ProfessorModel = Depends(obter_professor_atual),
    db: AsyncSession = Depends(get_session)
):
    return await repository_aviso.deletar(id_aviso, professor.id, db)


@router.put("/{id_aviso}", status_code=202, response_model=AvisoSchema)
async def alterar_aviso(
    id_aviso: int,
    aviso_alterado: AvisoSchemaUp,
    professor: ProfessorModel = Depends(obter_professor_atual),
    db: AsyncSession = Depends(get_session)
):
    return await repository_aviso.alterar(
        id_aviso, aviso_alterado, professor.id, db
    )