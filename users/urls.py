from django.urls import path, include
from users.views import Register, Login, PasswordChange, PasswordChangeDone, PasswordReset, PasswordResetDone, Logout, \
    Profile

urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path("login/", Login.as_view(), name="login"),
    path("password_change/", PasswordChange.as_view(), name="password_change"),
    path("password_change/done/", PasswordChangeDone.as_view(), name="password_change_done"),
    path("password_reset/", PasswordReset.as_view(), name="password_reset"),
    path("password_reset/done/", PasswordResetDone.as_view(), name="password_reset_done"),
    path(" ", Logout.as_view(), name="logout"),
    path("profile/", Profile.as_view(), name="profile"),
]
