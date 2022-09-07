from app.models.professor import ProfessorModel
from app.models.aluno import AlunoModel
from app.schemas.usuario import UsuarioSchemaCreate
from app.core.security import gerar_senha_hash

from sqlalchemy.ext.asyncio import AsyncSession


class UsuarioRepository:
    def verifica_tipo(self, usuario: UsuarioSchemaCreate):
        if usuario.tipo_usuario == "PROFESSOR":
            novo_professor: ProfessorModel = ProfessorModel(
                nome=usuario.nome,
                email=usuario.email,
                senha=gerar_senha_hash(usuario.senha),
                numero_telefone=usuario.numero_telefone,
                dt_nascimento=usuario.dt_nascimento,
                created_at=usuario.created_at,
                matricula=usuario.matricula
            )
            return novo_professor

        if usuario.tipo_usuario == "ALUNO":
            novo_aluno: AlunoModel = AlunoModel(
                nome=usuario.nome,
                email=usuario.email,
                senha=gerar_senha_hash(usuario.senha),
                numero_telefone=usuario.numero_telefone,
                dt_nascimento=usuario.dt_nascimento,
                created_at=usuario.created_at,
                matricula=usuario.matricula
            )
            return novo_aluno
        return None


    async def criar(self, usuario: UsuarioSchemaCreate, db: AsyncSession):
        novo_usuario = self.verifica_tipo(usuario)

        if not novo_usuario:
            return dict(mensage="Tipo de usuario invalido")

        db.add(novo_usuario)
        await db.commit()
        return novo_usuario
