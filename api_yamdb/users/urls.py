from django.urls import include, path
from rest_framework import routers, permissions
from rest_framework_simplejwt.views import TokenObtainPairView

from users.views import SignUpViewSet, UserViewSet, TokenView


router = routers.DefaultRouter()
router.register(r'auth', SignUpViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path(
        'auth/token/',
        TokenView.as_view(), name='token_obtain_pair'
    ),
    path('', include(router.urls)),
]
