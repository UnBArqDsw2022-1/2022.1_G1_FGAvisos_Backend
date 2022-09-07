from typing import Optional
from passlib.context import CryptContext

from fastapi.security import OAuth2PasswordBearer

from jose import jwt

from datetime import datetime, timedelta

from pytz import timezone

from app.core.config import settings
from app.models.aluno import AlunoModel
from app.models.professor import ProfessorModel

from pydantic import EmailStr

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession


oauth2_schema = OAuth2PasswordBearer(
    tokenUrl="/login"
)


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verifica_senha(senha: str, hash_senha: str) -> bool:
    return pwd_context.verify(senha, hash_senha)


def gerar_senha_hash(senha: str) -> str:
    return pwd_context.hash(senha)


def criar_acesso_token(subject: str) -> str:
    timezone_sp = timezone('America/Sao_Paulo')
    expira = datetime.now(tz=timezone_sp) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    payload = {
        "exp": expira, 
        "iat": datetime.now(tz=timezone_sp), 
        "sub": str(subject)
    }
    encoded_jwt = jwt.encode(
        payload, 
        settings.JWT_SECRET, 
        algorithm=settings.ALGORITHM
    )
    return encoded_jwt


async def autenticacao_usuario(
    email: EmailStr, 
    senha: str,
    usuarioModel,
    db: AsyncSession
) -> Optional[ProfessorModel | AlunoModel]:
    async with db as session:
        query = select(usuarioModel).filter(usuarioModel.email == email)
        result = await session.execute(query)
        usuario: ProfessorModel | AlunoModel = result.scalar()

        if not usuario:
            return None
        if not verifica_senha(senha, usuario.senha):
            return None
        return usuario