

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
    )
from django.core.validators import RegexValidator







class UserManager(BaseUserManager):
    """Manager for User"""
    def create_user(self, email, password=None, **extra_fields):
        """Create, save, and return a new user"""
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password):
        """Create new superuser."""
        user = self.create_user(email, password)
        user.is_doctor = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        
        return user






class User(AbstractBaseUser, PermissionsMixin):
    """The user model."""

    
    email = models.EmailField(max_length=100, unique=True,primary_key=True)
    birth_date = models.DateField(null=True)
    id_number = models.CharField(unique=True,null=True, max_length=100)
    iin_number = models.CharField(unique=True,null=True, max_length=100)
    is_staff = models.BooleanField(default=False)
    address = models.CharField(max_length=250)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_doctor = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False) 
    is_active = models.BooleanField(default=True)
    contact_number = models.CharField(validators = [RegexValidator(regex = r"^\+?1?\d{8,15}$")], max_length = 12, unique = True, default='+7')
    marital_status = models.CharField(max_length=25)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    

class Patient(models.Model):
    """
    The patient model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    blood_group = models.CharField(max_length=250,null=True)
    emergency_phone_number = models.CharField(validators = [RegexValidator(regex = r"^\+?1?\d{8,15}$")], max_length = 12, default='+7')
    registration_date = models.DateTimeField(null=True)

    #def __init__(self,user,blood_group,emergency_phone_number,registration_date):
       # self.user = user
      #  self.blood_group = blood_group
      #  self.emergency_phone_number = emergency_phone_number
      ##  self.super().save(using=self._db)



    def __str__(self):
        return self.user.email

class Doctor(models.Model):
    """
    The doctor model
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    department_id = models.CharField(max_length=100)
    experience = models.IntegerField()
    category = models.CharField(max_length=100)
    price_of_the_appointement = models.IntegerField()
    degree = models.CharField(max_length=100)
    rating = models.IntegerField()
    profile_photo = models.ImageField(null=True, default='image.profile.png')
    available_days = models.CharField(null=True, max_length=100)                                    

    def __str__(self):
        return self.user.email
     









"""
class Appointment(models.Model):
    The appointment of the patient
    patient = models.ForeignKey(User,related_name='patient',on_delete=models.CASCADE)
    doctor = models.ForeignKey(User,related_name='doctor',on_delete=models.CASCADE, null=True)
    service = models.CharField(max_length=250)
    date = models.DateTimeField()
    status = models.CharField(default='pending',blank=True,max_length=25)


    def make_an_appointment(self, patient, doctor, service, date):
        if patient==None or doctor==None:
            raise ValueError('Users must be present') 
        self.patient = patient
        self.doctor = doctor
        self.service = service
        self.date = date


        return self

    def approve_appointment(self, status=False):
        if status is True:
            self.status = 'approved'
        else:
            self.status = 'rejected'
        return self
    
    def __str__(self):
        return 'Appointment of the {self.patient.email}'

 """




    


    

    
    
   