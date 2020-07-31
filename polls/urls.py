# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 21:52:59 2020

@author: NICROMANO
"""

from django.urls import path
from . import views


app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('createLink/', views.createLinkPage, name="createLink"),
    path('saveLink/', views.saveLink, name="saveLink"),
    path('editLink/', views.editLink, name="editLink"),
    path('editLink/<int:link_id>', views.editLinkPage),
    path('deleteLink/<int:link_id>', views.deleteLink),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    
    

]