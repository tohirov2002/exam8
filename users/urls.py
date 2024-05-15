from django.urls import path
from rest_framework import routers

from users.views import (
    RegisterAPIView,
    password_change_view,
    password_reset_view
)

router = routers.DefaultRouter()

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name="register"),
    path('password-change/', password_change_view, name="password-change"),
    path('password-reset/', password_reset_view, name="password-reset"),
] + router.urls
