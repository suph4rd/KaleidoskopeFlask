"""add user

Revision ID: ed7c69393415
Revises: 59283cf535b4
Create Date: 2021-11-20 20:04:40.554613

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed7c69393415'
down_revision = '59283cf535b4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.Column('password_hash', sa.String(length=255), nullable=False),
    sa.Column('first_name', sa.String(length=255), nullable=True),
    sa.Column('last_name', sa.String(length=255), nullable=True),
    sa.Column('patronymic', sa.String(length=255), nullable=True),
    sa.Column('role', sa.Enum('common', 'admin', name='roleenum'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###