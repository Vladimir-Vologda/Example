import tempfile

from django.contrib.auth import get_user_model
from django.test import TestCase

from article.models import ArticleModel


class TestArticleModel(TestCase):

    def test_article_model(self):
        Article = ArticleModel
        Author = get_user_model()
        image = tempfile.NamedTemporaryFile(prefix='TestImage', suffix=".jpg").name
        user = Author.objects.create_user(
            name='TestUser', password='test_password',
        )
        article = Article.objects.create(
            author=user, title='TestTitle', description='TestDescription', text='TestText',
            image=image,
        )

        self.assertEqual(article.author, user)
        self.assertEqual(article.author.name, 'TestUser')
        self.assertEqual(article.title, 'TestTitle')
        self.assertEqual(article.description, 'TestDescription')
        self.assertEqual(article.text, 'TestText')
        self.assertEqual(article.slug, 'testtitle')
        self.assertEqual(article.image, article.image.name)

        #   test verbose_name
        field_label = article._meta.get_field('author').verbose_name
        self.assertEquals(field_label, 'Author')

        #   test verbose_name
        field_label = article._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'Title')

        #   test verbose_name
        field_label = article._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'Description')

        #   test verbose_name
        field_label = article._meta.get_field('text').verbose_name
        self.assertEquals(field_label, 'Article text')

        #   test verbose_name
        field_label = article._meta.get_field('image').verbose_name
        self.assertEquals(field_label, 'Изображение' or 'Image')

        #   test verbose_name
        field_label = article._meta.get_field('slug').verbose_name
        self.assertEquals(field_label, 'URL-address')

        #   test max_length
        max_length = article._meta.get_field('title').max_length
        self.assertEquals(max_length, 50)

        #   test max_length
        max_length = article._meta.get_field('description').max_length
        self.assertEquals(max_length, 250)

        #   test def __str__
        expected_object_name = f'{article.title} - ({article.author})'
        self.assertEquals(expected_object_name, str(article))

        #   test get_absolute_url
        self.assertEquals(article.get_absolute_url(), '/article/detail-article/testtitle/')

        self.client.logout()
