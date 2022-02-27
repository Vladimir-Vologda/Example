from django.contrib import admin

from article.models import ArticleModel


def get_description(self):
    return self.description[:25]


get_description.short_description = 'Description'


@admin.register(ArticleModel)
class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', get_description, 'image', 'slug')
    list_display_links = ('title', 'slug')
    list_filter = ('author',)
    search_fields = ('title',)
    prepopulated_fields = {
        'slug': ('title',)
    }
