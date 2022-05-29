from django.shortcuts import render,redirect


from django.db import connection
from django.views.generic import CreateView, DeleteView, ListView , UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import logout

from .models import *
from .forms import EditProfile, SolicitudServicioForm, UpdateSolicitudServicioT, registroform
# Create your views here.
def logout_view(request):
    logout(request)

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
class CrearSolicitudServicio(CreateView):
    model = WebSolicitudServicio
    form_class = SolicitudServicioForm
    template_name = 'sds.html'
    success_url = reverse_lazy('home')

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
    usuario = request.user
    form = SolicitudServicioForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = SolicitudServicioForm(request.POST)
        if form.is_valid():
            solicituds = form.save(commit=False)
            solicituds.rut_cli = myUser.objects.get(rut= usuario.rut)
            solicituds.save() 
            #form.save()
            return redirect('home')
    return render(request,'sds.html', context)

def solicitudesS(request):
    solicitudes = WebSolicitudServicio.objects.all().order_by('fecha_hora_visita_solicitada')
    form = UpdateSolicitudServicioT()
    context = {
        'solicitudes':solicitudes,
        'form': form
    }
    if request.method == 'POST':
        form = UpdateSolicitudServicioT(request.POST)
        if form.is_valid():
            form
    return render(request, 'SolicitudesS.html', context)
""" def sds(request):
    solicitudservicio = WebSolicitudServicio
    form = SolicitudServicioForm
    return render(request,'sds.html') """

def updatess(request,id):
    solicitud = WebSolicitudServicio.objects.get(numeross = id)
    if request.method == 'GET':
        form = UpdateSolicitudServicioT(instance = solicitud)
    else :
        form = UpdateSolicitudServicioT(request.POST, instance = solicitud)
        if form.is_valid():
            form.save()
            return redirect('solicitudes')
    context = {
        'form': form,
        'solicitud':solicitud
    }
    return render(request, 'updateSolicitud.html', context)