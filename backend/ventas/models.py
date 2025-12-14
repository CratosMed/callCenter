from django.db import models
from django.contrib.auth.models import User

# --- 1. TABLA PRINCIPAL: LA VENTA ---
class Venta(models.Model):
    ESTADO_PENDIENTE = 'PENDIENTE'
    ESTADO_AGENDADO = 'AGENDADO'
    ESTADO_TRAMITADO = 'TRAMITADO'
    ESTADO_ACTIVO = 'ACTIVO'
    ESTADO_CANCELADO = 'CANCELADO'
    
    OPCIONES_ESTADO = [
        (ESTADO_PENDIENTE, 'Pendiente'),
        (ESTADO_AGENDADO, 'Agendado'),
        (ESTADO_TRAMITADO, 'Tramitado'),
        (ESTADO_ACTIVO, 'Activo'),
        (ESTADO_CANCELADO, 'Cancelado'),
    ]

    # Datos del Cliente
    es_empresa = models.BooleanField(default=False, verbose_name="¿Es Empresa?")
    titular = models.CharField(max_length=200, verbose_name="Nombre Titular")
    razon_social = models.CharField(max_length=200, null=True, blank=True, verbose_name="Razón Social")
    documento_identidad = models.CharField(max_length=20, unique=True, verbose_name="DNI / CIF")
    fecha_nacimiento = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    
    # Dirección y Compañía
    nombre_compania_actual = models.CharField(max_length=100)
    direccion = models.TextField()
    codigo_postal = models.CharField(max_length=10)
    cuenta_bancaria = models.CharField(max_length=34, verbose_name="IBAN / Cuenta")

    # Gestión de la Venta
    asesor = models.ForeignKey(User, on_delete=models.PROTECT)
    estado = models.CharField(max_length=20, choices=OPCIONES_ESTADO, default=ESTADO_PENDIENTE)
    fecha_cita = models.DateTimeField(null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True)
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        nombre = self.razon_social if self.es_empresa and self.razon_social else self.titular
        return f"{nombre} ({self.get_estado_display()})"

# --- 2. TABLA SECUNDARIA: TELÉFONOS ---
class Telefono(models.Model):
    venta = models.ForeignKey(Venta, related_name='telefonos', on_delete=models.CASCADE)
    numero = models.CharField(max_length=20)
    etiqueta = models.CharField(max_length=50, blank=True, help_text="Ej: Personal, Oficina")

    def __str__(self):
        return self.numero