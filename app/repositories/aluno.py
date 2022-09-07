from app.models.aluno import AlunoModel
from app.schemas.aluno import AlunoSchema
from app.core.security import gerar_senha_hash

from fastapi import HTTPException, status

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


class AlunoRepository:

    async def aluno_existe(self, id: int, db: AsyncSession):
        async with db as session:
            query_aluno = select(AlunoModel).filter(
                AlunoModel.id == id)
            result = await session.execute(query_aluno)
            aluno = result.scalar()

            if not aluno:
                return None
            return aluno

    async def create(self, aluno: AlunoSchema, db: AsyncSession):
        try:
            novo_aluno: AlunoModel = AlunoModel(**aluno.dict())
            novo_aluno.senha = gerar_senha_hash(aluno.senha)
            db.add(novo_aluno)
            await db.commit()
        except Exception as erro:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Exeção -> {erro}")
        return novo_aluno

    async def delete(self, id: int, db: AsyncSession):
        aluno = await self.aluno_existe(id=id, db=db)

        if not aluno:
            raise HTTPException(detail='Usuario não encontrado',
                                status_code=status.HTTP_404_NOT_FOUND)

        async with db as session:
            await session.delete(aluno)
            await session.commit()

            return dict(message="Usuario deletado com sucesso")

    async def update(self, id: int, body: AlunoSchema, db: AsyncSession):
        async with db as session:
            query_aluno = select(AlunoModel).filter(
                AlunoModel.id == id)
            result = await session.execute(query_aluno)
            aluno: AlunoModel = result.scalar()

            if not aluno:
                raise HTTPException(detail='Usuario não encontrado',
                                    status_code=status.HTTP_404_NOT_FOUND)

            body = body.dict()
            for key in body:
                if body[key] != None:
                    setattr(aluno, key, body[key])
                    if body[key] == "senha":
                        setattr(aluno, key, gerar_senha_hash(body[key]))
            await session.commit()
            return aluno

    async def show(self, id: int, db: AsyncSession):
        aluno = await self.aluno_existe(id=id, db=db)

        if not aluno:
            raise HTTPException(detail='Usuario não encontrado',
                                status_code=status.HTTP_404_NOT_FOUND)
        return aluno

    async def list(self, db: AsyncSession):
        async with db as session:
            query_alunos = select(AlunoModel).order_by(
                AlunoModel.id)
            result = await session.execute(query_alunos)
            alunos = result.scalars().all()

            if not alunos:
                raise HTTPException(detail='Nenhum aluno foi encontrado',
                                    status_code=status.HTTP_404_NOT_FOUND)
            return alunos