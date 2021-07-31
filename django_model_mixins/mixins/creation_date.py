from django.db import models

__all__ = [
    "CreationDateMixin"
]


class CreationDateMixin(models.Model):
    """Add a `created_at` field which is automatically set on model creation."""

    class Meta:
        """Meta class."""

        abstract = True

    created_at = models.DateTimeField(
        auto_now_add=True
    )
