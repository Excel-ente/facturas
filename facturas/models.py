from django.db import models

class codigoFinanciero(models.Model):
    codigo = models.CharField(max_length= 255, blank=False, unique=True)
    
    def __str__(self):
        return str(self.codigo)

class factura(models.Model):
    emision = models.DateField(blank=True, null = True)
    alta = models.DateField(blank=True, null = True)
    codigo = models.ForeignKey(codigoFinanciero, on_delete=models.CASCADE, blank=False, null=False)
    nroFactura = models.CharField(max_length = 255, blank=True, null = True)
    proveedor = models.CharField(max_length = 255, blank=True, null = True)
    oc = models.CharField(max_length = 255, blank=True, null = True)
    total = models.DecimalField(max_digits=15, decimal_places=2, default=0, blank=True, null = True )
    ff = models.CharField(max_length = 255, blank=True, null = True)
    unidadEjecutora = models.CharField(max_length = 255, blank=True, null = True)
    objeto = models.CharField(max_length = 255, blank=True, null = True)
    fondoAfectado = models.CharField(max_length = 255, blank=True, null = True)
    
