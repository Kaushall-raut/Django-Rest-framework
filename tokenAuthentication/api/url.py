from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views


urlpatterns = [
    path('auth-token',obtain_auth_token),
    path("profile",views.user_profile),
    path("admin-profile",views.admin_profile),
]