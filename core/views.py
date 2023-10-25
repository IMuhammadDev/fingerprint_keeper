from rest_framework import generics
from .models import User, Fingerprint
from .serializers import UserSerializer, FingerprintSerializer


class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FingerprintListView(generics.ListCreateAPIView):
    queryset = Fingerprint.objects.all()
    serializer_class = FingerprintSerializer


class FingerprintDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fingerprint.objects.all()
    serializer_class = FingerprintSerializer
