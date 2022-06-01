from django.shortcuts import render,redirect


from django.db import connection
from django.views.generic import CreateView, DeleteView, ListView , UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout

from .models import *
from .forms import EditProfile, SolicitudServicioForm, UpdateSolicitudServicioT, registroform

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
    productos = Producto.objects.all().order_by('nombre')
    context = {
        'item':productos
    }
    return render(request,'home.html', context)
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
                else:
                    print(form.errors)
            if request.POST.get('submit') == 'sign_in':
                username = request.POST.get('username')
                password = request.POST.get('password')
                print(username, password)
                user = authenticate(request,username=username,password=password)
                if user is not None:
                    login(request,user)
                    return redirect('home')
                else :
                    print(user)
    context = {
        'form': form
    }
    return render(request, 'login.html', context)

def itemP(request,id):
    producto = Producto.objects.get(id = id)
    context = {
        'producto':producto
    }
    return render(request, 'item.html', context)

def perfil(request):
    usuario = request.user
    form = EditProfile(instance=usuario)
    context = {
        'form':form
    }
    if request.method == 'POST':
        form = EditProfile(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
    return render(request,'perfil.html', context)
def facturas(request):
    user = myUser.objects.get(rut = request.user.rut)
    compras = WebFactura.objects.filter(rut_cliente = user)
    context={
        'list': compras
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
            solicituds.id_cli = myUser.objects.get(id= usuario.id)
            solicituds.save() 
            #form.save()
            return redirect('home')
    return render(request,'sds.html', context)

def solicitudesS(request):
    user = myUser.objects.get(id = request.user.id)
    solicitudes = WebSolicitudServicio.objects.all().order_by('fecha_visita_solicitada')
    solicitudescli = WebSolicitudServicio.objects.filter(id_cli = user)
    context = {
        'solicitudes':solicitudes,
        'solicitudescli': solicitudescli
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

    