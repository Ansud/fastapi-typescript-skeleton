from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, WriteOnlyMapped, mapped_column, relationship
from typing_extensions import override

if TYPE_CHECKING:
    from .trade import Trade

from .base import NO_DELETE, BaseModel


class Rule(BaseModel):
    __tablename__ = "rule"

    # The rule entry can not be deleted because it is used in the trade
    deleted: Mapped[bool] = mapped_column(default=False)

    name: Mapped[str]
    description: Mapped[str]

    enter_trades: WriteOnlyMapped[Trade] = relationship(
        back_populates="rule_exit", cascade=NO_DELETE, order_by="Trade.created_at.asc()"
    )

    exit_trades: WriteOnlyMapped[Trade] = relationship(
        back_populates="rule_enter", cascade=NO_DELETE, order_by="Trade.created_at.asc()"
    )

    @override
    async def delete(self) -> None:
        self.deleted = True
