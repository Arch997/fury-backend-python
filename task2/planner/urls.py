# -*- coding: utf-8 -*-

from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('todos/', views.todos, name='todos'),
    path('todo/<int:todo_id>/', views.todo, name='todo'),
    path('events/', views.events, name='events'),
    path('events/<int:event_id>/', views.event, name='event'),
    path('add/<int:event_id>/', views.add, name='add_event'),

    ]
