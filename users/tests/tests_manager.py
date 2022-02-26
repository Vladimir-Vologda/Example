from django.contrib.auth import get_user_model
from django.test import TestCase


class TestCustomUserManager(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            name='TestUser', password='test_password'
        )

        self.assertEqual(user.name, 'TestUser')
        self.assertNotEqual(user.name, 'UserTest')
        self.assertTrue(user.is_active)
        self.assertFalse(not user.is_active)
        self.assertFalse(user.is_admin)

        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(ValueError):
            User.objects.create_user(
                name='',
            )

    def test_create_superuser(self):
        User = get_user_model()
        super_user = User.objects.create_superuser(
            name='SuperUser', password='super_password'
        )

        self.assertEqual(super_user.name, 'SuperUser')
        self.assertNotEqual(super_user.name, 'NoSuperUser')
        self.assertTrue(super_user.is_active)
        self.assertTrue(super_user.is_admin)
        self.assertFalse(not super_user.is_active)
        self.assertFalse(not super_user.is_admin)

        with self.assertRaises(TypeError):
            User.objects.create_superuser()
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                name='',
            )
