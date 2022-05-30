"""""
from typing import Awaitable
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UsernameField
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from .models import Producto, myUser
from .forms import Producto, registroform
from transbank.error.transbank_error import TransbankError
from transbank.webpay.webpay_plus.transaction import Transaction
import random

def home(request):
    return render(request, "templates/home.html")

def tienda(request):
    data = {"list": Producto.objects.all().order_by('id')}
    return render(request, "core/home.html", data)

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
def iniciar_pago(request):
    print("Webpay Plus Transaction.create")
    buy_order = str(random.randrange(1000000, 99999999))
    session_id = request.user.username
    amount = random.randrange(10000, 1000000)
    return_url = 'http://127.0.0.1:8000/pago_exitoso/'

    response = Transaction.create(buy_order, session_id, amount, return_url)
    print(response.token)

    perfil = myUser.objects.get(user=request.user)
    form = registroform()

    context = {
        "buy_order": buy_order,
        "session_id": session_id,
        "amount": amount,
        "return_url": return_url,
        "response": response,
        "token_ws": response.token,
        "url_tbk": response.url,
        "first_name": request.user.first_name,
        "last_name": request.user.last_name,
        "email": request.user.email,
        "rut": perfil.rut,
    }

    return render(request, "core/iniciarPago.html", context)

@csrf_exempt
def pago_exitoso(request):

    if request.method == " ":
        token = request.POST.get("token_ws")
        print("commit for token_ws: {}".format(token))
        response = Transaction.commit(token=token)
        print("response: {}".format(response))

        user = User.objects.get(username=response.session_id)
        perfil = myUser.objects.get(user=user)
        form = registroform()

        context = {
            "buy_order": response.buy_order,
            "session_id": response.session_id,
            "amount": response.amount,
            "response": response,
            "token_ws": token,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "rut": perfil.rut,
        }

        return render(request, "core/pago_exitoso.html", context)
    
    return redirect(home)
"""