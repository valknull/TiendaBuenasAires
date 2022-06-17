from rest_framework import serializers
from core.models import Producto , myUser, GuiasDespacho,WebFactura

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = myUser
        fields = ('username', 'email','first_name','last_name')


class WebfacturaClienteSerializer(serializers.ModelSerializer):
    rut_cliente = serializers.StringRelatedField(many = False)
    class Meta:
        model = WebFactura
        fields = ['nrofac','rut_cliente']

class GuiaDespachoSerializer(serializers.ModelSerializer):
    #nrofac= serializers.StringRelatedField(many = False)
    nrofac = WebfacturaClienteSerializer(many = False, read_only = True)
    id_producto = serializers.StringRelatedField(many = False)

    class Meta:
        model = GuiasDespacho
        fields = ['numeroGD','nrofac','id_producto','estadogd']