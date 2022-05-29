from django import forms
from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from django.db import transaction
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget,AdminSplitDateTime

from .models import *


class UpdateSolicitudServicioT(forms.ModelForm):
    class Meta:
        model = WebSolicitudServicio
        fields = ['fecha_visita_solicitada','hora_visita_solicitada']
        
class EditProfile(forms.ModelForm):
    class Meta:
        model = myUser
        fields = ['first_name', 'last_name', 'email', 'password', 'username', 'rut', 'dirusu']

class registroform(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = myUser
        fields = ['username', 'email', 'password1', 'password2']
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        return user

class SolicitudServicioForm(forms.ModelForm):
    class Meta:
        model = WebSolicitudServicio
        fields = ['tipo_servicio','fecha_visita_solicitada','hora_visita_solicitada','descripcion_requerimiento']
        excludes = ['rut_cli']

        
