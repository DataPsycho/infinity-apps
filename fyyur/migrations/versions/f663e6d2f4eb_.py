"""empty message

Revision ID: f663e6d2f4eb
Revises: ed56bd440688
Create Date: 2020-01-06 23:48:39.119292

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f663e6d2f4eb'
down_revision = 'ed56bd440688'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Artist_Geners',
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('gener_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['Artist.id'], ),
    sa.ForeignKeyConstraint(['gener_id'], ['Gener.id'], ),
    sa.PrimaryKeyConstraint('artist_id', 'gener_id')
    )
    op.alter_column('Gener', 'gener',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Gener', 'gener',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.drop_table('Artist_Geners')
    # ### end Alembic commands ###