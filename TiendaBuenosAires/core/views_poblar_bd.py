
from django.shortcuts import redirect
from django.contrib.auth.hashers import make_password
from .models import *

def poblar_bd(request):
    #Truncar WebSolicitudServicio
    try:
        WebSolicitudServicio.objects.all().delete()
        print("tabla WebSolicitudServicio Truncada")
    except Exception as err:
        print(f"Error al truncar tabla WebSolicitudServicio: {err}")
    #Truncar tabla Bodega
    try:
        BodegaStockProducto.objects.all().delete()
        print("Tabla bodega truncada")
    except Exception as err:
        print(f"Error al truncar tabla Bodega truncada: {err}")
    #Truncar tabla GuiasDespacho
    try:
        GuiasDespacho.objects.all().delete()
        print("Tabla Guia Despacho truncada")
    except Exception as err:
        print(f"Error al truncar tabla Guia Despacho: {err}")
    #Truncar tabla WebFactura
    try:
        WebFactura.objects.all().delete()
    except Exception  as err:
        print(f"Error al truncar tabla WebFactura: {err}" )
    #Eliminación de objetos en Producto
    try:
        Producto.objects.all().delete()
        print("Tabla producto truncada")
    except Exception as err:
        print(f"Error al truncar tabla producto:  {err}")
    #Truncar usuarios
    try:
        myUser.objects.all().delete()
        #myUser.objects.filter(is_customer = True).delete()
        #myUser.objects.filter(is_bodeguero = True).delete()
        #myUser.objects.filter(is_tecnico = True).delete() 
        print("Tabla de usuarios truncada")
    except Exception as err:
        print(f"Error al truncar  la tabla:  {err}")
    #Poblar tabla Usuarios
    try:
        myUser.objects.create(username = "user1", first_name ="Ana", last_name = "Torres", email = "atorres@duoc.cl", is_customer = True , rut = "1111-1", dirusu = "La Florida", password = make_password("123") )
        myUser.objects.create(username = "user2", first_name ="Juan", last_name = "Pérez", email = "jperez@duoc.cl", is_customer = True , rut = "2222-2", dirusu = "Santiago", password = make_password("123"))
        myUser.objects.create(username = "user3", first_name ="Mario", last_name = "Ayala", email = "mayala@duoc.cl", is_customer = True , rut = "3333-3", dirusu = "Providencia", password = make_password("123"))
        myUser.objects.create(username = "user4", first_name ="John", last_name = "Soto", email = "jsoto@duoc.cl", is_customer = True , rut = "4444-4", dirusu = "Las Condes", password = make_password("123"))
        myUser.objects.create(username = "user5", first_name ="Pedro", last_name = "Mora", email = "pmora@duoc.cl", is_customer = True , rut = "5555-5", dirusu = "Maipú", password = make_password("123"))
        myUser.objects.create(username = "tec1", first_name ="Juan", last_name = "Gatica", email = "jgatica@duoc.cl", is_tecnico = True , rut = "6666-6", dirusu = "Cerro Navia", password = make_password("123"))
        myUser.objects.create(username = "tec2", first_name ="María", last_name = "Vera", email = "mvera@duoc.cl", is_tecnico = True , rut = "7777-7", dirusu = "Peñalolén", password = make_password("123"))
        myUser.objects.create(username = "tec3", first_name ="Pablo", last_name = "Díaz", email = "pdiazduoc.cl", is_tecnico = True , rut = "0000-0", dirusu = "La Reina", password = make_password("123"))
        myUser.objects.create(username = "bod1", first_name ="Carlos", last_name = "Reyes", email = "creyes@duoc.cl", is_bodeguero = True , rut = "8888-8", dirusu = "La Florida", password = make_password("123"))
        myUser.objects.create(username = "admin", first_name ="Elon", last_name = "Musk", email = "emusk@duoc.cl", is_staff = True , is_superuser = True, rut = "9999-9", dirusu = "La Reina", password = make_password("123"))
        print("Tabla de usuarios poblada")
    except Exception as err:
        print(f"Error al crear usuarios : {err}")
    #Poblar tabla Producto
    try:
        print("Iniciar poblamiento de tabla Producto.")
        Producto.objects.create(id= 1,nombre="Aire Wifi 9000 btu", imagen_producto="images/productos/AireWifi9000btu.webp", precio=299990, descripcion="Enfría 9-16 m2"),
        Producto.objects.create(id= 2,nombre="Split Inv 12000 btu", imagen_producto="images/productos/SplitInv12000btu.webp", precio=450000, descripcion="Frío/Calor"),
        Producto.objects.create(id= 3,nombre="Anwo VP", imagen_producto="images/productos/AnwoVP.jpg", precio=288990, descripcion="9000 Virus Protect"),
        Producto.objects.create(id= 4,nombre="Anwo Portátil", imagen_producto="images/productos/AnwoPortátil.webp", precio=131990, descripcion="12000 btu f/c"),
        Producto.objects.create(id= 5,nombre="GPORT-14", imagen_producto="images/productos/GPORT-14.jpg", precio=399990, descripcion="Anwo 14000 btu"),
        Producto.objects.create(id= 6,nombre="Kendal 12000", imagen_producto="images/productos/Kendal12000.jpg", precio=335990, descripcion="Climat 22-24 m2"),

        print("Tabla Producto fue poblada.")
    except Exception as err:
        print(f"Error al poblar tabla producto: {err}")
    #Poblar tabla WebFactura
    try:
        WebFactura.objects.create(nrofac=1 , id_producto =Producto.objects.get(nombre = "Aire Wifi 9000 btu") , rut_cliente=myUser.objects.get(rut = "1111-1"), fechafac ='2022-02-23' , monto = 25000 , descripcion = "Aire Wifi 9000 btu"),
        WebFactura.objects.create(nrofac=2 , id_producto =Producto.objects.get(nombre = "Split Inv 12000 btu") , rut_cliente=myUser.objects.get(rut = "2222-2") , fechafac ='2022-02-24', monto = 450000, descripcion = "Split Inv 12000 btu"),
        WebFactura.objects.create(nrofac=3 , id_producto =Producto.objects.get(nombre = "Anwo Portátil") , rut_cliente=myUser.objects.get(rut = "3333-3") , fechafac ='2022-03-03', monto = 25000, descripcion = "Anwo Portátil"),
        WebFactura.objects.create(nrofac=4 , id_producto =Producto.objects.get(nombre = "Anwo Portátil") , rut_cliente=myUser.objects.get(rut = "4444-4") , fechafac ='2022-03-08', monto = 25000, descripcion = "Anwo Portátil"),
        WebFactura.objects.create(nrofac=5 , id_producto =Producto.objects.get(nombre = "Anwo Portátil") , rut_cliente=myUser.objects.get(rut = "5555-5") , fechafac ='2022-03-15', monto = 25000, descripcion = "Anwo Portátil"),
        WebFactura.objects.create(nrofac=6 , id_producto =Producto.objects.get(nombre = "Anwo Portátil") , rut_cliente=myUser.objects.get(rut = "1111-1") , fechafac ='2022-03-27' , monto = 25000, descripcion = "Mantención"),
        WebFactura.objects.create(nrofac=7 , id_producto =Producto.objects.get(nombre = "GPORT-14") , rut_cliente=myUser.objects.get(rut = "1111-1") , fechafac ='2022-04-03' , monto = 25000, descripcion = "GPORT-14"),
        WebFactura.objects.create(nrofac=8 , id_producto =Producto.objects.get(nombre = "Anwo VP") , rut_cliente=myUser.objects.get(rut = "1111-1") , fechafac ='2022-04-08', monto = 25000, descripcion = "Anwo VP" ),
        WebFactura.objects.create(nrofac=9 , id_producto =Producto.objects.get(nombre = "GPORT-14") , rut_cliente=myUser.objects.get(rut = "1111-1") , fechafac ='2022-04-15', monto = 25000, descripcion = "GPORT-14"),
    except Exception as err:
        print(f"Error al poblar WebFactura:  {err}")
    #poblar guiasDespacho
    try:
        GuiasDespacho.objects.create(nrofac = WebFactura.objects.get(nrofac = 1) , numeroGD = 11 , id_producto =Producto.objects.get(id = 1) , estadogd = 'E'),
        GuiasDespacho.objects.create(nrofac = WebFactura.objects.get(nrofac = 2) , numeroGD = 22 , id_producto =Producto.objects.get(id = 2) , estadogd = 'D'),
        GuiasDespacho.objects.create(nrofac = WebFactura.objects.get(nrofac = 8) , numeroGD = 88 , id_producto =Producto.objects.get(id = 3) , estadogd = 'B'),
    except Exception as err:
        print(f"Error al poblar tabla GuiasDespacho: {err}")
    #Poblar tabla WebSolicitudServicio
    try:
        WebSolicitudServicio.objects.create(numeross = 1, nro_factura =WebFactura.objects.get(nrofac = 1), tipo_servicio = 'I' , fecha_visita_solicitada = '2022-03-02', hora_visita_solicitada = '09:00', descripcion_requerimiento = "Instalar equipo", estado_ss = "SR", id_cli = myUser.objects.get(rut = "1111-1"), id_tec = myUser.objects.get(rut = "6666-6")),
        WebSolicitudServicio.objects.create(numeross = 2, nro_factura =WebFactura.objects.get(nrofac = 2), tipo_servicio = 'I' , fecha_visita_solicitada = '2022-03-03', hora_visita_solicitada = '10:00', descripcion_requerimiento = "Instalar equipo", estado_ss = "A", id_cli = myUser.objects.get(rut = "2222-2"), id_tec = myUser.objects.get(rut = "6666-6")),
        WebSolicitudServicio.objects.create(numeross = 3, nro_factura =WebFactura.objects.get(nrofac = 3), tipo_servicio = 'M' , fecha_visita_solicitada = '2022-03-10', hora_visita_solicitada = '15:00', descripcion_requerimiento = "Cambiar enchufe", estado_ss = "A", id_cli = myUser.objects.get(rut = "3333-3"), id_tec = myUser.objects.get(rut = "6666-6")),
        WebSolicitudServicio.objects.create(numeross = 4, nro_factura =WebFactura.objects.get(nrofac = 4), tipo_servicio = 'M' , fecha_visita_solicitada = '2022-03-15', hora_visita_solicitada = '09:00', descripcion_requerimiento = "Limpiar filtro", estado_ss = "A", id_cli = myUser.objects.get(rut = "4444-4"), id_tec = myUser.objects.get(rut = "6666-6")),
        WebSolicitudServicio.objects.create(numeross = 5, nro_factura =WebFactura.objects.get(nrofac = 5), tipo_servicio = 'R' , fecha_visita_solicitada = '2022-03-22', hora_visita_solicitada = '17:00', descripcion_requerimiento = "Reparar equipo", estado_ss = "A", id_cli = myUser.objects.get(rut = "5555-5"), id_tec = myUser.objects.get(rut = "6666-6")),
        WebSolicitudServicio.objects.create(numeross = 6, nro_factura =WebFactura.objects.get(nrofac = 6), tipo_servicio = 'M' , fecha_visita_solicitada = '2022-03-03', hora_visita_solicitada = '11:00', descripcion_requerimiento = "Limpiar filtro", estado_ss = "SR", id_cli = myUser.objects.get(rut = "1111-1"), id_tec = myUser.objects.get(rut = "7777-7")),
        WebSolicitudServicio.objects.create(numeross = 7, nro_factura =WebFactura.objects.get(nrofac = 7), tipo_servicio = 'R' , fecha_visita_solicitada = '2022-03-10', hora_visita_solicitada = '16:00', descripcion_requerimiento = "Reparar aire", estado_ss = "M", id_cli = myUser.objects.get(rut = "1111-1"), id_tec = myUser.objects.get(rut = "6666-6")),
        WebSolicitudServicio.objects.create(numeross = 8, nro_factura =WebFactura.objects.get(nrofac = 8), tipo_servicio = 'I' , fecha_visita_solicitada = '2022-03-15', hora_visita_solicitada = '10:00', descripcion_requerimiento = "Instalar equipo", estado_ss = "M", id_cli = myUser.objects.get(rut = "1111-1"), id_tec = myUser.objects.get(rut = "7777-7")),
        WebSolicitudServicio.objects.create(numeross = 9, nro_factura =WebFactura.objects.get(nrofac = 9), tipo_servicio = 'R' , fecha_visita_solicitada = '2022-03-22', hora_visita_solicitada = '18:00', descripcion_requerimiento = "Enchufe  quemado", estado_ss = "A", id_cli = myUser.objects.get(rut = "1111-1"), id_tec = myUser.objects.get(rut = "8888-8")),
    except Exception as err:
        print(f"Error al poblar tabla WebSServicio: {err}")
    #Poblar tabla BodegaStockProducto
    try:
        BodegaStockProducto.objects.create(idb = 88888, id_producto =Producto.objects.get(id = 1), nrofac = WebFactura.objects.get(nrofac = 1)),
        BodegaStockProducto.objects.create(idb = 22222, id_producto =Producto.objects.get(id = 2), nrofac = WebFactura.objects.get(nrofac = 2)),
        BodegaStockProducto.objects.create(idb = 90001, id_producto =Producto.objects.get(id = 3), nrofac = WebFactura.objects.get(nrofac = 8)),
        BodegaStockProducto.objects.create(idb = 90002, id_producto =Producto.objects.get(id = 1)),
        BodegaStockProducto.objects.create(idb = 11111, id_producto =Producto.objects.get(id = 3)),
        BodegaStockProducto.objects.create(idb = 90003, id_producto =Producto.objects.get(id = 4)),
        BodegaStockProducto.objects.create(idb = 90004, id_producto =Producto.objects.get(id = 6)),
        BodegaStockProducto.objects.create(idb = 90005, id_producto =Producto.objects.get(id = 1)),
        BodegaStockProducto.objects.create(idb = 90006, id_producto =Producto.objects.get(id = 3)),
        BodegaStockProducto.objects.create(idb = 90007, id_producto =Producto.objects.get(id = 4)),
    except Exception as err:
        print(f"Error al poblar Bodega: {err}") 
    return redirect('home')





