from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from backend_api.api.serializers import ApiTokenObtainPairSerializer, RegisterSerializer


class ApiTokenObtainPairView(TokenObtainPairView):
    serializer_class = ApiTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
