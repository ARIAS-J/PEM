from django.db import models
from django.contrib.auth.models import  AbstractUser, UserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
import uuid



# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)




class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, name='id')
    name = models.CharField(max_length=250, null=True )
    apellido = models.CharField(max_length=250, null=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=250, null=True)
    username = None
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    
    def __str__(self):
        return self.email


class Categoria(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, name='id')
    nombre = models.CharField(max_length=250, null=True,)
    
    
    #Relationship
    user = models.ForeignKey("User", on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.nombre


class Registro(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, name='id')
    monto = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    descripcion = models.CharField(max_length=1000, null=True)
    fecha = models.CharField(max_length=250, null=True)

    #Relationship
    user = models.ForeignKey("User", on_delete=models.CASCADE, null=True, blank=True)
    categoria = models.ForeignKey("Categoria", on_delete=models.CASCADE, null=True, blank=True)
