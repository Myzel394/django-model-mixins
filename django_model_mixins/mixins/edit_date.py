from django.db import models

__all__ = [
    "EditDateMixin"
]


class EditDateMixin(models.Model):
    """Mixin to create a `edited_at` field which is automatically set on model update."""

    class Meta:
        """Meta class."""

        abstract = True

    edited_at = models.DateTimeField(
        auto_now=True
    )
