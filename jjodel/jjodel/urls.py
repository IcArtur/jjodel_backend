"""Define urls for jjodel app."""
from django.contrib import admin
from django.urls import re_path

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    re_path('auth/', obtain_auth_token),
    re_path('', admin.site.urls),
]
