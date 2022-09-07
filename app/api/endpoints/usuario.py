from fastapi import APIRouter, status, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_session
from app.repositories.usuario import UsuarioRepository
from app.schemas.usuario import UsuarioSchemaCreate


router = APIRouter()

@router.post('/register', status_code=status.HTTP_201_CREATED)
async def registration(
        user: UsuarioSchemaCreate,
        db: AsyncSession = Depends(get_session)
):
    repository = UsuarioRepository()
    return await repository.criar(user, db)
