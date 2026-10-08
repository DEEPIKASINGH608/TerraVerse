"""initial_schema

Revision ID: 0001_initial_schema
Revises:
Create Date: 2026-10-06 22:00:00.000000

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from geoalchemy2 import Geometry

revision: str = '0001_initial_schema'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'datasets',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('department', sa.String(), nullable=False),
        sa.Column('file_type', sa.String(), nullable=False),
        sa.Column('status', sa.String(), default='RAW'),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now()),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'parcels',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('upi', sa.String(), nullable=False, unique=True),
        sa.Column('khasra_number', sa.String(), nullable=True),
        sa.Column('owner_name', sa.String(), nullable=True),
        sa.Column('confidence_score', sa.Float(), default=0.0),
        sa.Column('requires_review', sa.Boolean(), default=False),
        sa.Column('geometry', Geometry(geometry_type='POLYGON', srid=4326), nullable=True),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now()),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'conflicts',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('parcel_upi', sa.String(), nullable=False),
        sa.Column('conflict_type', sa.String(), nullable=False),
        sa.Column('severity', sa.String(), default='MEDIUM'),
        sa.Column('status', sa.String(), default='OPEN'),
        sa.Column('details', sa.JSON(), nullable=True),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now()),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('conflicts')
    op.drop_table('parcels')
    op.drop_table('datasets')