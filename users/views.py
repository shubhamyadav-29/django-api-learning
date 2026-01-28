from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from rest_framework.permissions import IsAuthenticated

from .models import UserProfile
from .serializers import UserProfileSerializer


class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]


class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]


class LoginAPIView(APIView):
    def post(self ,request):
        username = request.data.get("username")
        password = request.data.get("password")
        
        user = authenticate(username= username, password=password)
        
        if not user:
            return Response(
                {"error":"Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED
            )
            
        token,_ = Token.objects.get_or_create(user=user)
        
        return Response(
            {"token": token.key},
            status=status.HTTP_200_OK
        )
            
            