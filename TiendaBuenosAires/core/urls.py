from django.urls import path
from .views import *

urlpatterns = [
    path('home',home,name='home'),
    path('',login, name='login'),
    path('itemP',itemP, name='item'),
    path('perfil',perfil, name='perfil'),
    path('sds',sds, name='sds'),
    path('facturas',facturas, name='facturas')
]