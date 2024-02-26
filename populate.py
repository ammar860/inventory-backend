import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tms.settings')

import django

django.setup()

from api.models import User, Role, Permission


def populate():
    create__user()
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

def create__user():
    try:
        role = Role.objects.create(name='Admin', code_name='admin')
    except Role.DoesNotExist:
        role = Role.objects.create(name='Admin', code_name='admin')
        role.save()

    try:
        user = User.objects.get(username='ammar')
    except User.DoesNotExist:
        user = User.objects.create_superuser(
            id=2,
            username="ammar",
            password="123",
        )
        user.role = role
        user.save()

if __name__ == '__main__':
    print("Populating TMS...")
    populate()
