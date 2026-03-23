from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RegisterView, LoginView, LogoutView, UserProfileViewSet, PostViewSet, CommentViewSet,
    CommentLikeViewSet, SavePostViewSet, SavePostItemViewSet, StoryViewSet, HashtagViewSet
)

router = DefaultRouter()
router.register(r'users', UserProfileViewSet, basename='user')
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'comment-likes', CommentLikeViewSet, basename='comment-like')
router.register(r'saveposts', SavePostViewSet, basename='savepost')
router.register(r'savepost-items', SavePostItemViewSet, basename='savepostitem')
router.register(r'stories', StoryViewSet, basename='story')
router.register(r'hashtags', HashtagViewSet, basename='hashtag')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include(router.urls)),
]