import tempfile

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from article.models import ArticleModel

Author = get_user_model()
Article = ArticleModel
Image = tempfile.NamedTemporaryFile(prefix='TestImage', suffix=".jpg").name
UpdateImage = tempfile.NamedTemporaryFile(prefix='UpdateTestImage', suffix=".jpg").name


class TestArticleView(TestCase):

    def setUp(self) -> None:
        self.name = 'TestUser'
        self.password = 'test_password'
        self.author = Author.objects.create_user(
            name=self.name, password=self.password
        )
        self.client.login(name=self.name, password=self.password)

        self.article = Article.objects.create(
            author=self.author, title='TestTitle', description='TestDescription',
            text='TestText', image=Image,
        )

        self.client.logout()

    def test_list_view(self):
        response = self.client.get(reverse('article_list'))
        self.assertEqual(response.status_code, 200)

    def test_detail_view(self):
        response = self.client.get('/article/detail-article/testtitle/')
        self.assertEqual(response.status_code, 200)

    def test_create_view(self):
        self.client.login(name=self.name, password=self.password)
        response = self.client.post(
            reverse('article_create'),
            {'author': self.author, 'title': 'TestTitleView', 'description': 'TestDescription',
             'text': 'TestText', 'image': Image}
        )

        self.assertEqual(response.status_code, 302)

    def test_update_view(self):

        response = self.client.post(
            reverse('article_change', kwargs={'slug': self.article.slug}),
            {'author': self.author, 'title': 'UpdateTestTitle', 'description': 'UpdateTestDescription',
             'text': 'UpdateTestText', 'image': UpdateImage}
        )

        self.assertEqual(response.status_code, 302)

        self.article.refresh_from_db()

        self.assertEqual(self.article.author.name, 'TestUser')
        self.assertEqual(self.article.title, 'UpdateTestTitle')
        self.assertEqual(self.article.description, 'UpdateTestDescription')
        self.assertEqual(self.article.text, 'UpdateTestText')
        self.assertEqual(self.article.image, self.article.image.name)
        self.assertEqual(self.article.slug, 'testtitle')
