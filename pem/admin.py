from django.contrib import admin
from .models import User,Registro,Categoria

# Register your models here.
admin.site.register(User)
admin.site.register(Registro)
admin.site.register(Categoria)