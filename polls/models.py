from django.db import models

# Create your models here.


class User(models.Model):
    
    username = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username
    
    
class Link(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    desciption = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
    
    