from django.contrib.auth import authenticate
from rest_framework import serializers
from api.util import ldap_authenticate
from api.models import User


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255, required=True)
    password = serializers.CharField(max_length=255, required=True)

    def validate(self, attrs):
        username = attrs.get('username', None)
        password = attrs.get("password", None)

        if not username or not password:
            raise serializers.ValidationError({'msg': 'Invalid data.'})

        if username != "superuser":
            if not ldap_authenticate(username=username, password=password):
                raise serializers.ValidationError({'msg': 'Invalid credentials.'})

            users = User.objects.filter(username=username, role__isnull=False).all()
            if len(users) == 0:
                raise serializers.ValidationError({'msg': 'User does not exists or has no role assigned'})

        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError({'msg': 'Invalid credentials.'})

        attrs['user'] = user
        return attrs
