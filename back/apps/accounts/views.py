from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from .serializer import UserSerializer,UserRegisterSerializer
from .models import User
# Create your views here.

#NOTES :
# - maybe i will send tokens in an HttpOnlyCookie later 


class UserView(APIView) :
    permission_classes = [AllowAny]

    def get(self,request) :
        users= User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class RegisterView(APIView) :
    permission_classes = [AllowAny]

    def post(self,request) :
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

class LoginView(APIView) :
    permission_classes = [AllowAny]

    def post(self,request) :
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(username=email ,password=password)

        if user :
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "access" : str(refresh.access_token),
                    "refresh" : str(refresh)
                },
                status=status.HTTP_202_ACCEPTED
            )
        return Response({"message" : "invalid credentials "}, status=status.HTTP_400_BAD_REQUEST)
        

