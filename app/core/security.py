from passlib.context import CryptContext

from fastapi.security import OAuth2PasswordBearer

from jose import jwt

from datetime import datetime, timedelta

from pytz import timezone

from app.core.config import settings
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


async def criar_acesso_token(subject: str) -> str:
    timezone_sp = timezone('America/Sao_Paulo')
    expira = datetime.now(tz=timezone_sp) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    payload = {
        "exp": expira, 
        "iat": datetime.now(tz=timezone_sp), 
        "sub": subject
    }
    encoded_jwt = jwt.encode(
        payload, 
        settings.JWT_SECRET, 
        algorithm=settings.ALGORITHM
    )

    return encoded_jwt


async def autenticacao_professor(
    email: EmailStr, 
    senha: str, 
    db: AsyncSession
):
    async with db as session:
        query = select(ProfessorModel).filter(ProfessorModel.email == email)
        result = await session.execute(query)
        professor: ProfessorModel = result.scalar()

        if not professor:
            return None
        if not verifica_senha(senha, professor.senha):
            return None
        return professor