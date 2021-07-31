from boot_django import boot_django
from model_mixin_test import ModelMixinTestCase

boot_django()

from django_model_mixins.mixins import RandomIDMixin


class RandomIDMixinTest(ModelMixinTestCase):
    """Test cases for `RandomIDMixin`."""

    mixin = RandomIDMixin
    model: RandomIDMixin

    def test_creates_id(self):
        """Test if a random `id` is generated."""
        instance = self.model.objects.create()
        self.assertIsNotNone(instance.id)
        self.assertNotEqual("", instance.id)

    def test_id_length_is_derived_from_model(self):
        """Test if length is derived from the model."""
        old_value = self.model.ID_LENGTH
        length = 10
        self.model.ID_LENGTH = length
        instance = self.model.objects.create()
        self.assertEqual(length, len(instance.id))
        self.model.ID_LENGTH = old_value
