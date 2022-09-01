from typing import List
from unittest import result

from src.models.professor import ProfessorModel

from fastapi import HTTPException, status

from src.schemas.professor import ProfessorSchema

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


class ProfessorRepository:

    async def professor_existe(self, id: int, db: AsyncSession):
        async with db as session:
            query_professor = select(ProfessorModel).filter(ProfessorModel.id == id)
            result = await session.execute(query_professor)
            professor = result.scalar()

            if not professor:
                return None
            return professor

    async def create(self, professor: ProfessorSchema, db: AsyncSession):
        novo_professor: ProfessorModel = ProfessorModel(**professor.dict())
        
        try:
            db.add(novo_professor)
            await db.commit()
        except Exception as error:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=error)

        return novo_professor

    async def delete(self, id: int, db: AsyncSession):
        professor = await self.professor_existe(id=id, db=db)

        if not professor:
            raise HTTPException(detail='Usuario não encontrado', 
                                status_code=status.HTTP_404_NOT_FOUND) 

        async with db as session:
            await session.delete(professor)
            await session.commit()

            return dict(message = "Usuario deletado com sucesso")

    async def update(self, id: int, body: ProfessorSchema, db: AsyncSession):        
        async with db as session:
            query_professor = select(ProfessorModel).filter(ProfessorModel.id == id)
            result = await session.execute(query_professor)
            professor: ProfessorModel = result.scalar()

            if not professor:
                raise HTTPException(detail='Usuario não encontrado', 
                                    status_code=status.HTTP_404_NOT_FOUND) 
            
            body = body.dict()
            for key in body:
                if body[key] != None:
                    setattr(professor, key, body[key])

            await session.commit()
            return professor