from django.contrib import admin

from .models import Link, User
# Register your models here.
#Registro del modelo Link
admin.site.register(Link)
#registro del modelo User
admin.site.register(User)
