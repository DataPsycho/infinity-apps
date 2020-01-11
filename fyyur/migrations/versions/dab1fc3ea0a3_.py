"""empty message

Revision ID: dab1fc3ea0a3
Revises: a6a9f7c60f33
Create Date: 2020-01-11 20:55:49.949098

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dab1fc3ea0a3'
down_revision = 'a6a9f7c60f33'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'City', ['city'])
    op.create_unique_constraint(None, 'Gener', ['gener'])
    op.create_unique_constraint(None, 'State', ['state'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'State', type_='unique')
    op.drop_constraint(None, 'Gener', type_='unique')
    op.drop_constraint(None, 'City', type_='unique')
    # ### end Alembic commands ###