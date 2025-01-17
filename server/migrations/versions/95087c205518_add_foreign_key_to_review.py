"""add foreign key to Review

Revision ID: 95087c205518
Revises: 2cf5186dea99
Create Date: 2024-02-22 07:20:00.059510

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95087c205518'
down_revision = '2cf5186dea99'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reviews', sa.Column('employee_id', sa.Integer(), nullable=True))
    op.create_foreign_key(op.f('fk_reviews_employee_id_employees'), 'reviews', 'employees', ['employee_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_reviews_employee_id_employees'), 'reviews', type_='foreignkey')
    op.drop_column('reviews', 'employee_id')
    # ### end Alembic commands ###
