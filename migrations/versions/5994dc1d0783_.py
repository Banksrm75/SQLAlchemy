"""empty message

Revision ID: 5994dc1d0783
Revises: f506509c84d7
Create Date: 2024-11-28 00:10:20.482188

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5994dc1d0783'
down_revision = 'f506509c84d7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_name', sa.String(length=80), nullable=False),
    sa.Column('product_barcode', sa.Integer(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('category', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('product_barcode')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    # ### end Alembic commands ###
