from django import forms
from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from django.db import transaction
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget,AdminSplitDateTime

from .models import *

import datetime

class UpdateSolicitudServicioT(forms.ModelForm):
    class Meta:
        model = WebSolicitudServicio
        fields = ['fecha_visita_solicitada','hora_visita_solicitada']
        widgets = {
            
            'hora_visita_solicitada': forms.TimeInput(attrs= dict(type = 'time'))
        }
        def clean_field(self):
            date = self.cleaned_data["fecha_hora_visita_solicitada"]
            if date < datetime.date.today():
                raise forms.ValidationError("La fecha no puede estar en el pasado")
            return date
        
class EditProfile(forms.ModelForm):
    class Meta:
        model = myUser
        fields = ['first_name', 'last_name', 'email', 'password', 'username', 'rut', 'dirusu']

class registroform(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = myUser
        fields = ['username', 'email', 'password1', 'password2','dirusu']
        widgets = {
            'username': forms.TextInput(attrs=dict(placeholder = 'nombre de usuario')),
            'email': forms.EmailInput(attrs=dict(placeholder= 'Correo electronico')),
            'dirusu': forms.TextInput(attrs= dict(placeholder = 'Dirección')),
            
            'password1': forms.PasswordInput(attrs=dict(placeholder='Contraseña')),
            'password2': forms.PasswordInput(attrs=dict(placeholder = 'Repetir contraseña'))
        }
    @transaction.atomic()
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
        widgets = {
            'fecha_visita_solicitada': forms.DateInput(attrs=dict(type='date', value= datetime.date.today(), min = datetime.date.today)),
            'hora_visita_solicitada': forms.TimeInput(attrs= dict(type = 'time'))
        }
        def clean_field(self):
            date = self.cleaned_data["fecha_hora_visita_solicitada"]
            if date < datetime.date.today():
                raise forms.ValidationError("La fecha no puede estar en el pasado")
            return date


        
