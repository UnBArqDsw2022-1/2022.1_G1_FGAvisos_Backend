from app.models.aviso import AvisoModel
from app.schemas.aviso import AvisoSchema
from app.core.exceptions import Exceptions

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from typing import List


exceptions = Exceptions()

class AvisoRepository:
    async def aviso_existe(self, id: str, db: AsyncSession):
        async with db as session:
            query_aviso = await session.execute(
                select(AvisoModel).filter(AvisoModel.id == id)
            )
            aviso: AvisoModel = query_aviso.scalar()

            if not aviso:
                return None
            return aviso

    async def inserir(self, aviso: AvisoSchema, id_autor: int, db: AsyncSession):
        novo_aviso: AvisoModel = AvisoModel(**aviso.dict())
        novo_aviso.autor = id_autor
        try:
            db.add(novo_aviso)
            await db.commit()
        except Exception as Error:
            raise exceptions.bad_request(Error)
        return novo_aviso

    async def deletar(self, id: int, id_prof_atual: int, db: AsyncSession):
        aviso_a_deletar = await self.aviso_existe(id, db)

        if not aviso_a_deletar:
            raise exceptions.nao_encontrado("Aviso")
        if aviso_a_deletar.autor != id_prof_atual:
            raise exceptions.nao_autorizado("deletar este aviso.")

        await db.delete(aviso_a_deletar)
        await db.commit()

        return dict(message="Aviso deletado com sucesso")

    async def alterar(
            self,
            id: int,
            body: AvisoSchema,
            id_prof_atual: int,
            db: AsyncSession
    ):
        async with db as session:
            query = await session.execute(
                select(AvisoModel).filter(AvisoModel.id == id)
            )
            aviso_selecionado: AvisoModel = query.scalar()

            if not aviso_selecionado:
                raise exceptions.nao_encontrado("Aviso")
            if aviso_selecionado.autor != id_prof_atual:
                raise exceptions.nao_autorizado("alterar este aviso.")

            body = body.dict()
            for key in body:
                if body[key] is not None:
                    setattr(aviso_selecionado, key, body[key])
            await session.commit()
            return  aviso_selecionado

    async def obter_todos(self, db: AsyncSession):
        async with db as session:
            query_avisos = await session.execute(
                select(AvisoModel)
            )
            avisos: List[AvisoModel] = query_avisos.scalars().all()

            if not avisos:
                raise exceptions.nao_encontrados("aviso")
            return avisos

    async def obter_todos_por_turma(self, id_turma, db: AsyncSession):
        async with db as session:
            query_avisos = await session.execute(
                select(AvisoModel).filter(AvisoModel.turma == id_turma)
            )
            avisos: List[AvisoModel] = query_avisos.scalars().all()

            if not avisos:
                raise exceptions.nao_encontrados("aviso")
            return avisos

    async def obter_por_professor(self, id_professor: int, db: AsyncSession):
        async with db as session:
            query_avisos = await session.execute(
                select(AvisoModel).filter(AvisoModel.autor == id_professor)
            )
            avisos: List[AvisoModel] = query_avisos.scalars().all()

            if not avisos:
                raise exceptions.nao_encontrados("aviso vinculado a este professor")
            return avisos

    async def obter_por_professor_e_turma(
        self, id_prof: int, id_turma: int, db: AsyncSession
    ):
        async with db as session:
            query = select(AvisoModel).filter(AvisoModel.autor == id_prof).\
                filter(AvisoModel.turma == id_turma)
            resultado = await session.execute(query)
            avisos: List[AvisoModel] = resultado.scalars().all()

            if not avisos:
                raise exceptions.nao_encontrados("aviso")
            return avisos