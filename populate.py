import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tms.settings')

import django

django.setup()

from api.models import User, Role, Permission


def populate():
    permissions = Permission.objects.all()

    try:
        role = Role.objects.get(code_name='su')
        role.permissions.clear()
    except Role.DoesNotExist:
        role = Role.objects.create(name='SuperUser', code_name='su')

    role.permissions.add(*permissions)
    role.save()

    try:
        user = User.objects.get(username='superuser')
    except User.DoesNotExist:
        user = User.objects.create_superuser(
            id=1,
            username="superuser",
            password="123",
        )
        user.role = Role.objects.get(code_name='su')
        user.save()


if __name__ == '__main__':
    print("Populating TMS...")
    populate()
