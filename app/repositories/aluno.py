from app.models.aluno import AlunoModel
from app.schemas.aluno import AlunoSchema
from app.core.security import gerar_senha_hash
from app.models.aluno_turma import AlunoTurmaModel
from app.schemas.aluno_turma import AlunoTurmaSchema
from app.schemas.aviso import AvisoSchema
from app.models.aviso import AvisoModel
from app.models.turma import TurmaModel

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

    async def turma_existe(self, id: int, db: AsyncSession):
        async with db as session:
            query_turma = session.execute(
                select(TurmaModel).filter(TurmaModel.id == id)
            )
            turma: TurmaModel = query_turma.scalar()

            if not turma:
                return None
            return turma

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

    async def registrar_em_turma(
        self,
        id_aluno: int,
        id_turma:int,
        db: AsyncSession
    ):
        turma: TurmaModel = self.turma_existe(id_turma, db)
        if not turma:
            raise HTTPException(
                detail='Nenhum aluno foi encontrado',
                status_code=status.HTTP_404_NOT_FOUND
            )

        aluno_turma: AlunoTurmaModel = AlunoTurmaModel(
            id_aluno=id_aluno, id_turma=id_turma
        )
        db.add(aluno_turma)
        await db.commit()

        return dict(mensage="Aluno cadastrado na turma com sucesso.")


    async def obter_turmas_registradas(self, id_usuario: int, db: AsyncSession):
        async with db as session:
            select_turmas = select(TurmaModel).join(
                AlunoTurmaModel, TurmaModel.id == AlunoTurmaModel.id_turma).\
                where(AlunoTurmaModel.id_aluno == id_usuario)
            resultado_select = await session.execute(select_turmas)
            turmas = resultado_select.scalars().all()

            return turmas

    async def obter_avisos_viculados(self, id_usuario: int, db: AsyncSession):
        async with db as session:
            select_avisos = select(AvisoModel).join(
                TurmaModel, TurmaModel.id == AvisoModel.turma).\
                join(AlunoTurmaModel, AlunoTurmaModel.id_turma == TurmaModel.id).where(
                AlunoTurmaModel.id_aluno == id_usuario)
            resultado_select = await session.execute(select_avisos)
            avisos_viculados = resultado_select.scalars().all()

            return avisos_viculados
