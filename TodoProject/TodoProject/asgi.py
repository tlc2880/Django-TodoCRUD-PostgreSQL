"""
# Name: Tommy Cao
# Original Date: 11/04/16
# Updated: 3/3/20
# Description: Django Todo Create Read Update Delete (CRUD) with PostgreSQL.
# Using 'pipenv' for virtual environment.

"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TodoProject.settings')

application = get_asgi_application()
