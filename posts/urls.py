# from django.urls import path
from rest_framework.routers import DefaultRouter

from posts import views
from posts.apps import PostsConfig

app_name = PostsConfig.name

router = DefaultRouter()
router.register(prefix=r'posts', viewset=views.PostViewSet, basename='post')
router.register(prefix=r'(?P<post_id>\d+)/comments', viewset=views.CommentViewSet, basename='comment')

urlpatterns = router.urls
