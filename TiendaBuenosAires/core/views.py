from django.shortcuts import render,redirect


from django.db import connection
from django.views.generic import CreateView, DeleteView, ListView , UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout

from .models import *
from .forms import EditProfile, SolicitudServicioForm, UpdateSolicitudServicioT, registroform
""" from transbank.error.transbank_error import TransbankError
from transbank.webpay.webpay_plus.transaction import Transaction """
"""import random"""
# Create your views here.
def logout_view(request):
    logout(request)
    return redirect('login')

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
def registerpage(request):
    form = registroform()
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            if request.POST.get('submit') == 'sign_up':
                form = registroform(request.POST)
                if form.is_valid():
                    user = form.save()
                    user.save()
                    raw_password = form.cleaned_data.get('password1')
                    user = authenticate(username = user.username, password = raw_password)
                    login(request, user)
                    return redirect('home')
            if request.POST.get('submit') == 'sign_in':
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request, username= username, password = password)
                if user is not None:
                    login(request,user)
                    return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'login.html', context)

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
    solicitudes = WebSolicitudServicio.objects.all().order_by('fecha_visita_solicitada')
    context = {
        'solicitudes':solicitudes,
    }
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