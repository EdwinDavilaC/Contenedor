from django.contrib import admin

from Pedidos.models import Pedido, Cliente







admin.site.site_header = "Pedidos Banda Vanoni 2023"
admin.site.site_title = "Ingrese o modifique su pedido"


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('Serie_code','Number_order','Cliente','date_expired_delivery', 'Status_prepara', 'Respnsable_prep', 'Status_Revisado', 'Respnsable_revi', 'Guias', 'price', 'Cerrado' )
    ordering = ('Status_prepara', 'Status_Revisado',)
    search_fields = ('Number_order', 'Cliente',)
    list_editable = ('Status_prepara', 'Respnsable_prep', 'Status_Revisado', 'Respnsable_revi', 'Guias', 'price',)
    list_display_links = ('Number_order',)


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('Cedula','Cliente_name','Ciudad','create')
    ordering = ('Cliente_name',)
    search_fields = ('Cedula','Cliente_name',)
# Register your models here.

