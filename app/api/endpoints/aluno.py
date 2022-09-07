from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.aluno import AlunoModel
from app.schemas.aluno import AlunoSchema, AlunoSchemaCreate, AlunoSchemaUp
from app.repositories.aluno import AlunoRepository
from app.core.database import get_session
from app.core.security import autenticacao_usuario, criar_acesso_token
from app.core.deps import obter_aluno_logado


router = APIRouter()

repository_aluno = AlunoRepository()


@router.post('/login')
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_session)
):
    aluno: AlunoModel = await autenticacao_usuario(
        email=form_data.username,
        senha=form_data.password,
        usuarioModel=AlunoModel,
        db=db
    )
    if not aluno:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Dados de acesso incorretos.'
        )
    return {
        "access_token": criar_acesso_token(subject=aluno.id),
        "token_type": "bearer",
    }


@router.get('/logado', status_code=status.HTTP_200_OK, response_model=AlunoSchema)
def opter_professor_logado(
    professor_logado: AlunoModel = Depends(obter_aluno_logado)
):
    return professor_logado


@router.delete('/', status_code=status.HTTP_202_ACCEPTED)
async def delete_professor(
    professor_logado: AlunoModel = Depends(obter_aluno_logado),
    db: AsyncSession=Depends(get_session)
):
    result = await repository_aluno.delete(id=professor_logado.id, db=db)
    return result


@router.put('/', status_code=status.HTTP_202_ACCEPTED, response_model=AlunoSchema)
async def alterar_dados_conta(
    professor: AlunoSchemaUp,
    professor_logado: AlunoModel = Depends(obter_aluno_logado),
    db: AsyncSession = Depends(get_session)
):
    result = await repository_aluno.update(
        id=professor_logado.id,
        body=professor,
        db=db
    )
    return result


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=AlunoSchema)
async def get_professor(id: int, db: AsyncSession = Depends(get_session)):
    return await repository_aluno.show(id, db)


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[AlunoSchema])
async def get_professores(db: AsyncSession = Depends(get_session)):
    return await repository_aluno.list(db)