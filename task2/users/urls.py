# -*- coding: utf-8 -*-

from django.urls import path
from django.contrib.auth.views import LoginView

from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'),
         name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('todos/', views.todos, name='todos'),

    ]
