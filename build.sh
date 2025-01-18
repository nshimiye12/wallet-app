#!/bin/bash
# Exit immediately if a command exits with a non-zero status
set -e

# Install dependencies
if [ -f requirements.txt ]; then
    pip install -r requirements.txt
else
    echo "requirements.txt not found."
    exit 1
fi

# Apply database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput
