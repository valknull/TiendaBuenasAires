from django.urls import path
from django.contrib import admin
from .views import *

urlpatterns = [
    path('producto_create/', producto_create.as_view(), name="producto_create"),
    path('producto_update/', producto_update.as_view(), name="producto_update"),
    path('producto_read/<id>/', producto_read, name="producto_read"),
    path('producto_read_all/', producto_read_all, name='producto_read_all'),
    path('producto_delete/<id>/', producto_delete, name="producto_delete"),
    #path('login', login, name='hi'),
    path('guias_despacho/',guias_despacho_all, name="guiasDespacho"),
    path('stock_venta/',bodega_stock_venta, name = 'stockventa'),
    path('apilogin',Login.as_view(), name='loginapi'),
    path('logout', Logout.as_view(), name='logoutapi')
]
