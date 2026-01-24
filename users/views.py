from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if not user:
            return Response(
                {"error": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        token, _ = Token.objects.get_or_create(user=user)

        return Response(
            {"token": token.key},
            status=status.HTTP_200_OK
        )
























# from django.shortcuts import get_object_or_404
# from rest_framework.views import APIView 
# from rest_framework.response import Response
# from rest_framework import status
# from .models import UserProfile
# from .serializers import UserProfileSerializer

# class UserDetailAPIView(APIView):
#     def get(self , request,pk):
#         user = get_object_or_404(UserProfile,pk=pk)
#         serializer = UserProfileSerializer(user)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
    
#     def put(self, request, pk):
#         user = get_object_or_404(UserProfile,pk=pk)
#         serializer = UserProfileSerializer(user,data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 serializer.data,
#                 status=status.HTTP_200_OK
#             )
            
            
#         return Response(
#             serializer.errors,
#             status=status.HTTP_400_BAD_REQUEST
#         )
        
#     def delete(self ,request, pk):
#         user = get_object_or_404(UserProfile, pk=pk)
#         user.delete()
#         return Response(
#             {"message": "User deleted successfully"},
#             status=status.HTTP_204_NO_CONTENT
#         )
        

# from rest_framework import generics
# from .models import UserProfile
# from .serializers import UserProfileSerializer

# class UserListCreateAPIView(generics.ListCreateAPIView):
#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileSerializer


# class UserDetailAPIView(generics.RetrieveDestroyAPIView):
#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileSerializer
 