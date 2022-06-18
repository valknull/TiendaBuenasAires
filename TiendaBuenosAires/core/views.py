from urllib import response
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.db import connection
from django.db.models import Min, Count
from django.views.generic import CreateView, DeleteView, ListView , UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt

from datetime import datetime,date
""" from transbank.error.transbank_error import TransbankError
from transbank.webpay.webpay_plus.transaction import Transaction """
from transbank.webpay.webpay_plus.transaction import Transaction, WebpayOptions
import random
import time
from .models import *
from .forms import EditProfile, SolicitudServicioForm, UpdateSolicitudServicioT, registroform

# Create your views here.

def logout_view(request):
    logout(request)
    return redirect('login')

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
    tecnicos = myUser.objects.filter(is_tecnico=True)
    dictionarie = {}
    tecnicos_numero_ss = tecnicos.prefetch_related('rut_tecnico').annotate(n_ss = models.Count('rut_tecnico__numeross'))

    for i in tecnicos_numero_ss:
        dictionarie[i.id] = i.n_ss
    print(dictionarie)
    minval = min(dictionarie.values())
    res = list(filter(lambda x: dictionarie[x]==minval, dictionarie))
    random_list_number = random.randrange(0,len(res))
    tecnico = res[random_list_number]
    print(tecnico)

    context = {
        'form': form
    }
    if request.method == 'POST':
        form = SolicitudServicioForm(request.POST)
        if form.is_valid():
            solicituds = form.save(commit=False)
            solicituds.id_cli = myUser.objects.get(id= usuario.id)
            solicituds.id_tec = myUser.objects.get(id = tecnico)
            solicituds.save() 
            #form.save()
            return redirect('home')
    return render(request,'sds.html', context)

def solicitudesS(request):
    user = myUser.objects.get(id = request.user.id)
    solicitudes = WebSolicitudServicio.objects.all().order_by('id_cli__first_name')
    solicitudescli = WebSolicitudServicio.objects.filter(id_cli = user)
    context = {
        'solicitudes':solicitudes,
        'solicitudescli': solicitudescli
    }
    return render(request, 'SolicitudesS.html', context)

def updateEstadoSS(request,id):
    solicitud = WebSolicitudServicio.objects.get(numeross = id)
    if solicitud.estado_ss == WebSolicitudServicio.EstadoDeServicio.Pendiente or solicitud.estado_ss == WebSolicitudServicio.EstadoDeServicio.NuevaFechaPropuesta:
        solicitud.estado_ss = WebSolicitudServicio.EstadoDeServicio.Aceptada
    elif solicitud.estado_ss == WebSolicitudServicio.EstadoDeServicio.Aceptada:
        solicitud.estado_ss = WebSolicitudServicio.EstadoDeServicio.SERVICIOREALIZADO
    elif solicitud.estado_ss == WebSolicitudServicio.EstadoDeServicio.NuevaFechaPropuestaCliente:
        solicitud.estado_ss = WebSolicitudServicio.EstadoDeServicio.Aceptada
    solicitud.save()
    return redirect('solicitudes')
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

#https://www.transbankdevelopers.cl/documentacion/como_empezar#como-empezar
#https://www.transbankdevelopers.cl/documentacion/como_empezar#codigos-de-comercio
#https://www.transbankdevelopers.cl/referencia/webpay

# Tipo de tarjeta   Detalle                        Resultado
#----------------   -----------------------------  ------------------------------
# VISA              4051885600446623
#                   CVV 123
#                   cualquier fecha de expiración  Genera transacciones aprobadas.
# AMEX              3700 0000 0002 032
#                   CVV 1234
#                   cualquier fecha de expiración  Genera transacciones aprobadas.
# MASTERCARD        5186 0595 5959 0568
#                   CVV 123
#                   cualquier fecha de expiración  Genera transacciones rechazadas.
# Redcompra         4051 8842 3993 7763            Genera transacciones aprobadas (para operaciones que permiten débito Redcompra y prepago)
# Redcompra         4511 3466 6003 7060            Genera transacciones aprobadas (para operaciones que permiten débito Redcompra y prepago)
# Redcompra         5186 0085 4123 3829            Genera transacciones rechazadas (para operaciones que permiten débito Redcompra y prepago)

