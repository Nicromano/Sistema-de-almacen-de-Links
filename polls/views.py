#from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Link
from django.urls import reverse

def index(request):
    return render(request, 'polls/form_init.html')
    

def addUser(request):
    username_post = request.POST['username']
    id = 0

    id = User.objects.filter(username = username_post).values_list('id', flat=True)
    if len(id) == 0:
        #No existe usuario
        user = User(username=username_post)
        user.save()
        id = user.id
    else:
        id = id[0]
    
    return HttpResponseRedirect(reverse('polls:dashboard', args=(id,)))


def createLink(request):
    username = request.POST['username']
    return  render(request, 'polls/dashborad')
    

def dashboard(request, user_id):
    print(user_id)
    return HttpResponse('ver links')

def editLink(request, link_id):
    return HttpResponse('editar link')
