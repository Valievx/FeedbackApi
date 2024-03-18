from django.urls import include, path
from rest_framework import routers

from .views import (CategoryViewSet, GenreViewSet,
                    TitleViewSet, ReviewsViewSet,
                    CommentViewSet)

v1 = routers.DefaultRouter()
v1.register('categories', CategoryViewSet, basename='categories')
v1.register('genres', GenreViewSet, basename='genres')
v1.register('titles', TitleViewSet, basename='titles')
v1.register(r'titles/(?P<title_id>\d+)/reviews',
            ReviewsViewSet, basename='reviews')
v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments'
)

urlpatterns = [
    path('', include(v1.urls))
]
