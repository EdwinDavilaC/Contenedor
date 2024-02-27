from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.conf import settings



app_name='accounts'
urlpatterns = [

    path('', login_required(views.GetUsers), name= "Pedido/dashboard.html" ),

]
  
