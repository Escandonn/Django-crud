from django.db import models


# Modelo de tareas
class Task(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField(max_length=1000)
  created = models.DateTimeField(auto_now_add=True)
  datecompleted = models.DateTimeField(null=True, blank=True)
  important = models.BooleanField(default=False)
  
  def __str__(self):
    return self.title + ' - ' + self.user.username


# Modelo de productos comprados
class ProductoComprado(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    fecha_importacion = models.DateField()
    cantidad = models.IntegerField(default=0)  # Campo para el inventario

    class Meta:
        verbose_name = "Producto Comprado"
        verbose_name_plural = "Productos Comprados"

    def __str__(self):
        return self.nombre

# Modelo de productos vendidos
class ProductoVenta(models.Model):
    producto = models.ForeignKey(ProductoComprado, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_venta = models.DateField(auto_now_add=True)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"

    def save(self, *args, **kwargs):
        # Actualizar el precio_total antes de guardar
        self.precio_total = self.cantidad * self.producto.precio_venta
        super(ProductoVenta, self).save(*args, **kwargs)