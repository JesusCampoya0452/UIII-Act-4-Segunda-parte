from django.db import models

# ==========================================
# MODELO: CLIENTE
# ==========================================
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()
    direccion = models.CharField(max_length=200)
    fecha_registro = models.DateField(auto_now_add=True)
    notas = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# ==========================================
# MODELO: EMPLEADO
# ==========================================
class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()
    fecha_contratacion = models.DateField()
    salario = models.DecimalField(max_digits=8, decimal_places=2)
    # La relación ManyToMany se define aquí.
    # Un Empleado puede estar asignado a muchos Servicios.
    # Un Servicio puede tener muchos Empleados asignados.
    servicios = models.ManyToManyField('Servicio', related_name='empleados')


    def __str__(self):
        return f"{self.nombre} ({self.puesto})"


# ==========================================
# MODELO: SERVICIO
# ==========================================
class Servicio(models.Model):
    # Relación uno a muchos: Un Servicio pertenece a un Cliente.
    # Un Cliente puede tener muchos Servicios.
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='servicios')

    tipo_servicio = models.CharField(max_length=100)
    fecha_servicio = models.DateField()
    hora_entrega = models.TimeField()
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    estado = models.CharField(
        max_length=50,
        choices=[
            ('Pendiente', 'Pendiente'),
            ('En proceso', 'En proceso'),
            ('Completado', 'Completado')
        ],
        default='Pendiente'
    )
    forma_pago = models.CharField(max_length=50, default='Efectivo')

    def __str__(self):
        return f"{self.tipo_servicio} - {self.cliente.nombre}"