
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import DO_NOTHING
# Create your models here.
class myUser(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_tecnico = models.BooleanField(default=False)
    is_bodeguero = models.BooleanField(default=False)
    is_vendedor = models.BooleanField(default=False)
    rut = models.CharField("Rut",max_length=10)
    dirusu = models.CharField("Direccion",max_length=300)
    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()


class Producto(models.Model):
    id= models.AutoField("id de producto", primary_key=True)
    nombre = models.CharField("Nombre del producto", max_length=150)
    precio = models.IntegerField("precio")
    imagen_producto = models.ImageField("imagen del producto", upload_to="images/productos", default="")
    descripcion = models.CharField("Descripción", max_length=300)

    def __str__(self):
        return self.nombre

class WebFactura(models.Model):
    nrofac = models.AutoField("Nro factura", primary_key=True)
    id_producto = models.OneToOneField(Producto, on_delete=models.DO_NOTHING,db_column='id_producto')
    rut_cliente = models.ForeignKey(myUser,on_delete=models.DO_NOTHING,db_column='rutcli')
    fechafac = models.DateField("Fecha factura",auto_now_add=True, blank=True)
    monto = models.IntegerField("Monto")
    descripcion = models.CharField("Descripcion factura", max_length=300, null=True)
    
    def __str__(self) -> str:
        return str(self.nrofac)


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
    numeross = models.AutoField("Nro solicitud de servicio",primary_key=True)
    tipo_servicio=models.CharField(max_length=1, choices=TiposDeServicio.choices, default=TiposDeServicio.Reparacion)
    fecha_creacion_solicitud = models.DateField("Fecha creación de solicitud", auto_now_add=True, blank=True)
    fecha_visita_solicitada = models.DateField("Fecha de visita solicitada")
    hora_visita_solicitada = models.TimeField("Hora de visita solicitada")
    descripcion_requerimiento = models.CharField("Descripción del servicio requerido",max_length=300)
    acepta_fecha_hora_solicitada = models.CharField("Aceptar o rechazar fecha de solicitud", choices=AceptaSolicitud.choices, default=AceptaSolicitud.Aceptar, max_length=1,blank=True,null=True)
    estado_ss = models.CharField(max_length=3,choices=EstadoDeServicio.choices, default=EstadoDeServicio.FechaVisitaAceptada, null=True,blank=True)
    id_cli = models.ForeignKey(myUser,on_delete=models.DO_NOTHING,related_name='rut_cliente', db_column='idcli')
    id_tec = models.ForeignKey(myUser,on_delete=models.DO_NOTHING,related_name='rut_tecnico', db_column='idtec', null=True, blank=True)
    
    def __str__(self) -> str:
        return str(self.numeross)

class GuiasDespacho(models.Model):
    class Estado(models.TextChoices):
        EnBodega = 'B',"En Bodega"
        Despachado = 'D', "Despachado"
        Entregado = 'E', "Entregado"
    nrofac = models.ForeignKey(WebFactura, models.DO_NOTHING, db_column='nrofac')
    numeroGD = models.AutoField("Numero guia de despacho",primary_key=True)
    id_producto = models.ForeignKey(Producto,on_delete=DO_NOTHING, db_column='id_producto')
    estadogd = models.CharField(max_length=1, choices=Estado.choices, default = Estado.EnBodega)

class BodegaStockProducto(models.Model):
    idb = models.IntegerField(primary_key=True)
    id_producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='id_producto')
    nrofac = models.ForeignKey(WebFactura, models.DO_NOTHING, db_column='nrofac', blank=True, null=True)
    
    def __str__(self) -> str:
        return str(self.idb)
