from django.forms import ModelForm
from .models import Task,ProductoComprado,ProductoVenta


class ProductoCompradoForm(ModelForm):
    class Meta:
        model = ProductoComprado
        fields = '__all__'


class ProductoVentaForm(ModelForm):
    class Meta:
        model = ProductoVenta
        fields = '__all__'

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']