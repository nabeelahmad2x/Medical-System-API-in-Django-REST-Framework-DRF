from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy 


class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, contact, date_of_birth, password, **extra_fields):
        if not email:
            raise ValueError(gettext_lazy('The Email field must be set'))
        
        email = self.normalize_email(email)     
        user = self.model.objects.create(email=email, name=name, contact=contact, date_of_birth=date_of_birth, **extra_fields)
        #print('user----------------------0', user)
        #print('model----------------', self.model)
        user.set_password(password)
        return user

    def create_superuser(self, email, name, contact, date_of_birth, password, **extra_fields):
        #print("------------------------------------------admin")
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        #extra_fields.setdefault('has_module_perms', True)
        user = self.create_user(email, name, contact, date_of_birth, password, **extra_fields)
        print(user)
        return user

