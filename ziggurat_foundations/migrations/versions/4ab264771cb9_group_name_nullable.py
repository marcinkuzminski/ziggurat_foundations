"""group_name made nullable
Revision ID: 4ab264771cb9
Revises: None
Create Date: 2013-11-22 00:04:21.631000
"""


# revision identifiers, used by Alembic.
revision = '4ab264771cb9'
down_revision = '439766f6104d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # commands auto generated by Alembic - please adjust! ###
    op.alter_column('groups', 'group_name',
                    existing_type=sa.VARCHAR(length=128),
                    nullable=True)
    # end Alembic commands ###


def downgrade():
    # commands auto generated by Alembic - please adjust! ###
    op.alter_column('groups', 'group_name',
                    existing_type=sa.VARCHAR(length=128),
                    nullable=False)
    # end Alembic commands ###
