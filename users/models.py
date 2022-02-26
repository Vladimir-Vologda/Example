from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _

from users.managers import CustomUserManager


class CustomUserModel(AbstractBaseUser):
    name = models.CharField(_('Username'), max_length=50, unique=True, db_index=True)
    date_birth = models.DateField(_('Date of Birth'), default='2001-01-01')
    is_active = models.BooleanField(_('Status active'), default=True)
    is_admin = models.BooleanField(_('Status admin'), default=False)
    slug = models.SlugField(_('URL-address'), unique=True, db_index=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.slug)
        super(CustomUserModel, self).save(**kwargs)

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def is_staff(self):
        return self.is_admin
