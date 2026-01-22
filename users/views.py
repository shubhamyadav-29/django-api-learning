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
        

from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .models import UserProfile
from .serializers import UserProfileSerializer

class UserDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
        
        
 