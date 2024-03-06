from django.shortcuts import render
from django.http import HttpResponse

# importo los models de la App
from AppPe3_esg.models import *

# importo los forms de la app 
from AppPe3_esg.forms import *


# Create your views here.

# INICIO

def inicio(request):
     
     return render(request, 'inicio.html')


# ************************ CLIENTES ***********************
# creacion
def ver_clientes(request):

    return render(request, 'ver_clientes.html')


def crear_cliente(request):

    if request.method == 'POST':

        formularioCli = Clientesforms(request.POST) #Esto almacena la informacion ingresada en el formulario

        if formularioCli.is_valid():

            info_cli = formularioCli.cleaned_data # convierte la info del form en diccionario

            nvo_cli= Clientes(  nombre      = info_cli['nombre'], 
                                apellido    = info_cli['apellido'],
                                documento   = info_cli['documento'],
                                email       = info_cli['email'])
            
            nvo_cli.save()

            return render(request, 'inicio.html')

    else:

        formulario = Clientesforms() 

    return render(request, 'crear_cliente.html', {'formu_cli':formulario})

## busqueda
def buscar_cliente(request):

    if request.GET:

        documento   = request.GET['documento']
        clientebus  = Clientes.objects.filter(documento__icontains=documento)

        mensaje = f'Estos son los datos del cliente obtenidos para documento ingresado: {documento}'

        return render(  request, 
                        'buscar_cliente.html',
                        {'mensaje':mensaje, 
                        'resultados':clientebus})
    
    else:
    
        return render(request, 'buscar_cliente.html')
    
# ************************ PROVEEDORES ***********************
# creacion
def ver_proveedores(request):

    return render(request, 'ver_proveedores.html')


def crear_proveedor(request):

    if request.method == 'POST':

        formularioProv = Proveedoresforms(request.POST) #Esto almacena la informacion ingresada en el formulario

        if formularioProv.is_valid():

            info_prov = formularioProv.cleaned_data # convierte la info del form en diccionario

            nvo_prov= Proveedores(  razon_social= info_prov['razon_social'], 
                                    cuit        = info_prov['cuit'],
                                    email       = info_prov['email'],
                                    telefono    = info_prov['telefono'])
            
            nvo_prov.save()

            return render(request, 'inicio.html')

    else:

        formulario = Proveedoresforms() 

    return render(request, 'crear_proveedor.html', {'formu_prov':formulario})

## busqueda
def buscar_proveedor(request):

    if request.GET:

        cuit   = request.GET['cuit']
        provbus  = Proveedores.objects.filter(cuit__icontains=cuit)

        mensaje = f'Estos son los datos del Porveedor obtenidos para la cuit ingresada: {cuit}'

        return render(  request, 
                        'buscar_proveedor.html',
                        {'mensaje':mensaje, 
                        'resultados':provbus})
    
    else:
    
        return render(request, 'buscar_proveedor.html')    
    

# ************************ COMPRAS ***********************
# creacion

def registrar_compra(request):

    if request.method == 'POST':

        formularioCompras = Comprasforms(request.POST) #Esto almacena la informacion ingresada en el formulario

        if formularioCompras.is_valid():

            info_compras = formularioCompras.cleaned_data # convierte la info del form en diccionario

            nva_compra  = Compras(  producto    = info_compras['producto'], 
                                    cantidad    = info_compras['cantidad'],
                                    cuit_prov   = info_compras['cuit_prov'],
                                    fecha_comp  = info_compras['fecha_comp'])
            
            nva_compra.save()

            return render(request, 'ver_proveedores.html')

    else:

        formulario = Comprasforms() 

    return render(request, 'crear_compra.html', {'formu_compra':formulario})

## busqueda
def buscar_compras(request):

    if request.GET:

        cuit_prov   = request.GET['cuit_prov']
        comprabus   = Compras.objects.filter(cuit_prov__icontains=cuit_prov)

        mensaje = f'Estas son las compras realizadas al Porveedor con cuit: {cuit_prov}'

        return render(  request, 
                        'buscar_compra.html',
                        {'mensaje':mensaje, 
                        'resultados':comprabus})
    
    else:
    
        return render(request, 'buscar_compra.html')       
    

# ************************ PEDIDOS ***********************
# creacion
def ver_pedidos(request):

    return render(request, 'ver_pedidos.html')

def crear_pedido(request):

    if request.method == 'POST':

        formularioPedido = Pedidosforms(request.POST) #Esto almacena la informacion ingresada en el formulario

        if formularioPedido.is_valid():

            info_pedido = formularioPedido.cleaned_data # convierte la info del form en diccionario

            nva_pedido  = Pedidos(  fecha_pedido    = info_pedido['fecha_pedido'], 
                                    cantidad_p      = info_pedido['cantidad_p'],
                                    monto           = info_pedido['monto'],
                                    doc_cliente     = info_pedido['doc_cliente'])
            
            nva_pedido.save()

            return render(request, 'ver_pedidos.html')

    else:

        formulario = Pedidosforms() 

    return render(request, 'crear_pedido.html', {'formu_pedido':formulario})

## busqueda
def buscar_pedido(request):

    if request.GET:

        doc_cliente = request.GET['documento']
        pedidobus   = Pedidos.objects.filter(doc_cliente__icontains=doc_cliente)

        mensaje = f'Estos son los pedidos realizados Cliente: {doc_cliente}'

        return render(  request, 
                        'buscar_pedido.html',
                        {'mensaje':mensaje, 
                        'resultados':pedidobus})
    
    else:
    
        return render(request, 'buscar_pedido.html')          