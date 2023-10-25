from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Fingerprint


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ("username", "email", "phone_number", "profile_picture")


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = User
        fields = ("username", "email", "phone_number", "profile_picture")


class FingerprintForm(forms.ModelForm):
    class Meta:
        model = Fingerprint
        fields = ("fingerprint_data",)
