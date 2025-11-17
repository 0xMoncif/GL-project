from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from .serializer import UserSerializer,UserRegisterSerializer
from .models import User
# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny]) 
def register(request) :
    serializer = UserRegisterSerializer(data=request.data)
    if serializer.is_valid() :
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "access" : str(refresh.access_token),
                "refresh" : str(refresh)
            },
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny]) 
def get_users(request) :
    users= User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

