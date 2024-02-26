from django.middleware import csrf
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from api.util import set_access_cookies, set_refresh_cookies, get_tokens_for_user, combine_role_permissions
from api.models import OfficerProperty, SoldierProperty, NonResidentialProperty


class DashboardView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        officers = get_officers_list()
        soldiers = get_soldiers_list()
        non_residential = get_non_residential_list()

        moq_count = officers.filter(type__exact=OfficerProperty.PROPERTY_MOQ).count()
        flat_count = officers.filter(type__exact=OfficerProperty.PROPERTY_FLAT).count()
        house_count = officers.filter(type__exact=OfficerProperty.PROPERTY_HOUSE).count()

        jco_count = soldiers.filter(type__exact=SoldierProperty.PROPERTY_JCO).count()
        soldiers_count = soldiers.filter(type__exact=SoldierProperty.PROPERTY_SOLDIER).count()
        nco_count = soldiers.filter(type__exact=SoldierProperty.PROPERTY_NCsE).count()

        sm_barak_count = non_residential.filter(type__exact=NonResidentialProperty.PROPERTY_SM_BARAK).count()
        mt_shed_count = non_residential.filter(type__exact=NonResidentialProperty.PROPERTY_MT_SHED).count()
        park_futsal_count = non_residential.filter(type__exact=NonResidentialProperty.PROPERTY_PARK_FUTSAL).count()

        officers_obj = {
            'total': officers.count(),
            'labels': ['MOQ', 'FLAT', 'HOUSE'],
            'series': [moq_count, flat_count, house_count]
        }

        soldiers_obj = {
            'total': soldiers.count(),
            'labels': ['JCO', 'Soldiers', 'NCsE'],
            'series': [jco_count, soldiers_count, nco_count]
        }
        non_residential_obj = {
            'total': non_residential.count(),
            'labels': ['SM Barak', 'MT Shed', 'Park & Futsul'],
            'series': [sm_barak_count, mt_shed_count, park_futsal_count]
        }

        data = {
            'officers_obj': officers_obj,
            'soldiers_obj': soldiers_obj,
            'non_residential_obj': non_residential_obj
        }

        response = Response()
        response.status_code = status.HTTP_200_OK
        response.data = {"msg": "Login successfully", "data": data}

        return response


def get_officers_list():
    officers = OfficerProperty.objects.all()
    return officers


def get_soldiers_list():
    soldiers = SoldierProperty.objects.all()
    return soldiers


def get_non_residential_list():
    non_residential = NonResidentialProperty.objects.all()
    return non_residential
