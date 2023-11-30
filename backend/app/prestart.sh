#!/bin/sh
set -e

# Check that all services are up
python /app/app/prestart_app.py

# Run migrations
alembic upgrade head

# Load predefined fixtures
python /app/app/load_fixtures.py

