"""Define urls for jjodel app."""
from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('token/', obtain_auth_token, name='obtain_auth_token'),
    path('organization/<Group>/', include('jjodel.jjodel.routers.organization')),
]
