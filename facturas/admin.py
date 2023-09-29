from django.contrib import admin
from .models import factura, codigoFinanciero
from import_export.admin import ImportExportModelAdmin


admin.site.site_header = "Gestion Pilar"
admin.site.site_title = "Gestion Pilar"





@admin.register(codigoFinanciero)
class codigoFinancieroAdmin(ImportExportModelAdmin):
    list_display= ('codigo',)

@admin.register(factura)
class facturaAdmin(ImportExportModelAdmin):
    list_display=('emision', 'nroFactura', 'proveedor', 'total', 'objeto')


    def get_queryset(self, request):

        # Obtener el usuario actualmente autenticado
        user = request.user

        # Obtener el nombre del grupo al que pertenece el usuario
        user_group_name = user.groups.first().name if user.groups.exists() else None

        # Inicializar el queryset con todas las facturas
        queryset = super().get_queryset(request)

        # Filtrar las facturas por el nombre del grupo del usuario
        if user_group_name:
            queryset = queryset.filter(codigo__codigo=user_group_name)

        return queryset
