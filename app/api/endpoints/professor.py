from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from typing import List

from app.schemas.professor import ProfessorSchema
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.professor import ProfessorRepository
from app.core.database import get_session
from app.core.security import autenticacao_professor, criar_acesso_token


router = APIRouter()

professor_repository = ProfessorRepository()


@router.post('/signup', status_code=status.HTTP_201_CREATED, response_model=ProfessorSchema)
async def post_usuario_jwt(
    user: ProfessorSchema, 
    db: AsyncSession = Depends(get_session)
):
    return await professor_repository.create(user, db)


@router.post('/login')
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_session)
):
    professor = await autenticacao_professor(
        email=form_data.username,
        senha=form_data.password,
        db=db
    )

    if not professor:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail='Dados de acesso incorretos.'
        )

    return {
        "access_token": await criar_acesso_token(subject=professor.id),
        "token_type": "bearer",
    }


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