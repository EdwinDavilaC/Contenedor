from django.shortcuts import render, redirect
from .models import Cliente, Pedido
from django.db.models import Sum




def inicio(request):
    
   
    Pedidos = Pedido.objects.all()
    Clientes = Cliente.objects.all()

    Pedidos_prepa = Pedidos.filter(Status_prepara=True).count()
    Pedisos_revisados = Pedidos.filter(Status_Revisado=True).count()
    Total_pedidos = Pedidos.count()
    Pedidos_cerrados = Pedidos.filter(Cerrado=True).count()
    Pedido_cliente = Pedidos.filter(Envio_cliente=True).count()
    Pedido_Rcliente = Pedidos.filter(Envio_cliente=False).count()
    Acond = Pedidos.filter(Acondicionamiento=True).count()
    NOAcond = Pedidos.filter(Acondicionamiento=False).count()
    Angela = Pedidos.filter(Serie_code = 7).filter(Cerrado = False).count()
    Monica = Pedidos.filter(Serie_code = 1).filter(Cerrado = False).count()
    Mariasu = Pedidos.filter(Serie_code = 3).filter(Cerrado = False).count()
    Karina = Pedidos.filter(Serie_code = 6).filter(Cerrado = False).count()
    Diana = Pedidos.filter(Serie_code = 5).filter(Cerrado = False).count()
    Tahira = Pedidos.filter(Serie_code = 12).filter(Cerrado = False).count()
    hora_pedidos = Pedidos.filter(Status_Revisado=False).aggregate(Sum('Items_pedido'))['Items_pedido__sum']*7
    
    
    
    
    
    
    context = {
        'Pedidos' : Pedidos,
        'Clientes' : Clientes,
        'Pedidos_prepa' : Pedidos_prepa,
        'Pedisos_revisados' : Pedisos_revisados,
        'Total_pedidos' : Total_pedidos,
        'Pedidos_cerrados' : Pedidos_cerrados,
        'Pedido_cliente' : Pedido_cliente,
        'Pedido_Rcliente' : Pedido_Rcliente,
        'Acond' : Acond,
        'NOAcond' : NOAcond,
        'Monica' : Monica,
        'Angela' : Angela,
        'Mariasu' : Mariasu,
        'Karina' : Karina,
        'Diana' : Diana,
        'Tahira' : Tahira,
        'hora_pedidos' : hora_pedidos,
        
       
    }
    
    return render(request,"dashboard.html", context)
