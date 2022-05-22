from django.shortcuts import render
from .forms import EditProfile
# Create your views here.
def home(request):
    return render(request,'home.html')
def login(request):
    return render(request,'login.html')

def itemP(request):
    return render(request, 'item.html')

def perfil(request):
    form = EditProfile()
    usuario = {
        "nombre": "John",
        "apellido": "Doe"
    }

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
    return render(request, 'facturas.html')
def sds(request):
    return render(request,'sds.html')