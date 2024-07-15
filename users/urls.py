from django.urls import path, include
from users.views import Register, Login, PasswordChange, PasswordChangeDone, PasswordResetView, PasswordResetDone, \
    Logout, \
    ProfileView, ProfileChangeView, CreateLocationsView, LocationsView

urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path("login/", Login.as_view(), name="login"),
    path("password_change/", PasswordChange.as_view(), name="password_change"),
    path("password_change/done/", PasswordChangeDone.as_view(), name="password_change_done"),
    path("password_reset/", PasswordResetView.as_view(), name="password_reset"),
    path("password_reset/done/", PasswordResetDone.as_view(), name="password_reset_done"),
    path("", Logout.as_view(), name="logout"),
    path("profile/<int:pk>", ProfileView.as_view(), name="profile"),
    path("profile_change/<int:pk>", ProfileChangeView.as_view(), name="profile_change"),
    # path("start_page/", LocationsView.as_view(), name="start_page"),
    path("create_location/", CreateLocationsView.as_view(), name="create_location"),
]
