from django.urls import path
from .views import *

urlpatterns = [
    path('home',home,name='home'),
    path('',registerpage, name='login'),
    path('itemP',itemP, name='item'),
    path('perfil',perfil, name='perfil'),
    path('sds',sds, name='sds'),
    path('facturas',facturas, name='facturas'),
    path('solicitudes',solicitudesS, name = 'solicitudes'),
    #path('sds',CrearSolicitudServicio.as_view(), name='sds'),
    path('facturas',facturas, name='facturas'),
    path('updateS/<id>', updatess, name='UpdateSolicitud'),
    path('logout/',logout_view, name='logout')
]