from django.db import models  # Importing models from Django
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager  # Importing necessary classes from Django's authentication module
from abc import ABC, abstractmethod  # Importing ABC and abstractmethod for abstract classes

# Create your models here.
<<<<<<< Updated upstream
from subscribe.interface import Observer  # Importing Observer interface
from django.contrib.auth.models import BaseUserManager  # Importing BaseUserManager from Django's authentication module
from django.core.mail import EmailMessage  # Importing EmailMessage class from Django's core mail module
=======
from subscribe.interface import Observer
from django.contrib.auth.models import BaseUserManager
from django.core.mail import EmailMessage
>>>>>>> Stashed changes

class UserFactory(BaseUserManager):
    @staticmethod
    def create_user(email, password, **extra_fields):
        """
        Factory method to create a new user.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = email
        user = Account(email=email, **extra_fields)  # Creating a new Account instance
        user.set_password(password)  # Setting the password for the user
        user.save()  # Saving the user instance
        return user

    def create_superuser(self, first_name, last_name, email, username, password):
        # Create a superuser with admin privileges
        user = Account(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)  # Setting the password for the superuser
        user.is_admin = True  # Setting is_admin flag to True for the superuser
        user.is_active = True  # Setting is_active flag to True for the superuser
        user.is_staff = True  # Setting is_staff flag to True for the superuser
        user.is_superadmin = True  # Setting is_superadmin flag to True for the superuser
        user.save(using=self._db)  # Saving the superuser instance
        return user

    @classmethod
    def create_account(self, user_type='buyer', **kwargs):
        if user_type == 'buyer':
            buyer = BuyerFactory.create_buyer(**kwargs)  # Creating a new buyer instance
            return buyer
        if user_type == "seller":
            seller = SellerFactory.create_seller(**kwargs)  # Creating a new seller instance
            return seller
        else:
            raise ValueError("Invalid user type")

class BuyerFactory(UserFactory):
    @staticmethod
    def create_buyer(email, password, **extra_fields):
        """
        Factory method to create a new buyer.
        """
        return UserFactory.create_user(email, password, **extra_fields)

class SellerFactory(UserFactory):
    @staticmethod
    def create_seller(email, password, **extra_fields):
        """
        Factory method to create a new seller.
        """
        extra_fields.setdefault('is_seller', True)  # Setting default value for is_seller field
        return UserFactory.create_user(email, password, **extra_fields)

class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)  # Defining first name field
    last_name = models.CharField(max_length=50)  # Defining last name field
    username = models.CharField(max_length=50, unique=True)  # Defining username field
    email = models.EmailField(max_length=100, unique=True)  # Defining email field
    phone_number = models.CharField(max_length=50)  # Defining phone number field

    # Required fields
    date_joined = models.DateTimeField(auto_now_add=True)  # Defining date joined field
    last_login = models.DateTimeField(auto_now_add=True)  # Defining last login field
    is_seller = models.BooleanField(default=False)  # Defining is seller field with default value
    is_admin = models.BooleanField(default=False)  # Defining is admin field with default value
    is_staff = models.BooleanField(default=False)  # Defining is staff field with default value
    is_active = models.BooleanField(default=False)  # Defining is active field with default value
    is_superadmin = models.BooleanField(default=False)  # Defining is superadmin field with default value

    USERNAME_FIELD = 'email'  # Setting email as the username field
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']  # Defining required fields for creating a user

    objects = UserFactory()  # Creating a UserFactory object

    def __str__(self):
        return self.email  # Returning email as the string representation of the user

    def has_perm(self, perm, obj=None):
        return self.is_admin  # Checking if the user has admin permissions

    def has_module_perms(self, add_label):
        return True  # Granting module permissions to the user

class UserProfile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)  # Defining a one-to-one relationship with Account model
    address_line_1 = models.CharField(blank=True, max_length=100)  # Defining address line 1 field
    address_line_2 = models.CharField(blank=True, max_length=100)  # Defining address line 2 field
    profile_picture = models.ImageField(blank=True, upload_to='userprofile')  # Defining profile picture field
    city = models.CharField(blank=True, max_length=20)  # Defining city field
    state = models.CharField(blank=True, max_length=20)  # Defining state field
    country = models.CharField(blank=True, max_length=20)  # Defining country field

    def __str__(self):
        return self.user.first_name  # Returning the first name of the user as string representation

    def full_address(self):
<<<<<<< Updated upstream
        return f'{self.address_line_1} {self.address_line_2}'  # Returning full address of the user

class Logo(models.Model):
    category_image = models.ImageField(upload_to='photos/logo', blank=True)  # Defining category image field
    created_at = models.DateTimeField(auto_now_add=True)  # Defining created at field
    updated_at = models.DateTimeField(auto_now=True)  # Defining updated at field
=======
        return f'{self.address_line_1} {self.address_line_2}'
>>>>>>> Stashed changes
