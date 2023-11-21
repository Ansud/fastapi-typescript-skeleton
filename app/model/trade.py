from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .rule import Rule

from decimal import Decimal
from enum import Enum
from typing import Annotated

from .base import BaseModel

PriceInPoints = Annotated[Decimal, 6]


class MarketState(str, Enum):
    trend_bull = "bull"
    trend_bear = "bear"
    flat = "flat"
    undefined = "undefined"


class Trade(BaseModel):
    __tablename__ = "trade"

    # Entrance price
    price: Mapped[PriceInPoints]

    # Initial stop loss
    stoploss_initial: Mapped[PriceInPoints]

    # Final stop loss [it can differ from initial one because it can be trailing in any way]
    stoploss_current: Mapped[PriceInPoints]

    # The result of the trade [in points]
    result: Mapped[PriceInPoints]

    # Entrance by rule
    rule_enter_id: Mapped[int | None] = mapped_column(ForeignKey("rule.id", name="fk_enter_rule"))
    rule_enter: Mapped[Rule] = relationship(back_populates="enter_trades", lazy="selectin")

    # Exit by rule
    rule_exit_id: Mapped[int | None] = mapped_column(ForeignKey("rule.id", name="fk_exit_rule"))
    rule_exit: Mapped[Rule] = relationship(back_populates="exit_trades", lazy="selectin")

    market_state: Mapped[MarketState] = mapped_column(default=MarketState.undefined)

    comment: Mapped[str | None]
