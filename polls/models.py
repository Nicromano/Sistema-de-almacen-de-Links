from django.db import models

# Create your models here.


#Modelo User, salida en DB polls_user
class User(models.Model):
    
    #Campo nombre del usuario
    username = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username
    
    
#Modelo Link, salida en DB polls_link
class Link(models.Model):
    #Clave foranea hacia el modelo User
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #Campo nombre del Link 
    name = models.CharField(max_length=100)
    #Campo url del link
    url = models.URLField(max_length=200)
    #Descripción breve del link
    desciption = models.CharField(max_length=250)
    #TimeStamp del link 
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
    
    