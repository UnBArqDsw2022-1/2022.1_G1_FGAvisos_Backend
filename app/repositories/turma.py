from typing import List
from app.models.turma import TurmaModel
from app.schemas.turma import TurmaSchema
from app.core.exceptions import Exceptions

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


exceptions = Exceptions()


class TurmaRepository:

    async def turma_existe(self, id: int, db: AsyncSession):
        async with db as session:
            query_turma = select(TurmaModel).filter(TurmaModel.id == id)
            result = await session.execute(query_turma)
            turma: TurmaModel = result.scalar()

        if not turma:
            return None
        return turma

    async def create(self, id_professor: int, turma: TurmaSchema, db: AsyncSession):
        nova_turma: TurmaModel = TurmaModel(**turma.dict())
        nova_turma.professor_id = id_professor

        try:
            db.add(nova_turma)
            await db.commit()
        except Exception as error:
            raise exceptions.default_exception(error)
        return nova_turma

    async def list(self, db: AsyncSession):
        async with db as session:
            query_turmas = select(TurmaModel)
            result = await session.execute(query_turmas)
            turmas: List[TurmaModel] = result.scalars().all()

            if not turmas:
                raise exceptions.nao_encontrados("turma")
            return turmas

    async def show_turmas_professor(self, id_professor: int, db: AsyncSession):
        async with db as session:
            query = select(TurmaModel).filter(TurmaModel.professor_id == id_professor)
            result = await session.execute(query)
            turmas_professor: List[TurmaModel] = result.scalars().all()

            if not turmas_professor:
                raise exceptions.nao_encontrados("turma com este professor")
            return turmas_professor

    async def update(self, id: int, body: TurmaSchema, id_professor_atual: int, db: AsyncSession):
        async with db as session:
            query = select(TurmaModel).filter(TurmaModel.id == id)
            result = await session.execute(query)
            turma: TurmaModel = result.scalar()

            if not turma:
                raise exceptions.nao_encontrados("turma")
            if turma.professor_id != id_professor_atual:
                raise exceptions.sem_altorizacao("alterar essa turma!")

            body = body.dict()
            for key in body:
                if body[key] != None:
                    setattr(turma, key, body[key])
            
            await session.commit()
            return turma
    
    async def delete(self, id: int, id_professor_atual: int, db: AsyncSession):
        turma_a_deletar = await self.turma_existe(id, db)

        if not turma_a_deletar:
            raise exceptions.nao_encontrado("Turma")
        if turma_a_deletar.professor_id != id_professor_atual:
            raise exceptions.sem_altorizacao("apagar essa turma!")
        
        await db.delete(turma_a_deletar)
        await db.commit()
        return dict(message="Turma deletada com sucesso.")