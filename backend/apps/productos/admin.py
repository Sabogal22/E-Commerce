from django.contrib import admin
from .models import Categoria, Producto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
  list_display = ['nombre']
  search_fields = ['nombre']

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
  list_display = ['nombre', 'precio', 'precio_final', 'stock', 'categoria']
  list_filter = ['categoria', 'stock']
  search_fields = ['nombre', 'descripcion']