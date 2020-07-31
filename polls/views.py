#from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Link
from django.urls import reverse


def index(request):

    try:
        request.session['user']
        return redirect('/dashboard')
    except :
        return render(request, 'polls/login.html')
    
def logout(request):
    del request.session['user']
    return redirect('/')
def login(request):
    username_post = request.POST['username']
    id = User.objects.filter(username = username_post).values_list('id', flat=True)
    if len(id) == 0:
        #No existe usuario
        user = User(username=username_post)
        user.save()
        id = user.id
    else:
        id = id[0]

    request.session['user'] = id
    print(request.session['user'])
    #return HttpResponseRedirect(reverse('polls:dashboard', args=(id,)))
    return redirect('/dashboard')
#


def createLink(request):
    username = request.POST['username']
    return  render(request, 'polls/dashborad')
    

def dashboard(request):
    
    return HttpResponse(request.session['user'])

def editLink(request, link_id):
    return HttpResponse('editar link')
