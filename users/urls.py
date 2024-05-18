from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from users import views
from users.apps import UsersConfig


app_name = UsersConfig.name


urlpatterns = [
    path('register/', views.UserRegister.as_view(), name='register'),
    path('', views.UserList.as_view(), name='user-list'),
    path('<int:pk>/', views.UserRetrieve.as_view(), name='user-retrieve'),
    path('<int:pk>/update/', views.UserUpdate.as_view(), name='user-update'),
    path('<int:pk>/delete/', views.UserDelete.as_view(), name='user-delete'),

    path('token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]
