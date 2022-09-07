from fastapi import Depends, HTTPException, status

from pydantic import ValidationError

from jose import jwt

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.core.config import settings
from app.core.database import get_session
from app.core.security import oauth2_schema
from app.models.professor import ProfessorModel
from app.models.aluno import AlunoModel
from app.core.exceptions import Exceptions


exception = Exceptions()

async def obter_usuario_atual(
    usuarioModel,
    db: AsyncSession,
    token: str
):
    try:
        payload = jwt.decode(
            token, key=settings.JWT_SECRET, algorithms=[settings.ALGORITHM]
        )
        id_usuario: str = payload.get("sub")
    except (jwt.JWTError, ValidationError):
        raise exception.credenciais_invalida()

    async with db as session:
        query = await session.execute(
            select(usuarioModel).filter(usuarioModel.id == int(id_usuario))
        )
        usuario = query.scalar()

        if not usuario:
            raise exception.nao_encontrado("Professor")
        return usuario

async def obter_professor_logado(
    db: AsyncSession = Depends(get_session),
    token: str = Depends(oauth2_schema)
):
    return await obter_usuario_atual(ProfessorModel, db, token)


async def obter_aluno_logado(
    db: AsyncSession = Depends(get_session),
    token: str = Depends(oauth2_schema)
):
    return await obter_usuario_atual(AlunoModel, db, token)
