from django.db import models


# Create your models here.


UM = [
    ('Armados de Kits', 'Armados de Kits'),
    ('Acond. AVANOS ', 'Acond. AVANOS'),
    ('Acond. Impresión', 'Acond. Impresión'),
    ('Acond. Meditec ', 'Acond. Meditec '),
    
]


Serie = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('12', '12'),
    
]

Responsabl = [
    ('Rafael', 'Rafael'),
    ('Esteban', 'Esteban'),
    ('Randy', 'Randy'),
    ('Marco', 'Marco'),
    ('Guillermo', 'Guillermo'),
    ('Orlando', 'Orlando'),
    ('Edwin', 'Edwin'),
    ('Lorena', 'Lorena'),
    ('Otro', 'Otro'),
    
]


class Cliente(models.Model):
    
    Cliente_name = models.CharField('Nombre del cliente', max_length=60)
    Cedula = models.CharField('numero de cedula o Ruc', max_length=13, unique= False)
    Ciudad = models.CharField('Ciudad', max_length=60 )
    Sector = models.CharField('Sector', max_length=60)
    Referencia = models.CharField('Referencia', max_length=60)
    Calle_principal = models.CharField('Calle principal', max_length=60)
    Calle_secundaria = models.CharField('Calle secundaria', max_length=60)
    Numero_de_domicilio = models.CharField('Numero de domicilio', max_length=60 )
    
    create= models.DateTimeField(auto_now_add=True)
    update= models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'  {self.Cliente_name}  '



class Pedido(models.Model):
    
    Serie_code= models.CharField('Numero de serie', choices=Serie, max_length=2)
    Number_order = models.CharField('Numero de pedido', max_length=30, unique=False)
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Items_pedido = models.IntegerField('Numero de items en el pedido')
    date_expired_delivery = models.DateTimeField('Fecha de entrega')
    Envio_cliente = models.BooleanField(default=False)
    Acondicionamiento = models.BooleanField(default=False)
    Tipo_acondi = models.CharField('Tipo de acondicionamiento', choices=UM, max_length=30, blank= True,)
    Cantidad_acond = models.IntegerField('cantidad unidades acondicionamiento')
    Cantidad_personas = models.CharField('cantidad personas ingresan a acondi', max_length=2, blank= True)
    Status_prepara = models.BooleanField(default=False)
    Respnsable_prep = models.CharField('Responsable prepa', choices=Responsabl, max_length=30,blank= True,)
    Status_Revisado = models.BooleanField(default=False)
    Respnsable_revi = models.CharField('Responsable revi', choices=Responsabl, max_length=30, blank= True,)
    Guias = models.CharField('Numero de Guia', max_length=15, unique=False, blank= True,)
    Cajas = models.CharField('Numero de bultos', max_length=30, unique=False, blank= True,)
    price= models.FloatField('Precio', null= True ,blank = True )
    novedad_pedido = models.BooleanField(default=False, blank = True )
    Detalle_novedad = models.CharField('cantidad personas ingresan a acondi', max_length=100, blank= True)
    
                
    Cerrado = models.BooleanField(default=False)
             
        
        
    create= models.DateTimeField(auto_now_add=True)
    update= models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.Serie_code} {self.Number_order} {self.Cliente}'

