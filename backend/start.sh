#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

# Apply database migrations
python manage.py migrate

# Run the application
python manage.py runserver 0.0.0.0:8000
