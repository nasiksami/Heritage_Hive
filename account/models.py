from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.

from django.contrib.auth.models import BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user( first_name, last_name, username, email, password=None,user_type="buyer"):
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have a username')
        print(user_type)

        user = Account(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        if (user_type=="seller"):
            user.is_seller=True
        user.set_password(password)
        user.save()
        print(user)
        return user

    def create_superuser(self,first_name, last_name, email, username, password):
        user = Account(
            email=email,
            username=username,
            
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

    @classmethod
    def create_account(cls, user_type='buyer', **kwargs):
        if user_type == 'buyer':
            return cls.create_user(**kwargs)
        if user_type=="seller":
            return cls.create_user(**kwargs,user_type="seller")
        if user_type=="superuser":
            return cls.create_superuser(**kwargs)
        else:
            raise ValueError("Invalid user type")

class Account(AbstractBaseUser):
    first_name= models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username=models.CharField(max_length=50,unique=True)
    email=models.EmailField(max_length=100,unique=True)
    phone_number=models.CharField(max_length=50)


    #required filed mendotory 

    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now_add=True)
    is_seller=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    is_superadmin=models.BooleanField(default=False)
    

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','first_name','last_name']

    objects=MyAccountManager()

    def __str__(self):
        return self.email
    

    def has_perm(self,perm,obj=None):
        return self.is_admin
    

    def has_module_perms(self,add_label):
        return True




class UserProfile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    address_line_1 = models.CharField(blank=True, max_length=100)
    address_line_2 = models.CharField(blank=True, max_length=100)
    profile_picture = models.ImageField(blank=True, upload_to='userprofile')
    city = models.CharField(blank=True, max_length=20)
    state = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=20)

    def __str__(self):
        return self.user.first_name

    def full_address(self):
        return f'{self.address_line_1} {self.address_line_2}'
