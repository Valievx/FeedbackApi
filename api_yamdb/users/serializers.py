import re

from rest_framework import serializers
from users.models import User


class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=254, required=True)
    username = serializers.CharField(max_length=150, required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

    def validate_username(self, username):
        pattern = r'^[\w.@+-]+$'
        if not re.match(pattern, username) or username == 'me':
            raise serializers.ValidationError('Недопустимый username.')
        return username

    def validate(self, attrs):
        email = attrs['email']
        username = attrs['username']

        if (
            User.objects.filter(email=email).exists()
            or User.objects.filter(username=username).exists()
        ):
            if not User.objects.filter(username=username, email=email).exists():
                raise serializers.ValidationError('Недопустимый email.')

        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role'
        )


class MeUserSerializer(UserSerializer):
    role = serializers.CharField(read_only=True)


class PostUserSerializer(UserSerializer):
    email = serializers.EmailField(max_length=254, required=True)

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Такой email уже есть.')
        return email


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    confirmation_code = serializers.CharField(max_length=10)
