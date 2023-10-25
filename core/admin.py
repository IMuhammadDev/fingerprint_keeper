from django.contrib import admin
from .models import User, Fingerprint


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "phone_number"]


@admin.register(Fingerprint)
class FingerprintAdmin(admin.ModelAdmin):
    list_display = ["user", "created_at"]
    search_fields = ["user__username", "user__email"]
