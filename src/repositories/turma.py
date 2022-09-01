from typing import List
from unittest import result
from src.models.turma import TurmaModel
from src.schemas.turma import TurmaSchema

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from fastapi import status, HTTPException


class TurmaRepository:

    async def turma_existe(self, id: int, db: AsyncSession):
        async with db as session:
            query_turma = select(TurmaModel).filter(TurmaModel.id == id)
            result = await session.execute(query_turma)
            turma: TurmaModel = result.scalar()

        if not turma:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Turma não encontrada")
        return turma

    async def create(self, turma: TurmaSchema, db: AsyncSession):
        nova_turma: TurmaModel = TurmaModel(**turma.dict())

        try:
            db.add(nova_turma)
            await db.commit()
        except Exception as error:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail=error)
        return nova_turma

    async def list(self, db: AsyncSession):
        async with db as session:
            query_turmas = select(TurmaModel)
            result = await session.execute(query_turmas)
            turmas: List[TurmaModel] = result.scalars().all()

            if not turmas:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                    detail="Nenhuma turma foi encontrada.")
            return turmas

    async def show_turmas_professor(self, id_professor: int, db: AsyncSession):
        async with db as session:
            query = select(TurmaModel).filter(TurmaModel.professor == id_professor)
            result = await session.execute(query)
            turmas_professor: List[TurmaModel] = result.scalars().all()

            if not turmas_professor:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                    detail="Não foram encontradas turmas para este professor.")
            return turmas_professor

    async def update(self, id: int, body: TurmaSchema, db: AsyncSession):
        async with db as session:
            query = select(TurmaModel).filter(TurmaModel.id == id)
            result = await session.execute(query)
            turma: TurmaModel = result.scalar()

            if not turma:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                    detail="Nenhuma turma foi encontrada.")

            body = body.dict()
            for key in body:
                if body[key] != None:
                    setattr(turma, key, body[key])
            
            await session.commit()
            return turma
            