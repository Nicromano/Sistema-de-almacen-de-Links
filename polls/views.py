#from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'polls/index.html')
    


def createLink(request):
    return  HttpResponse(request.POST['username'])
    

def viewLinks(request):
    return HttpResponse('ver links')

def editLink(request, link_id):
    return HttpResponse('editar link')
