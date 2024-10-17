from django.shortcuts import render

from rest_framework_simplejwt.views import TokenObtainPairView # type: ignore
from rest_framework import generics # type: ignore
from rest_framework.permissions import AllowAny # type: ignore

from userauths.models import User, Profile
from userauths.serializer import RegisterSerializer, UserSerializer, ProfileSerializer, MyTokenObtainPairSerializer

# Create your views here.

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryblast = User.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = RegisterSerializer