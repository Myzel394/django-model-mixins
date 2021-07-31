from model_mixin_test import ModelMixinTestCase
from django_model_mixins.mixins import TokenMixin


class TokenMixinTest(ModelMixinTestCase):
    """Test cases for `TokenMixin`."""

    mixin = TokenMixin
    model: TokenMixin

    def test_creates_id(self):
        """Test if a random `token` is generated."""
        instance = self.model.objects.create()
        self.assertNotEqual("", instance.token)

    def test_id_length_is_derived_from_model(self):
        """Test if length is derived from the model."""
        old_value = self.model.TOKEN_LENGTH
        length = 10
        self.model.TOKEN_LENGTH = length

        instance = self.model.objects.create()
        self.assertEqual(length, len(instance.token))

        self.model.TOKEN_LENGTH = old_value

    def test_doesnt_create_id_if_is_false(self):
        """Test if a `token` is not generated when `CREATE_ON_CREATION = False`."""
        old_value = self.model.CREATE_ON_CREATION

        self.model.CREATE_ON_CREATION = False
        instance = self.model.objects.create()
        self.assertEqual("", instance.token)

        self.model.CREATE_ON_CREATION = old_value

    def test_token_can_be_recreated(self):
        """Test if a `token` can be recreated."""
        instance = self.model.objects.create()
        old_token = instance.token

        instance.recreate_token()
        instance.refresh_from_db()

        self.assertNotEqual(old_token, instance.token)
