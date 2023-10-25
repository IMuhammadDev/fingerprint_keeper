from rest_framework import serializers
from .models import User, Fingerprint


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "phone_number", "profile_picture"]


class FingerprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fingerprint
        fields = ["id", "user", "fingerprint_data", "created_at"]
