from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, DetailView

from article.forms import CustomCreateArticleForm
from article.models import ArticleModel


class ArticleListView(ListView):
    model = ArticleModel
    template_name = 'article/article_list_view.html'
    context_object_name = 'form'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['title'] = _("Article's")
        return context


class ArticleCreateView(CreateView):
    form_class = CustomCreateArticleForm
    model = ArticleModel
    template_name = 'article/article_create_view.html'
    context_object_name = 'form'
    success_url = reverse_lazy('article_list')

    def get_context_data(self, **kwargs):
        context = super(ArticleCreateView, self).get_context_data(**kwargs)
        context['title'] = _('Create article')
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(ArticleCreateView, self).form_valid(form)


class ArticleDetailView(DetailView):
    model = ArticleModel
    template_name = 'article/article_detail_view.html'
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['title'] = context['form']
        return context
