"""init

Revision ID: 59283cf535b4
Revises: 
Create Date: 2021-11-14 22:43:57.065141

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59283cf535b4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('content',
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('type', sa.String(length=255), nullable=False),
    sa.Column('link', sqlalchemy_utils.types.url.URLType(), nullable=True),
    sa.Column('img', sqlalchemy_utils.types.url.URLType(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('footer',
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('footer')
    op.drop_table('content')
    # ### end Alembic commands ###
