from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class ArticleModel(models.Model):
    author = models.ForeignKey(get_user_model(), verbose_name='Author', on_delete=models.PROTECT)
    title = models.CharField(_('Title'), max_length=50)
    description = models.CharField(_('Description'), max_length=250)
    text = models.TextField(_('Article text'))
    image = models.ImageField(_('Image'), upload_to='article/', default='default/article_default.jpg')
    slug = models.SlugField(_('URL-address'), unique=True, db_index=True)

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _("Article's")

    def __str__(self):
        return f'{self.title} - ({self.author})'

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.title[:25])
        super(ArticleModel, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})
