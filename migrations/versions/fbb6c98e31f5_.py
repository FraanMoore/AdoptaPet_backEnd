"""empty message

Revision ID: fbb6c98e31f5
Revises: cf39ae3ac14c
Create Date: 2023-03-27 21:13:54.410213

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fbb6c98e31f5'
down_revision = 'cf39ae3ac14c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('form', schema=None) as batch_op:
        batch_op.alter_column('query5',
               existing_type=sa.BOOLEAN(),
               type_=sa.String(length=500),
               nullable=False)
        batch_op.alter_column('query6',
               existing_type=sa.BOOLEAN(),
               type_=sa.String(length=500),
               nullable=False)
        batch_op.alter_column('query14',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=500),
               existing_nullable=False)
        batch_op.alter_column('query15',
               existing_type=sa.BOOLEAN(),
               type_=sa.String(length=500),
               nullable=False)
        batch_op.alter_column('query16',
               existing_type=sa.VARCHAR(length=500),
               type_=sa.Boolean(),
               nullable=True)
        batch_op.alter_column('query17',
               existing_type=sa.BOOLEAN(),
               type_=sa.String(length=500),
               nullable=False)
        batch_op.alter_column('query18',
               existing_type=sa.VARCHAR(length=500),
               type_=sa.Boolean(),
               nullable=True)
        batch_op.alter_column('query19',
               existing_type=sa.BOOLEAN(),
               type_=sa.String(length=500),
               nullable=False)
        batch_op.alter_column('query20',
               existing_type=sa.VARCHAR(length=500),
               type_=sa.Boolean(),
               nullable=True)
        batch_op.alter_column('query23',
               existing_type=sa.BOOLEAN(),
               type_=sa.String(length=500),
               nullable=False)
        batch_op.alter_column('query28',
               existing_type=sa.BOOLEAN(),
               type_=sa.String(length=500),
               nullable=False)
        batch_op.alter_column('query30',
               existing_type=sa.VARCHAR(length=500),
               type_=sa.Boolean(),
               nullable=True)
        batch_op.alter_column('query38',
               existing_type=sa.VARCHAR(length=500),
               type_=sa.Boolean(),
               nullable=True)
        batch_op.alter_column('query42',
               existing_type=sa.BOOLEAN(),
               type_=sa.String(length=500),
               nullable=False)
        batch_op.alter_column('query44',
               existing_type=sa.VARCHAR(length=500),
               type_=sa.Boolean(),
               nullable=True)

    with op.batch_alter_table('pet', schema=None) as batch_op:
        batch_op.alter_column('age',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=50),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pet', schema=None) as batch_op:
        batch_op.alter_column('age',
               existing_type=sa.String(length=50),
               type_=sa.INTEGER(),
               existing_nullable=False)

    with op.batch_alter_table('form', schema=None) as batch_op:
        batch_op.alter_column('query44',
               existing_type=sa.Boolean(),
               type_=sa.VARCHAR(length=500),
               nullable=False)
        batch_op.alter_column('query42',
               existing_type=sa.String(length=500),
               type_=sa.BOOLEAN(),
               nullable=True)
        batch_op.alter_column('query38',
               existing_type=sa.Boolean(),
               type_=sa.VARCHAR(length=500),
               nullable=False)
        batch_op.alter_column('query30',
               existing_type=sa.Boolean(),
               type_=sa.VARCHAR(length=500),
               nullable=False)
        batch_op.alter_column('query28',
               existing_type=sa.String(length=500),
               type_=sa.BOOLEAN(),
               nullable=True)
        batch_op.alter_column('query23',
               existing_type=sa.String(length=500),
               type_=sa.BOOLEAN(),
               nullable=True)
        batch_op.alter_column('query20',
               existing_type=sa.Boolean(),
               type_=sa.VARCHAR(length=500),
               nullable=False)
        batch_op.alter_column('query19',
               existing_type=sa.String(length=500),
               type_=sa.BOOLEAN(),
               nullable=True)
        batch_op.alter_column('query18',
               existing_type=sa.Boolean(),
               type_=sa.VARCHAR(length=500),
               nullable=False)
        batch_op.alter_column('query17',
               existing_type=sa.String(length=500),
               type_=sa.BOOLEAN(),
               nullable=True)
        batch_op.alter_column('query16',
               existing_type=sa.Boolean(),
               type_=sa.VARCHAR(length=500),
               nullable=False)
        batch_op.alter_column('query15',
               existing_type=sa.String(length=500),
               type_=sa.BOOLEAN(),
               nullable=True)
        batch_op.alter_column('query14',
               existing_type=sa.String(length=500),
               type_=sa.INTEGER(),
               existing_nullable=False)
        batch_op.alter_column('query6',
               existing_type=sa.String(length=500),
               type_=sa.BOOLEAN(),
               nullable=True)
        batch_op.alter_column('query5',
               existing_type=sa.String(length=500),
               type_=sa.BOOLEAN(),
               nullable=True)

    # ### end Alembic commands ###
