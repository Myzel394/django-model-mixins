import secrets

from django.conf import settings
from django.db import models

from .. import constants

__all__ = [
    "TokenMixin"
]

TOKEN_MAX_LENGTH = getattr(settings, "TOKEN_MAX_LENGTH", constants.DEFAULT_RANDOM_ID_MAX_LENGTH)
TOKEN_CHARS = getattr(settings, "TOKEN_ID_CHARS", constants.DEFAULT_RANDOM_ID_CHARS)
CREATE_ON_CREATION = getattr(
    settings, "TOKEN_CREATE_ON_CREATION", constants.TOKEN_CREATE_ON_CREATION
)


class TokenMixin(models.Model):
    """Create a `token` field with the ability to change it."""

    class Meta:
        """Meta class."""

        abstract = True

    TOKEN_LENGTH = TOKEN_MAX_LENGTH
    TOKEN_CHARS = TOKEN_CHARS
    CREATE_ON_CREATION = CREATE_ON_CREATION

    token = models.CharField(
        max_length=TOKEN_MAX_LENGTH
    )

    @classmethod
    def _generate_token(cls) -> str:
        """Generate a token and return it.

        This function just generates a token.
        """
        assert cls.TOKEN_LENGTH <= TOKEN_MAX_LENGTH, \
            f"`TOKEN_LENGTH` can be at most `{TOKEN_MAX_LENGTH}`"

        return "".join(
            secrets.choice(cls.TOKEN_CHARS)
            for _ in range(cls.TOKEN_LENGTH)
        )

    def _create_token(self):
        """Generate a new token and set it."""
        self.token = self._generate_token()

    def recreate_token(self):
        """Recreates the token and saves it."""
        self._create_token()
        self.save()

    def save(self, *args, **kwargs):
        """Create a token if necessary and allowed."""
        if self.token == "" and self.CREATE_ON_CREATION:
            self._create_token()

        return super().save(*args, **kwargs)
