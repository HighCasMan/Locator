from django.urls import path, include
from django.views.generic import TemplateView
from users import views
from users.views import Register, Login, PasswordReset

urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path("login/", Login.as_view(), name="login"),
    path("password_reset/", PasswordReset.as_view(), name="password_reset"),
    path('mainpage/', TemplateView.as_view(template_name='main.html'), name='mainpage'),
    path('search/', TemplateView.as_view(template_name='../templates/search.html'), name='search'),
]
