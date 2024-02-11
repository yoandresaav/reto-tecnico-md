#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

# Apply database migrations
python manage.py migrate

# fixtures have pk so it rewrite the same data
python manage.py loaddata ./data/dump.json

# Run tests
pytest

# Run the application
python manage.py runserver 0.0.0.0:8000
