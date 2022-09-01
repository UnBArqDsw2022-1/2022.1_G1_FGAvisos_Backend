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