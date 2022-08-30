"""init

Revision ID: 0135a2dcf927
Revises: 41fcd8ae6116
Create Date: 2022-08-24 00:02:53.223682

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0135a2dcf927'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('aluno',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=150), nullable=False),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('senha', sa.String(length=20), nullable=False),
    sa.Column('numero_telefone', sa.String(length=20), nullable=True),
    sa.Column('dt_nascimento', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('matricula', sa.BigInteger(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('matricula')
    )
    op.create_table('professor',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=150), nullable=False),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('senha', sa.String(length=20), nullable=False),
    sa.Column('numero_telefone', sa.String(length=20), nullable=True),
    sa.Column('dt_nascimento', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('matricula', sa.BigInteger(), nullable=False),
    sa.Column('is_coordenador', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('matricula')
    )
    op.create_table('turma',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('professor', sa.Integer(), nullable=True),
    sa.Column('ano', sa.Integer(), nullable=False),
    sa.Column('semestre', sa.Integer(), nullable=False),
    sa.Column('nome_disciplina', sa.String(length=75), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['professor'], ['professor.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('aluno_turma',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('id_aluno', sa.Integer(), nullable=True),
    sa.Column('id_turma', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_aluno'], ['aluno.id'], ),
    sa.ForeignKeyConstraint(['id_turma'], ['turma.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id_aluno'),
    sa.UniqueConstraint('id_turma')
    )
    op.create_table('aviso',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('titulo', sa.String(length=30), nullable=False),
    sa.Column('corpo', sa.String(length=2000), nullable=False),
    sa.Column('autor', sa.Integer(), nullable=False),
    sa.Column('tag', sa.String(length=20), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('turma', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['autor'], ['professor.id'], ),
    sa.ForeignKeyConstraint(['turma'], ['turma.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comentario',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('id_aviso', sa.Integer(), nullable=True),
    sa.Column('autor_aluno', sa.Integer(), nullable=True),
    sa.Column('autor_professor', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['autor_aluno'], ['aluno.id'], ),
    sa.ForeignKeyConstraint(['autor_professor'], ['professor.id'], ),
    sa.ForeignKeyConstraint(['id_aviso'], ['aviso.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comentario')
    op.drop_table('aviso')
    op.drop_table('aluno_turma')
    op.drop_table('turma')
    op.drop_table('professor')
    op.drop_table('aluno')
    # ### end Alembic commands ###