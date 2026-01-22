from django.urls import path
from .views import  UserDetailAPIView

urlpatterns = [
    path('users/', UserDetailAPIView.as_view()),
    path('users/<int:pk>/', UserDetailAPIView.as_view()),
]