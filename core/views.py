##from argparse import Action
from django.shortcuts import render,redirect
from .models import Producto, Categoria
from .forms import  ProductoForm

# Create your views here.

def index(request):
    return render(request, "core/index.html")
def nosotros(request):
    return render(request, "core/nosotros.html")

def contacto(request):
    return render(request, "core/contacto.html")


def producto_tienda(request):
    data = {"list": Producto.objects.all().order_by('id_producto')}
    return render (request,"core/producto_tienda.html",data)

def ficha_producto(request,id):
    producto = Producto.objects.get(id_producto=id)
    data = {"producto" : producto}
    return render(request,"core/ficha_producto.html",data)

def producto(request,action,id):
    data = {"mesg" : "","form": ProductoForm, "action":action,"id":id   }
    
    if action == 'ins':
        if request.method =='POST':
            form = ProductoForm(request.POST, request.FILES)
            if form.is_valid:
                try:
                    form.save()
                    data["mesg"] = "Producto agregado"
                except:
                    data["mesg"] ="error al crear nuevo producto"
    elif action=='upd':
        objeto = Producto.objects.get(id_producto=id) 
        if request.method== "POST":
            form= ProductoForm(data=request.POST, files=request.FILES,instance=objeto)
            if form.is_valid:
                form.save()
                data["mesg"] = "Producto actualizado"
            data["form"] = ProductoForm(instance=objeto)
            
    elif action == 'del':
        try:
            Producto.objects.get(id_producto=id).delete()
            data["mesg"] = "Producto eliminado"
            return redirect(producto, action='ins',id = '-1')
        except:
            data["mesg"] = "el producto no existe/ya esta eliminado"
            
    data["list"] = Producto.objects.all().order_by('id_producto')
    return render(request,"core/producto.html",data )

#######################################################################
#######################################################################
#######################################################################
def poblar_base_datos(request):
    Producto.objects.all().delete()
    Producto.objects.create(id_producto=1,nombre="rines",precio=500000,categoria=Categoria.objects.get(id_categoria=1))
    Producto.objects.create(id_producto=2,nombre="perifericos",precio=130000,categoria=Categoria.objects.get(id_categoria=1))
    Producto.objects.create(id_producto=3,nombre="aleron carbono",precio=320000,categoria=Categoria.objects.get(id_categoria=1))
    return redirect(producto,action='ins',id='-1')

