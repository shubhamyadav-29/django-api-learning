from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from .models import UserProfile
from .serializers import UserProfilSerializer

class UserListAPIView(APIView):
    def get(self , request):
        users = UserProfile.objects.all()
        serializer = UserProfilSerializer(users,many= True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
 