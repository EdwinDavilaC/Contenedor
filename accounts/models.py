from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager #es similar al de forms


class UserManager(BaseUserManager):
    def create_user(self, email, username, name, id_number, last_name, password= None):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico!')
        
        if not id_number:
            raise ValueError('El usuario debe tener número de cédula!')

        usuario = self.model(
            username=username, 
            email = self.normalize_email(email), 
            name=name, 
            last_name=last_name, 
            id_number=id_number
        )

        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self, email, username, name, id_number, last_name, password= None):
        
        usuario = self.create_user (
            email,    
            username=username, 
            name=name, 
            last_name=last_name, 
            id_number=id_number,
            password=password
        )
        usuario.admin_user = True
        usuario.save()
        return usuario
        


class Usuario(AbstractBaseUser):
    username = models.CharField('Nombre de usuario', max_length=30, unique=True)
    email = models.EmailField('Correo elactronico', max_length=30, unique=True)
    name = models.CharField('Nombre', max_length=30, blank = True, null= True)
    last_name = models.CharField('Apellido', max_length=30, blank = True, null= True)
    id_number = models.CharField('Numero de cedula', max_length=10, unique=True)
    active_user = models.BooleanField(default=True)
    admin_user = models.BooleanField(default=False)
    address = models.CharField('Direccion', max_length=250, blank = True, null= True)
    phone_number = models.CharField('Numero de telefono', max_length=30, blank = True, null= True)
    image = models.ImageField( upload_to= 'pefil', blank = True, null= True)
    create= models.DateTimeField(auto_now_add=True)
    update= models.DateTimeField(auto_now=True)
    

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','name','last_name','id_number']

    def __str__(self):
        return f'(self.name),(self.last_name)'
        
    def has_perm(self,perm,obj =None):
        return True

    def has_module_perms (self,app_label):
        return True

    @property
    def is_staff(self):
        return self.admin_user
    


# Create your models here.
