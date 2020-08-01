#from django.shortcuts import render
# Create your views here.

from django.shortcuts import render, redirect
from .models import User, Link
from timeago import format
import datetime


# función de ruta inicial
def index(request):

    try:  # Excepción por si no existe un usuario registrado
        request.session['user']  # Variable de sessión almacenada
        return redirect('/dashboard')  # Redirigue a la página /dashboard
    except:
        # Renderia el archivo login.html existente en templates/polls
        return render(request, 'polls/login.html')


def logout(request):
    try:  # Excepción por si no existe un usuario registrado
        del request.session['user']  # Elimina la variable de sesión
    except:
        return redirect('/')  # Redirigue a la vista prinpal (def index)
    return redirect('/')  # Redirigue a la vista prinpal (def index)

# función que llama el formualrio de login.html


def login(request):
    try:
        # Variable recuperada del formulario
        username_post = request.POST['username']
        # Obtiene una lista de id que existen con la variable recuperada, Mayúsculas y minúsculas por igual
        id = User.objects.filter(
            username__iexact=username_post).values_list('id', flat=True)
        # Si no existe ningun id retornado
        if len(id) == 0:
            # Es decir, No existe usuario
            # Se crea el usuario llamado al modelo User
            user = User(username=username_post)
            user.save()  # Se almacena el valor dado en el usar
            id = user.id  # Se obtiene el id usuario antes agregado
        else:
            # Si existe el usuario, se inicia sessión con ese usuario
            id = id[0]  # Devuelve el id de ese único usuario
        # Almacena el id en una variable de sesión
        request.session['user'] = id
        return redirect('/dashboard')  # Se redirigue hacia el dashboard
    except:  # Si existe algún problema
        return redirect('/')  # S redirigue a la vista principal

# Vista del formulario createLink


def createLinkPage(request):
    # Retorna el template cretateLink.html almacenado en el directorio Templates/polls pasando valor la variable de la sesión almacenada previamente
    return render(request, 'polls/createLink.html', {'username': User.objects.get(pk=request.session['user'])})


def saveLink(request):
    try:  # Excepción por si no existen variables de sesión almacenadas
        # Creación del objeto Link, pasando los datos al constructor del mismo
        link = Link(user=User.objects.get(
            pk=request.session['user']), name=request.POST['nombre'], url=request.POST['http'], desciption=request.POST['description'])
        link.save()  # Almacenamos los datos del modelo
        # Variable de sesión para alerta: Proceso correcto
        request.session['message'] = 'success'
    except:
        # Variable de sesión para alerta: Proceso incorrecto
        request.session['message'] = 'error'

    return redirect('/dashboard')  # Redirigue al /dashboard

# Función que renderiza la página de las visualización de los links


def dashboard(request):
    try:
        # Revisa si existe variable de usaurio
        user_session = request.session['user']
    except:  # Si no existe crea una excepción
        return redirect('/')  # Se redirigue a la vista principal(Login)
    # Consultar los datos del usuario
    # Obtiene los datos de un usuario dada su clave primaria (pk)
    username = User.objects.get(pk=user_session)
    # Filtra todos los link del usuario anterior
    links = Link.objects.filter(user_id=user_session)
    try:
        # Recupera la variable de sesión por si hay algún mensaje
        message = request.session['message']
        del request.session['message']  # Elimina la variable de sesión
    except:  # Si existe algún problema
        message = None  # El mensaje es nulo
    context = {'username': username, 'links': links, 'message': message}  # Contexto para renderizar
    # renderiza el archivo dashboard.html con datos almacenados en el context
    return render(request, 'polls/dashboard.html', context)


# Función que actualiza los datos del link
def editLink(request):
    try:  # Excepción por si existe variables de sessión almacenadas
        request.session['user']  # Id de usuario almacenado
        id_link = request.session['id_link']  # id link almacenado
    except:  # Si hubo algún problema
        return redirect('/')  # Se redirigue hacía la vista principal
    # Se elimina la variable de sessión almancenada
    del request.session['id_link']
    try:  # Excepción por si existe problema al editar el link
        # Obtiene los datos del link con clave primaria
        link = Link.objects.get(pk=id_link)
        link.name = request.POST['name']  # actualiza el campo field
        link.url = request.POST['http']  # actualiza el campo url
        # actualiza el campo description
        link.desciption = request.POST['description']
        link.save()  # guarda los datos cambiados
        # variable de usuario: proceso exitoso
        request.session['message'] = 'success'
    except Exception:
        # variable de usuario: proceso erróneo
        request.session['message'] = 'error'
    return redirect('/dashboard')  # redirigue el dashboard


def editLinkPage(request, link_id):
    try:  # Excepción por no existe variable de sesión almacenada
        request.session['user']  # variable de sesión: id del usuario
    except:  # Si hubo algún problema
        return redirect('/')  # Se redirigue a la vista principal
    try:
        links = Link.objects.get(pk=link_id)  # obtiene los datos del link
        # almacena el id del link en una variable de sesión
        request.session['id_link'] = link_id
        # crea un diccionario con los datos del link
        link = {'name': links.name, 'url': links.url,
                'desciption': links.desciption}
        # renderiza la vista editLink.html con los datos del link
        return render(request, 'polls/editLink.html', {'link': link, 'username': User.objects.get(pk=request.session['user'])})
    except:  # si hubo un problema
        request.session['message'] = 'error' #alamacena un variable de sesión si hubo un error
        return redirect('/dashboard')#se redirigue hacia el dashboard

#Función para eliminar el link
def deleteLink(request, link_id):
    try:#Excepción por si no existe variables de sesión
        request.session['user'] #variable de sesión: id de usuario
    except:#Si hubo un problema
        return redirect('/') #Se redirigue hacia la vista principal(login)
    try:
        link = Link.objects.get(pk=link_id) #Obtiene los datos de un link en función de su clave primaria (pk)
        link.delete()#Eliminar el objeto existente en los datos 
        request.session['message'] = 'success'#Variable de sesión para el mensaje de exito
    except:#Si huubo un error 
        request.session['message'] = 'error' #Variable de sesión para el mensaje de error 
    return redirect('/dashboard')#Se redirigue al dashboard
