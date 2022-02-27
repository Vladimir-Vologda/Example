from django.urls import path

from users.views import CustomRegistrationView, CustomLoginView, CustomChangeView, CustomLogoutView

urlpatterns = [
    path('registration/', CustomRegistrationView.as_view(), name='registration'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('change/<slug:slug>/', CustomChangeView.as_view(), name='change'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
