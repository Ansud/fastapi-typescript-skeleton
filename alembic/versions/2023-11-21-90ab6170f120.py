"""empty message

Revision ID: 90ab6170f120
Revises:
Create Date: 2023-11-21 14:56:54.493135

"""
from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "90ab6170f120"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "rule",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("deleted", sa.Boolean(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "trade",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("price", sa.Numeric(), nullable=False),
        sa.Column("stoploss_initial", sa.Numeric(), nullable=False),
        sa.Column("stoploss_current", sa.Numeric(), nullable=False),
        sa.Column("result", sa.Numeric(), nullable=False),
        sa.Column("rule_enter_id", sa.BigInteger(), nullable=True),
        sa.Column("rule_exit_id", sa.BigInteger(), nullable=True),
        sa.Column(
            "market_state", sa.Enum("trend_bull", "trend_bear", "flat", "undefined", name="marketstate"), nullable=False
        ),
        sa.Column("comment", sa.String(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.ForeignKeyConstraint(["rule_enter_id"], ["rule.id"], name="fk_enter_rule"),
        sa.ForeignKeyConstraint(["rule_exit_id"], ["rule.id"], name="fk_exit_rule"),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("trade")
    op.drop_table("rule")
