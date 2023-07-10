from django.db import models

# Create your models here.
class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True,verbose_name="id de categoria")
    nombre_categoria = models.CharField(max_length=50,blank=False, null=False, verbose_name="nombre categoria")
    
    def __str__(self):
        return self.nombre_categoria
    
class Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True, verbose_name="id de producto")
    nombre = models.CharField(max_length=50, blank=False, null=False, verbose_name="nombre producto")
    precio = models.IntegerField(blank=False, null=False, verbose_name="precio del producto")
    imagen=models.ImageField(upload_to="imagenes/",default="nn.jpg",null=False,blank=False, verbose_name="imagen")
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.nombre
    
