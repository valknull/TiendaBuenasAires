from django.shortcuts import render
from .forms import EditProfile
from django.db import connection
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
# Create your views here.

""" class ModelCreateView(CreateView):
    model = Model
    template_name = ".html" """


def listar_productos():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    cursor.callproc("SP_OBTENER_STOCK_ACTUAL",[out_cur])
    lista=[]
    for i in out_cur:
        lista.append(i)
    return lista

def home(request):
    return render(request,'home.html')
def login(request):
    return render(request,'login.html')

def itemP(request):
    return render(request, 'item.html')

def perfil(request):
    form = EditProfile()
    """ usuario = {
        "nombre": "John",
        "apellido": "Doe"
    } """

    context = {
        'form':form
    }
    if request.method == 'POST':
        form = EditProfile(request.POST)
        if form.is_valid():
            form.save()
        """nombre_cambio = request.body.get('Nombre_change')
        nombre_cambio = hola
        usuario.update({'nombre': nombre_cambio})"""
        
    return render(request,'perfil.html', context)
def facturas(request):
    print(listar_productos())
    context={
        'productos': listar_productos()
    }
    return render(request, 'facturas.html', context)
def sds(request):
    return render(request,'sds.html')

def solicitudesS(request):
    return render(request, 'SolicitudesS.html')