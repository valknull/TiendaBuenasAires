from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import DO_NOTHING
# Create your models here.
class myUser(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_tecnico = models.BooleanField(default=False)

class Cliente(models.Model):
    user = models.OneToOneField(myUser, on_delete=models.CASCADE,primary_key=True)

class Tecnico (models.Model):
    user = models.OneToOneField(myUser,on_delete=models.CASCADE,primary_key=True)

class Producto(models.Model):
    id= models.AutoField("id de producto", primary_key=True)
    nombre = models.CharField("Nombre del producto", max_length=50)
    precio = models.IntegerField("precio")
    imagen_producto = models.ImageField("imagen del producto", upload_to="images/productos", default="")
    descripcion = models.CharField("Descripción", max_length=50)
    estado = models.CharField("Estado del producto", max_length=20)
    


    def __str__(self):
        return self.nombre

class WebFactura(models.Model):
    class TipoFactura(models.TextChoices):
        Boleta = 'B',"Boleta"
        Factura = 'F',"Factura"
    id = models.AutoField("id de factura", primary_key=True)
    tipo_factura = models.CharField(max_length=1, choices=TipoFactura.choices,default=TipoFactura.Boleta)
    producto = models.OneToOneField(Producto, on_delete=models.DO_NOTHING)
    cliente = models.ForeignKey(Cliente,on_delete=models.DO_NOTHING)
    fechafac = models.DateField("Fecha factura")

"""#Fecha de visita aceptada
FECHA_A = "FechaVisitaAceptada"
#Nueva fecha prouesta
N_FECHA_P = "NuevaFechaPropuesta"
#Fecha de visita acordada con el cliente.
F_VISITA_A = "FechaVisitaAcordada"
SR = "ServicioRealizado"
"""


class WebSolicitudServicio(models.Model):
    class TiposDeServicio(models.TextChoices):
        Reparacion = 'R',"Reparacion"
        Mantencion = 'M',"Mantencion"
    class AceptaSolicitud(models.TextChoices):
        Aceptar = 'A',"Aceptar"
        Rechazar = 'R',"Rechazar"
    class EstadoDeServicio(models.TextChoices):
        FechaVisitaAceptada = 'FA',"Fecha Visita Aceptada"
        NuevaFechaPropuesta = 'NFP',"Nueva fecha propuesta"
        FechaVisitaAcordada = 'FVA',"Fecha de visita acordada"
        SERVICIOREALIZADO = 'SR',"Servicio Realizado"
    id = models.AutoField("Nro solicitud de servicio",primary_key=True)
    tipo_servicio=models.CharField(max_length=1, choices=TiposDeServicio.choices, default=TiposDeServicio.Reparacion)
    fecha_creacion_solicitud = models.DateField("Fecha creación de solicitud")
    fecha_hora_visita_solicitada = models.DateField("Fecha de visita solicitada")
    hora_visita_solicitada = models.DateTimeField("Hora de visita solicitada")
    descripcion_requerimiento = models.CharField("Descripción del servicio requerido",max_length=150)
    acepta_fecha_hora_solicitada = models.CharField("Aceptar o rechazar fecha de solicitud", choices=AceptaSolicitud.choices, default=AceptaSolicitud.Aceptar, max_length=1)
    fecha_visita_tecnica = models.DateField("Fecha de visita tecnica")
    hora_visita_tecnica = models.DateTimeField("Hora de visita tecnica")
    estado_ss = models.CharField(max_length=3,choices=EstadoDeServicio.choices, default=EstadoDeServicio.FechaVisitaAceptada)
    cliente = models.ForeignKey(Cliente,on_delete=models.DO_NOTHING)
    tecnico = models.ForeignKey(Tecnico,on_delete=models.DO_NOTHING)
    

class GuiasDespacho(models.Model):
    class Estado(models.TextChoices):
        EnBodega = 'B',"En Bodega"
        Despachado = 'D', "Despachado"
        Entregado = 'E', "Entregado"
    numeroOD = models.AutoField("Numero guia de despacho",primary_key=True)
    cliente = models.ForeignKey(Cliente,on_delete=DO_NOTHING)
    estadogd = models.ForeignKey(max_length=1, choices=Estado.choices, default = Estado.EnBodega)