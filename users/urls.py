from django.urls import path, include

from users import views
from users.views import Register, Login, PasswordReset

urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path("login/", Login.as_view(), name="login"),
    path("password_reset/", PasswordReset.as_view(), name="password_reset"),
]
