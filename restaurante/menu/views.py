from django.shortcuts import render, redirect
from .models import Plato, Pago

# LISTAR
def lista_platos(request):
    platos = Plato.objects.all()
    return render(request, 'lista.html', {'platos': platos})

# CREAR
def crear_plato(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        Plato.objects.create(nombre=nombre, descripcion=descripcion, precio=precio)
        return redirect('lista')
    return render(request, 'crear.html')

# ELIMINAR
def eliminar_plato(request, id):
    plato = Plato.objects.get(id=id)
    plato.delete()
    return redirect('lista')

# EDITAR
def editar_plato(request, id):
    plato = Plato.objects.get(id=id)
    if request.method == 'POST':
        plato.nombre = request.POST['nombre']
        plato.descripcion = request.POST['descripcion']
        plato.precio = request.POST['precio']
        plato.save()
        return redirect('lista')
    return render(request, 'editar.html', {'plato': plato})

# PAGOS
def pagar_plato(request, id):
    plato = Plato.objects.get(id=id)
    if request.method == 'POST':
        nombre_cliente = request.POST['nombre']
        metodo_pago = request.POST['metodo']
        Pago.objects.create(
            plato=plato, 
            nombre_cliente = nombre_cliente, 
            metodo_pago=metodo_pago
            )
        return render (request, 'confirmacion.html', {'plato': plato})
    return render(request, 'pago.html', {'plato': plato})