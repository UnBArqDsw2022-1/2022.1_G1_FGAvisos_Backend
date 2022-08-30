from typing import List

from src.models.professor import ProfessorModel

from fastapi import HTTPException, status

from src.schemas.professor import ProfessorSchema

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


class ProfessorRepository:

    async def create(self, professor: ProfessorSchema, db: AsyncSession):
        novo_professor: ProfessorModel = ProfessorModel(**professor.dict())
        
        try:
            db.add(novo_professor)
            await db.commit()
        except Exception as error:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=error)

        return novo_professor