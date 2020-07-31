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
    return redirect('/dashboard')



def createLinkPage(request):
    return  render(request, 'polls/createLink.html', {'username': User.objects.get(pk= request.session['user']) })
    

def saveLink(request):
    
    try:
        link = Link(user=User.objects.get(pk=request.session['user']), name=request.POST['nombre'], url=request.POST['http'], desciption=request.POST['description'])
        link.save()
        request.session['message'] = 'success'
    except:
        request.session['message'] = 'error'



    return redirect('/dashboard')

def dashboard(request):
    try:
        user_session = request.session['user']
    except :
        return redirect('/')
    #Consultar los datos del usuario 
    username = User.objects.get(pk=user_session)
    links = Link.objects.filter(user_id=user_session)

    context = {'username': username, 'links': links}
    print(username, links)
    return render(request, 'polls/dashboard.html', context)
    

def editLink(request, link_id):
    return HttpResponse('editar link')

def deleteLink(request, link_id):
    link = Link.objects.get(pk=link_id)
    link.delete()

    return redirect('/dashboard')