from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import check_password
from pem.models import User

class CustomBackend(ModelBackend):
    def authenticate(self, request, **kwargs):
        email = kwargs['email']
        print('Aqui esta el email backend ==>>', email)
        password = kwargs['password']
        print('Aqui esta el password backend ==>>', password)
        try:
            customer = User.objects.get(email=email)
            print('GET query aqui ===>>', customer)
            password_isvalid = customer.check_password(password)
            print('aqui esta el password check ===>>', password_isvalid)
            if password_isvalid:
                
                return customer
        except User.DoesNotExist:
            pass