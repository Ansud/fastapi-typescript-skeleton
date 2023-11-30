#!/bin/sh
set -e

echo "Execute prestart script"
/app/app/prestart.sh

echo "Start app"
python /app/app/main.py
