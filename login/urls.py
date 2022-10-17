from django.contrib.auth import views as auth_views
from django.urls import path
from login.views import *

urlpatterns = [
    path('login/', logar, name='login'),
    path('logout/', sair, name='logout')
]
