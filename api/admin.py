from django.contrib import admin
from .models import Task,ProductoComprado,ProductoVenta

# Register your models here.

admin.site.register(Task)
admin.site.register(ProductoComprado)
admin.site.register(ProductoVenta)