from django.contrib import admin
from django.urls import path, include

from users.views import LocationsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LocationsView.as_view(), name='home'),
    path('users/', include('users.urls')),
  
]
