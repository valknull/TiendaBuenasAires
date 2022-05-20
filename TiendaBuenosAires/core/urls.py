from urllib.parse import urlparse
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='login')
]