"""empty message

Revision ID: 83d2f6966b5f
Revises: 16adcf32a319
Create Date: 2022-06-06 13:52:57.426460

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83d2f6966b5f'
down_revision = '16adcf32a319'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('website_link', sa.String(length=120), nullable=True))
    op.add_column('Artist', sa.Column('seeking_venues', sa.Boolean(), nullable=False))
    op.add_column('Artist', sa.Column('seeking_description', sa.String(length=500), nullable=True))
    op.alter_column('Venue', 'seeking_talent',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Venue', 'seeking_talent',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.drop_column('Artist', 'seeking_description')
    op.drop_column('Artist', 'seeking_venues')
    op.drop_column('Artist', 'website_link')
    # ### end Alembic commands ###
