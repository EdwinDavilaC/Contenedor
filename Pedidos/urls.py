from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required




app_name='Pedidos'
urlpatterns = [

    path('clientes/', login_required(views.GetClientes), name= "cliente" ),
    path('pedidos/', login_required(views.GetPedidos), name= "pedidos" ),
    
    
         
]
  