@csrf_exempt
def iniciar_pago(request, id):
    print("Webpay Plus Transaction.create")
    producto = Producto.objects.get(id = id)
    buy_order = str(random.randrange(1000000, 99999999))
    session_id = request.user.username

    request.session['buyProductID'] = id

    print(producto.precio)
    amount = producto.precio
    return_url = 'http://127.0.0.1:8000/pago_exitoso/'

    commercecode = "597055555532"
    apikey = "579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C"
    
    tx = Transaction(options=WebpayOptions(commerce_code=commercecode, api_key=apikey, integration_type="TEST"))
    response = tx.create(buy_order, session_id, amount, return_url)
    print(response['token'])

    #perfil = myUser.objects.get(user=request.user)
    #form = registroform()

    context = {
        "buy_order": buy_order,
        "session_id": session_id,
        "amount": amount,
        "return_url": return_url,
        "response": response,
        "token_ws":  response['token'],
        "url_tbk": response['url'],
        "first_name": request.user.first_name,
        "last_name": request.user.last_name,
        "email": request.user.email,
        "rut": request.user.rut,
        "direccion": request.user.dirusu,
    }

    return render(request, "iniciarPago.html", context)


def str_time_prop(start, end, time_format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formatted in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))

def random_date(start, end, prop):
    return str_time_prop(start, end, '%Y/%m/%d', prop)

@csrf_exempt
def pago_exitoso(request):

    if request.method == "GET":
        token = request.GET.get("token_ws")
        print("commit for token_ws: {}".format(token))
        commercecode = "597055555532"
        apikey = "579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C"
        tx = Transaction(options=WebpayOptions(commerce_code=commercecode, api_key=apikey, integration_type="TEST"))
        response = tx.commit(token=token)
        print("response: {}".format(response))
        """
        if response['response_code'] == 0 :
            
            print(request.session.get('buyProductID'))
            print(request.user.id)
            dnow = datetime.now()
            datePlus1Day = dnow.replace(day= dnow.day + 1)
            dateplus4months = dnow.replace(month= dnow.month + 4)
            randate = random_date(datePlus1Day.strftime("%Y/%m/%d"),dateplus4months.strftime("%Y/%m/%d"),random.random())
            randhour = dnow.replace(hour=random.randint(9, 20), minute= random.randint(0, 59),second= random.randint(0, 59)).strftime("%H:%M:%S")
            print(randate , randhour)
            tecnicos = myUser.objects.filter(is_tecnico=True)
            dictionarie = {}
            tecnicos_numero_ss = tecnicos.prefetch_related('rut_tecnico').annotate(n_ss = models.Count('rut_tecnico__numeross'))

            for i in tecnicos_numero_ss:
                dictionarie[i.id] = i.n_ss
            print(dictionarie)
            minval = min(dictionarie.values())
            res = list(filter(lambda x: dictionarie[x]==minval, dictionarie))
            random_list_number = random.randrange(0,len(res))
            tecnico = res[random_list_number]
            print(tecnico)
            producto = Producto.objects.get(id = request.session.get('buyProductID'))
            #WebFactura.objects.create(id_producto = producto.id, rut_cliente = myUser.objects.get(id = request.user.id), monto = producto.precio, descripcion = producto.nombre)
            #WebSolicitudServicio.objects.create(tipo_servicio = 'I', fecha_visita_solicitada = randate , hora_visita_solicitada = randhour, descripcion_requerimiento = "Instalacion", estado_ss = "P", id_cli = myUser.objects.get(id = request.user.id), id_tec =  myUser.objects.get(id = tecnico))
            GuiasDespacho.objects.create() 
        if response['response_code'] == -1:
            print('rechazado')
        """
        user = myUser.objects.get(username=response['session_id'])
        #perfil = myUser.objects.get(user=user)
        #form = registroform()

        context = {
            "buy_order": response['buy_order'],
            "session_id": response['session_id'],
            "amount": response['amount'],
            "response": response,
            "token_ws": token,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "rut": user.rut,
            "direccion": user.dirusu,
            "response_code": response['response_code']
        }
        return render(request, 'pagoExitoso.html', context)
    else:
        return redirect(home)