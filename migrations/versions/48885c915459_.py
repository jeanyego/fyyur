"""empty message

Revision ID: 48885c915459
Revises: 8f5a4dfcdcfa
Create Date: 2022-06-11 08:56:44.417650

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48885c915459'
down_revision = '8f5a4dfcdcfa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Artist', 'seeking_venue',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.drop_column('Show', 'id')
    op.alter_column('Venue', 'genres',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Venue', 'genres',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.add_column('Show', sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Show_id_seq"\'::regclass)'), autoincrement=True, nullable=False))
    op.alter_column('Artist', 'seeking_venue',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    # ### end Alembic commands ###