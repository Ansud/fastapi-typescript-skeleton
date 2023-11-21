from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker, create_async_engine
from sqlalchemy.pool import AsyncAdaptedQueuePool

from app.core.settings import settings


def create_db_engine() -> AsyncEngine:
    if settings.DB_URI_ASYNC is None:
        raise NotImplementedError("DB_URI_ASYNC is not configured")

    return create_async_engine(
        settings.DB_URI_ASYNC.unicode_string(),
        pool_pre_ping=True,
        isolation_level="READ COMMITTED",
        poolclass=AsyncAdaptedQueuePool,
    )


async_engine = create_db_engine()
async_session = async_sessionmaker(bind=async_engine, expire_on_commit=False)
