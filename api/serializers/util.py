def get_user_data(user):
    if not user:
        return None

    data = {
        'name': user.name,
        'username': user.username,
    }
    return data

def get_member_data(member):
    if not member:
        return None

    data = {
        'name': member.name,
        'army_no': member.army_no,
        'prefix': get_prefix_data(member.army_prefix),
        'rank':get_rank_type_data(member.rank),
        'course': member.course,
        'parent_unit': member.parent_unit,
        'unit_comd': member.unit_comd,
        'created_by_data':get_user_data(member.created_by)
    }
    return data



def get_organization_data(organization):
    if not organization:
        return None

    data = {
        'id': organization.id,
        'name': organization.name,
    }
    return data


def get_role_data(role):
    if not role:
        return None

    data = {
        'id': role.id,
        'name': role.name,
        'code_name': role.code_name
    }
    return data


def get_prefix_data(prefix):
    if not prefix:
        return None

    data = {
        'id': prefix.id,
        'name': prefix.name,
    }
    return data


def get_rank_type_data(rank_type):
    if not rank_type:
        return None

    data = {
        'id': rank_type.id,
        'name': rank_type.name,
        'category': rank_type.category,
    }
    return data
