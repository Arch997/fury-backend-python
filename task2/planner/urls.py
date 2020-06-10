# -*- coding: utf-8 -*-

from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('events/', views.events, name='events'),
    path('events/<int:event_id>/', views.event, name='event'),
    path('add_event/', views.add, name='add_event'),
    path('edit_event/<int:event_id>/', views.edit, name='edit_event'),
    path('events/<int:event_id>/delete', views.delete, name='delete_event'),

    ]
