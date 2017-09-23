"""empty message

Revision ID: f7008f92ddb0
Revises: be659a06342b
Create Date: 2017-09-23 13:03:52.189250

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f7008f92ddb0'
down_revision = 'be659a06342b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('share',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_created', sa.DateTime(timezone=True), server_default=sa.text(u'CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('date_updated', sa.DateTime(timezone=True), server_default=sa.text(u'CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.Column('red_packet_token', sa.String(length=8), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_share_date_created'), 'share', ['date_created'], unique=False)
    op.create_index(op.f('ix_share_date_updated'), 'share', ['date_updated'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_share_date_updated'), table_name='share')
    op.drop_index(op.f('ix_share_date_created'), table_name='share')
    op.drop_table('share')
    # ### end Alembic commands ###
