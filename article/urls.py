from django.urls import path

from article.views import ArticleListView, ArticleCreateView, ArticleDetailView, ArticleChangeView

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('create-article/', ArticleCreateView.as_view(), name='article_create'),
    path('detail-article/<slug:slug>/', ArticleDetailView.as_view(), name='article_detail'),
    path('change/<slug:slug>/', ArticleChangeView.as_view(), name='article_change'),
]
