from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager
import uuid
import datetime
# Create your models here.
class MyAccountManger(BaseUserManager):
    def create_user(self, first_name, last_name , username , email, password = None):
        if not email:
            raise ValueError('Email Address is Mandatory!')
        
        if not username:
            raise ValueError('User must have a UserName!')


        user = self.model(
            email  = self.normalize_email(email),
            username  = username , 
            first_name  = first_name,
            last_name      = last_name,
        ) 

        user.set_password(password)
        user.save(using=self._db)
        return user
        
    
    def create_superuser(self, first_name , last_name, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name= last_name,
            password = password,
        )

        user.is_admin = True
        user.is_active = True 
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user
        
class Account(AbstractBaseUser):
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    username        = models.CharField(max_length=50, unique=True)
    email           = models.EmailField(max_length=100, unique=True)
    phone_number    = models.CharField(max_length=50)
    
    #required
    date_joined     = models.DateTimeField(auto_now_add=True)
    last_login      = models.DateTimeField(auto_now_add=True)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=False)
    is_superadmin   = models.BooleanField(default=False)

    
    
    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username','first_name', 'last_name']

    objects = MyAccountManger()
    
    
    def __str__(self):
        return self.email
    
    
    
    def has_perm(self, perm , obj=None):
        return self.is_admin
    
    
    
    def has_module_perms(self, add_label):
        return True


class Profile(models.Model):
    depart = models.ForeignKey('dashboard.Department', on_delete=models.CASCADE, blank=True,null=True)
    account = models.OneToOneField(Account , on_delete=models.CASCADE, blank=True , null=True)
    name = models.CharField(max_length=50,null=True,blank=True)
    salary  = models.DecimalField(decimal_places=2,max_digits=10,default = 0)
    username = models.CharField(max_length=50,null=True,blank=True)
    email = models.EmailField(blank=True,null=True)
    role = models.CharField(max_length=150,null=True,blank=True)
    location = models.CharField(max_length=50,null=True,blank=True)
    gender = models.CharField(max_length=50,null=True,blank=True)
    age = models.IntegerField(default = 0)
    on_vacation = models.BooleanField(default=False)
    skills = models.CharField(max_length=255,null=True,blank=True)
    languages = models.CharField(max_length=50,null=True,blank=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False,primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return str(self.username)

    @property
    def imageURL(self):
        try:
            url = self.profile_image.url
        except:
            url = '/images/user-default.png'
        return url
    
    class Meta:
        ordering = ['-created']


