from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def login(request):
    return render(request,'login.html')

def itemP(request):
    return render(request, 'item.html')

def perfil(request):
    usuario = {
        "nombre": "John",
        "apellido": "Doe"
    }
    context = {
        'usuario':usuario
    }
    
    return render(request,'perfil.html', context)
def facturas(request):
    return render(request, 'facturas.html')
def sds(request):
    return render(request,'sds.html')