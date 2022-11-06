import email
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Doctor, User, Patient
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .forms import UserCreateForm, UserForm, PatientCreateForm,DoctorCreateForm,DoctorForm,PatientForm
from django.db.models import Q
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.admin.views.decorators import staff_member_required    





def loginPage(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = get_user_model().objects.get(email=email)
        except:
            messages.error(request, "User does not exist")
        
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            if user.is_staff:
                return render(request, 'admin_page.html', context)
            return redirect('home')
        else:
            messages.error(request, "Username OR Password does not exist")

    
    return render(request, 'login_page.html', context)





def logoutUser(request):
    logout(request)
    return redirect('home')

def registerUser(request):
    form = UserCreateForm()
    email = request.POST.get('email')
    password = request.POST.get('password')
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            return redirect('adminPage')
    return render(request, 'register.html', {'form':form})  



class PatientRegister(UserPassesTestMixin, CreateView):

    def test_func(self):
        return self.request.user.is_staff

    model = User
    form_class = PatientCreateForm
    template_name = 'register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'patient'
        return super().get_context_data(**kwargs)

    def form_valid(self, form): 
        user = form.save()
        return redirect('adminPage')


    




class DoctorRegister(UserPassesTestMixin, CreateView):


    def test_func(self):
        return self.request.user.is_staff


    model = User
    form_class = DoctorCreateForm
    template_name = 'register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'doctor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('adminPage')


   





@staff_member_required
def adminPage(request):
    """Admin page"""
    
    if not request.user.is_staff:
        return HttpResponse("You are not staff")

    return render(request, 'admin_page.html')
    



class UserView(UserPassesTestMixin, ListView):

    def test_func(self):
        return self.request.user.is_staff
    model = User
    template_name = 'user_list.html'


    



def updateUser(request, pk):

    if not request.user.is_staff:
        return HttpResponse("This page does not exist")


    user = User.objects.get(email=pk)
    extra_form = None
    if user.is_doctor and (not user.is_staff):
        doctor = Doctor.objects.get(user=user)
        extra_form = DoctorForm(request.POST or None, instance=doctor)
        user_form = UserForm(request.POST or None, instance=user)
    elif user.is_staff:
        user_form = UserForm(request.POST or None, instance=user)
    else:
        patient = Patient.objects.get(user=user)
        extra_form = PatientForm(request.POST or None, instance=patient)
        user_form = UserForm(request.POST or None, instance=user)

    if request.method=='POST':
        
        if user.is_doctor and (not user.is_staff):
            if extra_form.is_valid and user_form.is_valid:
                extra_form.save()
                user_form.save()
                return redirect('adminPage')
        elif user.is_staff:
            if user_form.is_valid:
                user_form.save()
                return redirect('adminPage')
        else:
            if extra_form.is_valid and user_form.is_valid:
                extra_form.save()
                user_form.save()
                return redirect('adminPage')

    context = {'user_form':user_form, 'extra_form':extra_form}
    return render(request, 'user_form.html', context)
















def home(request):
    return render(request,'home.html')

def adminPage(request):
    return render(request, 'admin_page.html')

def services(request):
    return render(request, 'services.html')

def contacts(request):
    return render(request, 'contacts.html')

def make_an_appointment(request):
    return render(request, 'make_an_appointment.html')

def about_us(request):
    return render(request, 'about_us.html')
