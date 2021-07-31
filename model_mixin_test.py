from typing import *

from django.db import models
from django.db import connection
from django.test import TestCase
from django.db.models.base import ModelBase

__all__ = [
    "ModelMixinTestCase"
]


class ModelMixinTestCase(TestCase):
    """Test Case for abstract mixin models.

    Subclass and set cls.mixin to your desired mixin.
    access your model using cls.model.
    """

    mixin: Type[models.Model]
    model: Type[models.Model]

    @classmethod
    def setUpClass(cls) -> None:
        """Create a real model based on `mixin`."""
        cls.model = ModelBase(
            "__Test" + cls.mixin.__name__,
            (cls.mixin,),
            {"__module__": cls.mixin.__module__}
        )

        # Use schema_editor to create schema
        with connection.schema_editor() as editor:
            editor.create_model(cls.model)

        super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        """Delete model from database."""
        # allow the transaction to exit
        super().tearDownClass()

        # Use schema_editor to delete schema
        with connection.schema_editor() as editor:
            editor.delete_model(cls.model)

        # close the connection
        connection.close()
