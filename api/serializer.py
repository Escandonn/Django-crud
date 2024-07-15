from rest_framework import serializers
from .models import Task,ProductoComprado,ProductoVenta


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # fields = ('id', 'title', 'description', 'done')
        fields = '__all__'



class Producto_CompradoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoComprado
        fields = '__all__'

class Producto_VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoVenta
        fields = '__all__'

