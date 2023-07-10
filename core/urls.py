#por terminar. Se van agregando mas archivos en el transcurso
from django.urls import path
from  .views import index,contacto,nosotros, poblar_base_datos,producto,producto_tienda,ficha_producto

urlpatterns = [
    path('',index, name="index"),
    path('contacto',contacto, name="contacto"),
    path('nosotros',nosotros, name="nosotros"),
    path('poblar_base_datos',poblar_base_datos,name="poblar_base_datos"),
    path('producto/<action>/<id>',producto,name="producto"),
    path('producto_tienda',producto_tienda,name="producto_tienda"),
    path('ficha_producto/<id>',ficha_producto,name="ficha_producto"),
]


