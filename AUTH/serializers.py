from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import AuthUser


class CreateUserSerializer(serializers.ModelSerializer):
    authtoken = serializers.SerializerMethodField()

    class Meta:
        model = AuthUser
        fields = ['email', 'password', 'authtoken']

    def get_authtoken(self, user):                        # for generating refresh and access token
        token = RefreshToken.for_user(user=user)

        return {
            'refresh': str(token),
            'access': str(token.access_token),
        }

    def create(self, validated_data):
        user = super(CreateUserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
