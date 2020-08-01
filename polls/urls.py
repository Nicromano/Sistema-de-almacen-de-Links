# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 21:52:59 2020

@author: NICROMANO
"""

from django.urls import path
from . import views


app_name = 'polls'
urlpatterns = [
    #Url inicial
    path('', views.index, name='index'),
    #url GET para crear el link: Muestra un formulario
    path('createLink/', views.createLinkPage, name="createLink"),
    #Url POST para agregar el link: Almacena los datos
    path('saveLink/', views.saveLink, name="saveLink"),
    #Url POST para editar el link: Envia datos para actualizar
    path('editLink/', views.editLink, name="editLink"),
    #Ural GET para editar el link: Presenta formulario para editar el link
    path('editLink/<int:link_id>', views.editLinkPage),
    #Url POST elimina un link
    path('deleteLink/<int:link_id>', views.deleteLink),
    #Url presenta el home, donde se visualizan todos los links 
    path('dashboard/', views.dashboard, name="dashboard"),
    #Url login para enviar los datos a guardar 
    path('login/', views.login, name="login"),
    #Elimina las variables de sesione y cierra sessión
    path('logout/', views.logout, name="logout"),
    
    

]