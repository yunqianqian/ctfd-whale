"""empty message

Revision ID: 5779830cec2f
Revises: 
Create Date: 2020-08-03 05:44:54.338459

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5779830cec2f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('image',
    sa.Column('ID', sa.String(length=64), nullable=False),
    sa.Column('NAME', sa.String(length=128), nullable=False),
    sa.Column('IMAGEID', sa.String(length=128), nullable=False),
    sa.Column('CREATETIME', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('ID'),
    sa.UniqueConstraint('IMAGEID'),
    sa.UniqueConstraint('NAME')
    )
    op.create_table('challenge',
    sa.Column('ID', sa.String(length=64), nullable=False),
    sa.Column('MEMORY', sa.String(length=32), nullable=True),
    sa.Column('CPU', sa.Float(), nullable=True),
    sa.Column('IMAGEID', sa.String(length=128), nullable=False),
    sa.Column('TYPE', sa.String(length=32), nullable=True),
    sa.Column('PORT', sa.String(length=64), nullable=True),
    sa.Column('CREATETIME', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['IMAGEID'], ['image.IMAGEID'], ),
    sa.PrimaryKeyConstraint('ID')
    )
    op.create_table('container',
    sa.Column('ID', sa.String(length=64), nullable=False),
    sa.Column('IMAGEID', sa.String(length=128), nullable=False),
    sa.Column('USERID', sa.String(length=17), nullable=False),
    sa.Column('CONNAME', sa.String(length=128), nullable=False),
    sa.Column('FLAG', sa.String(length=256), nullable=True),
    sa.Column('RESETNUM', sa.Integer(), nullable=True),
    sa.Column('PORT', sa.String(length=64), nullable=True),
    sa.Column('CREATETIME', sa.DateTime(), nullable=False),
    sa.Column('STATUS', sa.String(length=1), nullable=False),
    sa.ForeignKeyConstraint(['IMAGEID'], ['image.IMAGEID'], ),
    sa.PrimaryKeyConstraint('ID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('container')
    op.drop_table('challenge')
    op.drop_table('image')
    # ### end Alembic commands ###