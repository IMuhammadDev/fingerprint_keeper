from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.UserListView.as_view(), name="user-list"),
    path("users/<int:pk>/", views.UserDetailView.as_view(), name="user-detail"),
    path("fingerprints/", views.FingerprintListView.as_view(), name="fingerprint-list"),
    path(
        "fingerprints/<int:pk>/",
        views.FingerprintDetailView.as_view(),
        name="fingerprint-detail",
    ),
]
