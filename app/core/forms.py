from datetime import date, datetime
from email.policy import default
from django.forms import ModelForm
from .models import User, Patient, Doctor
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm
from django.core.validators import RegexValidator
from django.db import transaction


user = get_user_model

class UserCreateForm(UserCreationForm):
    """
    Create user form
    """

    class Meta:
        model = User
        fields = ('email', 'birth_date', 'contact_number', 'id_number', 'iin_number', 'first_name', 'middle_name', 'last_name', 
                    'address', 'marital_status')

class UserForm(ModelForm):
    """
    User Form
    """

    class Meta:
        model = User
        fields = ('email', 'birth_date', 'contact_number', 'id_number', 'iin_number', 'first_name', 'middle_name', 'last_name', 
                    'address', 'marital_status')




CHOICES = (('A-','A-'),('A+','A+'),('AB+','AB+'),('AB-','AB-'),('O-','O-'),('O+','O+'))

class PatientCreateForm(UserCreateForm):
    """
    Patient Creation Form
    """
    blood_group = forms.MultipleChoiceField(required=True, choices=CHOICES)
    emergency_phone_number = forms.CharField()
    registration_date = forms.DateTimeField()
  

    class Meta(UserCreateForm.Meta):
        model = User
        fields = ('email', 'birth_date', 'contact_number', 'id_number', 'iin_number', 'first_name', 'middle_name', 'last_name', 
                   'address', 'marital_status','blood_group','emergency_phone_number','password1', 'password2')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_doctor=False
        user.save()
        data = self.cleaned_data
        patient = Patient.objects.create(user=user)
        patient.emergency_phone_number = data['emergency_phone_number']
        patient.blood_group = data['blood_group']
        patient.registration_date = datetime.now()
        patient.save() 
        return patient
    
class DoctorCreateForm(UserCreateForm):

    
    department_id = forms.CharField(max_length=100)
    experience = forms.IntegerField()
    category = forms.CharField(max_length=100)
    price_of_the_appointement = forms.IntegerField()
    degree = forms.CharField(max_length=100)
    rating = forms.IntegerField()
    available_days = forms.CharField( max_length=100)
    profile_photo = forms.ImageField(required=False)




    class Meta(UserCreateForm.Meta):
        model = User
        fields=('email', 'birth_date', 'contact_number', 'id_number', 'iin_number', 'first_name', 'middle_name', 'last_name', 'profile_photo',
                    'address', 'marital_status', 'department_id', 'experience', 'category', 'price_of_the_appointement','degree',
                    'rating','available_days','password1','password2')
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_doctor = True
        user.save()
        data = self.cleaned_data
        doctor = Doctor.objects.create(user=user, profile_photo=data['profile_photo'], department_id=data['department_id'], experience = data['experience'], category = data['category'],
        price_of_the_appointement = data['price_of_the_appointement'], degree = data['degree'],rating = data['rating'],available_days = data['available_days'])

        return doctor

       
class DoctorForm(ModelForm):
    """
    Doctor Form
    """

    class Meta:
        model = Doctor
        fields = ('profile_photo', 'department_id', 'experience', 'category', 'price_of_the_appointement','degree',
                    'rating','available_days',)
    
class PatientForm(ModelForm):
    """
    Patient Form
    """

    class Meta:
        model = Patient
        fields = ('blood_group','emergency_phone_number')
       