import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tms.settings')

import django

django.setup()

from api.models import Permission

permissions = [

    Permission(name='Create User', code_name='create_user', module_name='User', description='User can create user'),
    Permission(name='Read User', code_name='read_user', module_name='User', description='User can read user'),
    Permission(name='Update User', code_name='update_user', module_name='User', description='User can update user'),
    Permission(name='Show User', code_name='show_user', module_name='User', description='User can view user'),
    Permission(name='Read Organization', code_name='read_organization', module_name='Organization',
               description='User can read organization'),
    Permission(name='Show Organization', code_name='show_organization', module_name='Organization',
               description='User can show organization'),
    Permission(name='Create Role', code_name='create_role', module_name='Role', description='User can create role'),
    Permission(name='Read Role', code_name='read_role', module_name='Role', description='User can read role'),
    Permission(name='Update Role', code_name='update_role', module_name='Role', description='User can update role'),
    Permission(name='Delete Role', code_name='delete_role', module_name='Role', description='User can delete role'),
    Permission(name='Show Role', code_name='show_role', module_name='Role', description='User can view role'),

    Permission(name='Show Officer Property', code_name='show_officer_property', module_name='Officer_Property',
               description='User can view Officer Property'),
    Permission(name='Create Officer Property', code_name='create_officer_property', module_name='Officer_Property',
               description='User can view Officer Property'),
    Permission(name='Read Officer Property', code_name='read_officer_property', module_name='Officer_Property',
               description='User can view Officer Property'),
    Permission(name='Update Officer Property', code_name='update_officer_property', module_name='Officer_Property',
               description='User can view Officer Property'),
    Permission(name='Delete Officer Property', code_name='delete_officer_property', module_name='Officer_Property',
               description='User can view Officer Property'),

    Permission(name='Show Officer Maintenance', code_name='show_officer_maintenance', module_name='Officer_maintenance',
               description='User can view Officer maintenance'),
    Permission(name='Create Officer Maintenance', code_name='create_officer_maintenance',
               module_name='Officer_Maintenance',
               description='User can view Officer maintenance'),
    Permission(name='Read Officer Maintenance', code_name='read_officer_maintenance', module_name='Officer_Maintenance',
               description='User can view Officer maintenance'),
    Permission(name='Update Officer Maintenance', code_name='update_officer_maintenance',
               module_name='Officer_Maintenance',
               description='User can view Officer maintenance'),
    Permission(name='Delete Officer Maintenance', code_name='delete_officer_maintenance',
               module_name='Officer_Maintenance',
               description='User can view Officer maintenance'),

]


def add_permission():
    for permission in permissions:
        try:
            Permission.objects.get(code_name=permission.code_name)
        except Permission.DoesNotExist:
            permission.save()


if __name__ == '__main__':
    print("Adding permissions to TMS...")
    add_permission()
