from django.contrib.auth import get_user_model
from django.test import TestCase


class UserTests(TestCase):
    User = get_user_model()

    def test_create_user(self):
        user = self.User.objects.create_user(phone='09135551460', password='RezaY123654789')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_mentor)

    def test_create_mentor(self):
        user = self.User.objects.create_mentor(phone='09135551461', password='RezaY123654789')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.is_mentor)

    def test_create_superuser(self):
        user = self.User.objects.create_superuser(phone='09135551462', password='RezaY123654789')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        self.assertFalse(user.is_mentor)
