from django.shortcuts import render

from rest_framework_simplejwt.views import TokenObtainPairView # type: ignore

from userauths.models import User, Profile
from userauths.serializer import RegisterSerializer, UserSerializer, ProfileSerializer, MyTokenObtainPairSerializer

# Create your views here.

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
