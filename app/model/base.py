from datetime import UTC, datetime
from typing import Self

from sqlalchemy import BigInteger, DateTime
from sqlalchemy.ext.asyncio import AsyncSession, async_object_session
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql import exists, func, select


def datetime_utcnow() -> datetime:
    return datetime.now(UTC)


NO_DELETE = "save-update, merge, expunge"


class BaseModel(DeclarativeBase):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime_utcnow,
        server_default=func.now(),
    )

    @classmethod
    async def get(cls, db: AsyncSession, id: int) -> Self | None:
        return await db.get(cls, id)

    @classmethod
    async def exists(cls, db: AsyncSession, id: int) -> bool:
        result = await db.execute(select(exists().where(cls.id == id)))
        return result.scalar()

    @classmethod
    async def all(cls, db: AsyncSession) -> list[Self]:
        return list(await db.scalars(select(cls).order_by([cls.id])))

    @property
    def db(self) -> AsyncSession:
        db = async_object_session(self)

        if db is None:
            raise RuntimeError("DB instance (AsyncSession) is None. Can not continue.")

        return db

    async def delete(self) -> None:
        await self.db.delete(self)
