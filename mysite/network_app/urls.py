from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import (
    RegisterView, LoginView, LogoutView, UserProfileListAPIView, PostViewSet, CommentViewSet,
    CommentLikeViewSet, SavePostViewSet, SavePostItemViewSet, StoryViewSet, HashtagViewSet
)

router = SimpleRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'comment-likes', CommentLikeViewSet, basename='comment-like')
router.register(r'save_posts', SavePostViewSet, basename='save_post')
router.register(r'save_post-items', SavePostItemViewSet, basename='save_post_item')
router.register(r'stories', StoryViewSet, basename='story')
router.register(r'hashtags', HashtagViewSet, basename='hashtag')

urlpatterns = [
    path('user_list/', UserProfileListAPIView.as_view(), name='user_list'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include(router.urls)),
]