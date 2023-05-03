from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserSerializer, ProfileSerializer, MyTokenObtainPairSerializer


class SignUpView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer


class GoogleLoginView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class EmailLoginView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

