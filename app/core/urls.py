from django.urls import path
from . import views
from .models import User

urlpatterns = [
    path('', views.home, name="home"),
    path('services/', views.services, name="services" ),
    path('contacts/', views.contacts, name='contacts'),
    path('make_an_appointment/', views.make_an_appointment, name='appointment'),
    path('about_us/', views.about_us, name='about_us'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('adminPage/', views.adminPage, name='adminPage'),
    path('user_list/', views.UserView.as_view(), name='user_list'),
    path('updateUser/<str:pk>/',views.updateUser,name='updateUser'),
    path('register_patient/', views.PatientRegister.as_view(), name='register_patient'),
    path('register_doctor', views.DoctorRegister.as_view(), name='register_doctor'),
]