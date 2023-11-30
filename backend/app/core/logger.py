import json

import structlog
from core.settings import settings


def _logger_configure(log_level: int) -> None:
    structlog.configure(
        cache_logger_on_first_use=True,
        wrapper_class=structlog.make_filtering_bound_logger(log_level),
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.processors.add_log_level,
            structlog.processors.format_exc_info,
            structlog.processors.TimeStamper(fmt="iso", utc=True),
            structlog.processors.JSONRenderer(serializer=lambda x: json.dumps(x, default=str)),
        ],
        logger_factory=structlog.BytesLoggerFactory(),
    )


_logger_configure(settings.LOG_LEVEL)

app_logger = structlog.get_logger()
