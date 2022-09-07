"""alteracao aluno_turma

Revision ID: f9704b41ca1b
Revises: 0135a2dcf927
Create Date: 2022-09-07 16:48:22.122413

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9704b41ca1b'
down_revision = '0135a2dcf927'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('aluno_turma_id_aluno_key', 'aluno_turma', type_='unique')
    op.drop_constraint('aluno_turma_id_turma_key', 'aluno_turma', type_='unique')
    op.create_unique_constraint(None, 'aluno_turma', ['id_aluno', 'id_turma'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'aluno_turma', type_='unique')
    op.create_unique_constraint('aluno_turma_id_turma_key', 'aluno_turma', ['id_turma'])
    op.create_unique_constraint('aluno_turma_id_aluno_key', 'aluno_turma', ['id_aluno'])
    # ### end Alembic commands ###
