from django.contrib.auth.backends import BaseBackend
from api.models import User


class PasswordLessAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            if username == 'superuser':
                return None

            users = User.objects.filter(username=username, role__isnull=False).all()
            if len(users) == 0:
                return None

            return users[0]
        except User.DoesNotExist:
            return None
