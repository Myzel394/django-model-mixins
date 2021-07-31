from datetime import datetime, timedelta, timezone

from django.db import models

from .token import TokenMixin

__all__ = [
    "TokenGeneratedAtMixin"
]


class TokenGeneratedAtMixin(TokenMixin):
    """Inherits `TokenMixin` and add a `token_generated` field.

    This class expects a field called `TOKEN_VALID_DURATION_IN_SECONDS` which is an int
    indicating how long a `token` is valid (duration in seconds).

    `token_generated` saves when the given `token` has been generated.
    """

    class Meta:
        """Meta class."""

        abstract = True

    # Duration in seconds
    TOKEN_VALID_DURATION_IN_SECONDS: int

    token_generated = models.DateTimeField(
        blank=True,
        null=True
    )

    @property
    def expire_date(self) -> datetime:
        """Return the datetime this token will expire."""
        return self.token_generated + timedelta(seconds=self.TOKEN_VALID_DURATION_IN_SECONDS)

    @property
    def is_expired(self) -> bool:
        """Return whether this token has expired."""
        return self.expire_date <= timezone.now()

    def _create_token(self):
        """Generate a new token and set it."""
        super()._create_token()
        self.token_generated = timezone.now()

