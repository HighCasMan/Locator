from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('users/', include('users.urls')),
    path('mainpage/', TemplateView.as_view(template_name='main.html'), name='mainpage'),
]
