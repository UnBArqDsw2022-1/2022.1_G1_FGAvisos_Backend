from app.models.professor import ProfessorModel
from app.schemas.professor import ProfessorSchema
from app.core.security import gerar_senha_hash
from app.core.exceptions import Exceptions

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


exceptions = Exceptions()

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
        try:
            new_professor: ProfessorModel = ProfessorModel(
                nome=professor.nome,
                email=professor.email,
                senha=gerar_senha_hash(professor.senha),
                numero_telefone=professor.numero_telefone,
                dt_nascimento=professor.dt_nascimento,
                created_at=professor.created_at,
                matricula=professor.matricula,
                is_coordenador=professor.is_coordenador
            )
            db.add(new_professor)
            await db.commit()
        except Exception as erro:
            raise exceptions.default_exception(erro)
        return new_professor
        

    async def delete(self, id: int, db: AsyncSession):
        professor = await self.professor_existe(id=id, db=db)

        if not professor:
            raise exceptions.nao_encontrado("Professor")

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
                raise exceptions.nao_encontrado("Professor")
            
            body = body.dict()
            for key in body:
                if body[key] != None:
                    setattr(professor, key, body[key])

            await session.commit()
            return professor
    
    async def show(self, id: int, db: AsyncSession):
        professor = await self.professor_existe(id=id, db=db)

        if not professor:
            raise exceptions.nao_encontrado("Professor")
        return professor

    async def list(self, db: AsyncSession):
        async with db as session:
            query_professores = select(ProfessorModel).order_by(ProfessorModel.id)
            result = await session.execute(query_professores)
            professores = result.scalars().all()

            if not professores:
                raise exceptions.nao_encontrados("professor")
            return professores