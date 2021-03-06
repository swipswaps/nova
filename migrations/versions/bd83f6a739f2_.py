"""empty message

Revision ID: bd83f6a739f2
Revises: e645ddac7dad
Create Date: 2017-10-13 21:38:38.417677

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd83f6a739f2'
down_revision = 'e645ddac7dad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fund',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('council', sa.Integer(), nullable=True),
    sa.Column('budget', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('expense',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('budget', sa.Float(), nullable=True),
    sa.Column('spent', sa.Float(), nullable=True),
    sa.Column('fund_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['fund_id'], ['fund.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('expense')
    op.drop_table('fund')
    # ### end Alembic commands ###
