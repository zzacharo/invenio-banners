#
# This file is part of Invenio.
# Copyright (C) 2016-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Create invenio-banners db table."""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e02314da32e'
down_revision = 'e40d93d99040'
branch_labels = ()
depends_on = None


def upgrade():
    """Upgrade database."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('banners',
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('updated', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('message', sa.Text(), nullable=False),
    sa.Column('url_path', sa.String(length=255), nullable=True),
    sa.Column('category', sa.String(length=20), nullable=False),
    sa.Column('start_datetime', sa.DateTime(), nullable=False),
    sa.Column('end_datetime', sa.DateTime(), nullable=True),
    sa.Column('active', sa.Boolean(name='active'), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_banners'))
    )
    # ### end Alembic commands ###


def downgrade():
    """Downgrade database."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('banners')
    # ### end Alembic commands ###
