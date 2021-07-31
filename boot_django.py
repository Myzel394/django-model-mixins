# https://realpython.com/installable-django-app/
import os

import django
from django.conf import settings

__all__ = [
    "boot_django"
]

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "django_model_mixins"))


def boot_django():
    """Boot Django with minimal configuration."""
    settings.configure(
        BASE_DIR=BASE_DIR,
        DEBUG=True,
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
            }
        },
        INSTALLED_APPS=(
            "django_model_mixins",
        ),
        TIME_ZONE="EST",
    )
    django.setup()
