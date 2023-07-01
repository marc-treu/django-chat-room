from django.conf import settings
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


def pytest_configure():
    settings.configure(
        CHANNEL_LAYERS={
            "default": {
                "BACKEND": "channels.layers.InMemoryChannelLayer",
            },
        },

        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "TEST": {
                    "NAME": BASE_DIR / "db.sqlite3",
                },
            }
        },
        INSTALLED_APPS=[
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sessions",
            "django.contrib.admin",
            "channels",
        ],
        SECRET_KEY="Not_a_secret_key",
    )
