from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, UpdateView, DetailView

from users.forms import CustomUserCreateForm, CustomUserChangeForm
from users.models import CustomUserModel


class CustomRegistrationView(CreateView):
    form_class = CustomUserCreateForm
    model = CustomUserModel
    template_name = 'users/custom_registration_view.html'
    context_object_name = 'form'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super(CustomRegistrationView, self).get_context_data(**kwargs)
        context['title'] = _('Registration')
        return context


class CustomLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/custom_login_view.html'

    def get_context_data(self, **kwargs):
        context = super(CustomLoginView, self).get_context_data(**kwargs)
        context['title'] = _('Authentication of account')
        return context


class CustomDetailView(DetailView):
    model = CustomUserModel
    template_name = 'users/custom_detail_view.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super(CustomDetailView, self).get_context_data(**kwargs)
        context['title'] = context['user']
        return context


class CustomChangeView(UpdateView):
    form_class = CustomUserChangeForm
    model = CustomUserModel
    template_name = 'users/custom_change_view.html'
    context_object_name = 'form'
    success_url = reverse_lazy('')

    def get_context_data(self, **kwargs):
        context = super(CustomChangeView, self).get_context_data(**kwargs)
        context['title'] = _('Update of account')
        return context


class CustomLogoutView(LogoutView):

    def get_context_data(self, **kwargs):
        context = super(CustomLogoutView, self).get_context_data(**kwargs)
        return context
