from django.urls import path
from .views import  UserListAPIView

urlpatterns = [
    # path('users/', UserListAPIView.as_view()),
    path('users/<int:pk>/', UserListAPIView.as_view()),
]