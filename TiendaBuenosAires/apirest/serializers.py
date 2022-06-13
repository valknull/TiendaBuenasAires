from rest_framework import serializers
from core.models import Producto , myUser

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = myUser
        fields = ('username', 'email','first_name','last_name')
