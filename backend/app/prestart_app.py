import asyncio
import logging

from sqlalchemy import text
from tenacity import after_log, before_log, retry, stop_after_attempt, wait_fixed

from app.core.db import async_session

logger = logging.getLogger()

max_tries = 60
wait_seconds = 1


@retry(
    stop=stop_after_attempt(max_tries),
    wait=wait_fixed(wait_seconds),
    before=before_log(logger, logging.INFO),
    after=after_log(logger, logging.WARN),
)
async def init() -> None:
    try:
        async with async_session() as db:
            await db.execute(text("SELECT 1"))
    except Exception as e:
        logger.error(e)
        raise e


async def main() -> None:
    await init()


if __name__ == "__main__":
    asyncio.run(main())
