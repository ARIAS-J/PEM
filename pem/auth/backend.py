from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import check_password
from pem.models import User

class CustomBackend(ModelBackend):
    def authenticate(self, request, **kwargs):
        email = kwargs['email']
        
        password = kwargs['password']
        
        try:
            customer = User.objects.get(email=email)
            
            password_isvalid = customer.check_password(password)
            
            if password_isvalid:
                
                return customer
        except User.DoesNotExist:
            pass