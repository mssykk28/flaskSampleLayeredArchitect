"""initialize

Revision ID: f2d86a445825
Revises:
Create Date: 2022-04-03 10:00:00
"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.mysql import BOOLEAN, INTEGER, TIMESTAMP, VARCHAR

# revision identifiers, used by Alembic.
revision = "f2d86a445825"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():  # noqa
    op.create_table(
        "example",
        sa.Column("id", INTEGER, primary_key=True, autoincrement=True),
        sa.Column("example_string", VARCHAR(50), nullable=False),
        sa.Column("example_number", INTEGER, nullable=True),
        sa.Column("example_datetime", TIMESTAMP, nullable=True),
        sa.Column("example_boolean", BOOLEAN, nullable=True),
    )


def downgrade():  # noqa
    op.drop_table("example")
