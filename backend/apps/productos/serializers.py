from rest_framework import serializers
from .models import Producto, Categoria

class CategoriaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Categoria
    fields = ['id', 'nombre']

class ProductoSerializer(serializers.ModelSerializer):
  categoria_nombre = serializers.CharField(source='categoria.nombre', read_only=True)
  precio_final = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
  tiene_promocion = serializers.BooleanField(read_only=True)
    
  class Meta:
    model = Producto
    fields = [
      'id', 'nombre', 'descripcion', 'precio', 'precio_promocion',
      'precio_final', 'tiene_promocion', 'categoria', 'categoria_nombre',
      'stock', 'imagen'
    ]