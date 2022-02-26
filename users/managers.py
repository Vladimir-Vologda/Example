from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):

    def create_user(self, name, password=None):
        """
        Create and save user
        """
        if not name:
            raise ValueError(_('Users must have an username'))

        user = self.model(
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, password=None):
        """
        Create and save superuser
        """
        user = self.create_user(
            name=name,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
