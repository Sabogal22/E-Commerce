from django.db import models

class Categoria(models.Model):
  nombre = models.CharField(max_length=100)
    
  def __str__(self):
    return self.nombre

class Producto(models.Model):
  nombre = models.CharField(max_length=200)
  descripcion = models.TextField()
  precio = models.DecimalField(max_digits=10, decimal_places=2)
  precio_promocion = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
  categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
  stock = models.IntegerField(default=0)
  imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    
  def __str__(self):
    return self.nombre
    
  @property
  def precio_final(self):
    """Devuelve el precio con promoción si existe"""
    return self.precio_promocion if self.precio_promocion else self.precio
    
  @property
  def tiene_promocion(self):
    """Verifica si tiene precio promocional"""
    return self.precio_promocion is not None