from fastapi import Depends, HTTPException, status

from pydantic import ValidationError

from jose import jwt

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.core.config import settings
from app.core.database import get_session
from app.core.security import oauth2_schema
from app.models.professor import ProfessorModel


async def obter_professor_atual(
    db: AsyncSession = Depends(get_session),
    token: str = Depends(oauth2_schema)
):
    try:
        payload = jwt.decode(
            token, key=settings.JWT_SECRET, algorithms=[settings.ALGORITHM]
        )
        id_professor: str = payload.get("sub")
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Não foi possível validar as credenciais."
        )
    
    async with db as session:
        query = await session.execute(
            select(ProfessorModel).filter(ProfessorModel.id == int(id_professor))
        )
        professor = query.scalar()

        if not professor:
            raise HTTPException(status_code=404, detail="Professor não encontrado.")
        return professor
