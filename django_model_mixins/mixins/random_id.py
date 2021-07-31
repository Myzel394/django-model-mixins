import secrets

from django.conf import settings
from django.db import models

from .. import constants

__all__ = [
    "RandomIDMixin"
]

ID_MAX_LENGTH = getattr(settings, "RANDOM_ID_MAX_LENGTH", constants.DEFAULT_RANDOM_ID_MAX_LENGTH)
ID_CHARS = getattr(settings, "RANDOM_ID_CHARS", constants.DEFAULT_RANDOM_ID_CHARS)


class RandomIDMixin(models.Model):
    """Add a `id` field which is randomly set and unchangeable."""

    class Meta:
        """Meta class."""

        abstract = True

    ID_LENGTH = ID_MAX_LENGTH
    ID_CHARS = ID_CHARS

    id = models.CharField(
        max_length=ID_MAX_LENGTH,
        primary_key=True,
        unique=True,
        editable=False
    )

    @classmethod
    def _generate_id(cls) -> str:
        """Generate a cryptographically randomly and unique id.

        You can override this function if you want to change the generation.
        This function doesn't set the `id` - it only generates and returns it.
        """
        assert cls.ID_LENGTH <= ID_MAX_LENGTH, f'`ID_LENGTH` can be at most `{ID_MAX_LENGTH}`.'

        # Create an id until it's available

        # Because of the fact, that it's very unlikely that an id will be taken already,
        # we will do a database lookup instead of saving the ids in a set. This reduces the
        # amount of data that must be stored in the memory.

        while True:
            random_id = "".join(
                secrets.choice(cls.ID_CHARS)
                for _ in range(cls.ID_LENGTH)
            )

            # Check availability
            id_taken = cls.objects.only("id").filter(id=random_id).exists()
            if not id_taken:
                return random_id

    def save(self, *args, **kwargs):
        """Automatically set `id`."""
        if not self.id:
            self.id = self._generate_id()

        return super().save(*args, **kwargs)
