# app_lavanderia/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Rutas para la página de inicio
    path('', views.inicio_lavanderia, name='inicio_lavanderia'),

    # Rutas para el modelo Cliente
    path('clientes/', views.ver_clientes, name='ver_clientes'),
    path('clientes/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('clientes/actualizar/<int:id>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('clientes/borrar/<int:id>/', views.borrar_cliente, name='borrar_cliente'),

    # Rutas para el modelo Empleado <--- ¡Asegúrate de que estas existan!
    path('empleados/', views.ver_empleados, name='ver_empleados'), # <--- ESTA ES LA CLAVE
    path('empleados/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('empleados/actualizar/<int:id>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('empleados/borrar/<int:id>/', views.borrar_empleado, name='borrar_empleado'),

        # Rutas para el modelo Empleado <--- ¡Asegúrate de que estas existan!
    path('servicios/', views.ver_servicios, name='ver_servicios'), # <--- ESTA ES LA CLAVE
    path('servicios/agregar/', views.agregar_servicio, name='agregar_servicio'),
    path('servicios/actualizar/<int:id>/', views.actualizar_servicio, name='actualizar_servicio'),
    path('servicios/borrar/<int:id>/', views.borrar_servicio, name='borrar_servicio'),
]