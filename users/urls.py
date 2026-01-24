# from django.urls import path
# from .views import  UserListCreateAPIView , UserDetailAPIView

# urlpatterns = [
#     path('users/', UserListCreateAPIView.as_view()),
#     path('users/<int:pk>/', UserDetailAPIView.as_view()),
# ]


from django.urls import path
from .views import LoginAPIView

urlpatterns = [
    path('login/', LoginAPIView.as_view()),
    path('users/', UserListCreateAPIView.as_view()),
    path('users/<int:pk>/', UserDetailAPIView.as_view()),
]
