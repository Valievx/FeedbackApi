from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.utils.crypto import get_random_string
from rest_framework import filters, viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User
from users.permissions import IsAdmin
from users.serializers import (
    MeUserSerializer,
    PostUserSerializer,
    UserSerializer,
    TokenSerializer,
    SignUpSerializer
)


class SignUpViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer

    @action(methods=['post'], detail=False, permission_classes=[AllowAny])
    def signup(self, request):
        serializer = SignUpSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data['email']
            username = serializer.validated_data['username']

            if not User.objects.filter(username=username, email=email).exists():
                user = User.objects.create(username=username, email=email)
            else:
                user = User.objects.get(username=username)

            confirmation_code = get_random_string(6)
            user.confirmation_code = confirmation_code
            user.save()
            send_mail(
                'Код подтверждения регистрации',
                f'Ваш код подтверждения: {confirmation_code}',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'head', 'options', 'patch', 'delete']
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]
    filter_backends = [filters.SearchFilter]
    lookup_field = 'username'
    search_fields = ('username',)

    def get_serializer_class(self):
        if self.action == 'create':
            return PostUserSerializer
        return UserSerializer

    @action(
        methods=['get', 'patch'],
        detail=False,
        permission_classes=[IsAuthenticated]
    )
    def me(self, request):
        user = get_object_or_404(User, username=self.request.user)
        serializer = MeUserSerializer(user)
        if request.method == 'PATCH':
            serializer = MeUserSerializer(
                user,
                data=request.data,
                partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class TokenView(TokenObtainPairView):
    def post(self, request):
        serializer = TokenSerializer(data=request.data)
        if serializer.is_valid():
            confirmation_code = serializer.validated_data['confirmation_code']
            username = serializer.validated_data['username']
            user = get_object_or_404(User, username=username)

            if user.confirmation_code == confirmation_code:
                token = RefreshToken.for_user(user)
                return Response(
                    {"token": str(token.access_token)},
                    status=status.HTTP_200_OK
                )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
