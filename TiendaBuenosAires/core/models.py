from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import DO_NOTHING
# Create your models here.
class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_tecnico = models.BooleanField(default=False)



class producto(models.Model):
    id= models.AutoField("id de producto", primary_key=True)
    nombre = models.CharField("Nombre del producto", max_length=50)
    precio = models.IntegerField("precio")
    imagen_producto = models.ImageField("imagen del producto", upload_to="images/productos", default="")
    descripcion = models.CharField("Descripción", max_length=50)
    estado = models.CharField("Estado del producto", max_length=20)
    


    def __str__(self):
        return self.nombre
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
    tipo_servicio=models.CharField(max_length=1, choices=TiposDeServicio.choices, default=TiposDeServicio.Reparacion)
    fecha_creacion_solicitud = models.DateTimeField()
    fecha_hora_visita_solicitada = models.DateTimeField()
    descripcion_requerimiento = models.CharField(max_length=150)
    acepta_fecha_hora_solicitada = models.DateTimeField()
    fecha_hora_visita_tecnica = models.DateTimeField()

    class EstadoDeServicio(models.TextChoices):
        FechaVisitaAceptada = 'FA',"Fecha Visita Aceptada"
        NuevaFechaPropuesta = 'NFP',"Nueva fecha propuesta"
        FechaVisitaAcordada = 'FVA',"Fecha de visita acordada"
        SERVICIOREALIZADO = 'SR',"Servicio Realizado"
    estado_ss = models.CharField(max_length=3,choices=EstadoDeServicio.choices, default=EstadoDeServicio.FechaVisitaAceptada)

    cliente = models.OneToOneField(User,on_delete=models.DO_NOTHING)
    tecnico = models.OneToOneField(User,on_delete=models.DO_NOTHING)
    

