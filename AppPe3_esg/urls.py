from django.urls import path
from AppPe3_esg.views import *

urlpatterns = [
    path(''                     ,inicio         ,   name = 'molde_inicio'),

    path('cliente/'             ,ver_clientes   ,   name = 'clientes'),
    path('proveedores/'         ,ver_proveedores,   name = 'proveedores'),  
    path('pedidos/'             ,ver_pedidos,       name = 'pedidos'),     

    path('crear_cliente/'       ,crear_cliente),
    path('crear_proveedor/'     ,crear_proveedor),
    path('crear_compra/'        ,registrar_compra),
    path('crear_pedido/'        ,crear_pedido),

    path('buscar_cliente/'      ,buscar_cliente),
    path('buscar_proveedor/'    ,buscar_proveedor),
    path('buscar_compra/'       ,buscar_compras),
    path('buscar_pedido/'       ,buscar_pedido),

    
]
