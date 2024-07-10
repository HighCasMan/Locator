from django.contrib.auth.backends import BaseBackend

from users.models import User


class EmailAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        kwargs = {'email': username}
        try:
            user = User.objects.get(**kwargs)
            if user.check_password(password):
                return user
            else:
                return None
        except User.DoesNotExist:       #?
            return None
