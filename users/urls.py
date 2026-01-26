from django.urls import path
from .views import UserListCreateAPIView, UserDetailAPIView ,LoginAPIView


urlpatterns = [
    path('login/', LoginAPIView.as_view()),
    path('users/', UserListCreateAPIView.as_view()),
    path('users/<int:pk>/', UserDetailAPIView.as_view()),
]
