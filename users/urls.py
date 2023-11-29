from django.urls import path, include
from django.views.generic import TemplateView

from users.views import Register
from .views import example

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('example/', example, name="example"),
]
