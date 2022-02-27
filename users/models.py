from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from users.managers import CustomUserManager


def img_dir(instance, filename):
    return f'users/{instance.name}/{filename}'


class CustomUserModel(AbstractBaseUser):
    name = models.CharField(_('Username'), max_length=50, unique=True, db_index=True)
    phone = PhoneNumberField(_('Phone number'), unique=True, null=True)
    first_name = models.CharField(_('Name'), max_length=50, blank=True)
    last_name = models.CharField(_('Surname'), max_length=50, blank=True)
    date_birth = models.DateField(_('Date of Birth'), default='2001-01-01')
    avatar = models.ImageField(_('Image'), upload_to=img_dir, default='default/user_default.jpg')
    is_active = models.BooleanField(_('Status active'), default=True)
    is_admin = models.BooleanField(_('Status admin'), default=False)
    slug = models.SlugField(_('URL-address'), unique=True, db_index=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.name)
        super(CustomUserModel, self).save(**kwargs)

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    # def get_absolute_url(self):
    #     return reverse('user_detail', kwargs={
    #         'slug': self.slug
    #     })
