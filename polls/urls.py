# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 21:52:59 2020

@author: NICROMANO
"""

from django.urls import path

from  . import views


urlpatterns = [
    path('', views.index, name='index'),
]