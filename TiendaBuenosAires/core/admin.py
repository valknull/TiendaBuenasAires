from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Producto)
admin.site.register(myUser)
admin.site.register(WebSolicitudServicio)
admin.site.register(WebFactura)
admin.site.register(GuiasDespacho)

