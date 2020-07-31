# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 21:52:59 2020

@author: NICROMANO
"""

from django.urls import path

from  . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('createLink/', views.createLink, name="createLink"),
    path('editLink/<int:link_id>', views.editLink),
    path('dashboard/<int:user_id>', views.dashboard, name="dashboard"),
    path('addUser/', views.addUser, name="addUser"),
]