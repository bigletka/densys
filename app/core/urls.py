from django.urls import path
from . import views
from .models import User

urlpatterns = [
    path('', views.home, name="home"),
    path('services/', views.services, name="services" ),
    path('contacts/', views.contacts, name='contacts'),
    path('make_an_appointment/', views.AppointmentCreateView.as_view(), name='appointment'),
    path('appointment_by_doctor/<str:email>/', views.AppointmentCreate, name='appointment_by_doctor'),
    path('about_us/', views.about_us, name='about_us'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('adminPage/', views.adminPage, name='adminPage'),
    path('user_list/', views.UserView.as_view(), name='user_list'),
    path('updateUser/<str:pk>/',views.updateUser,name='updateUser'),
    path('register_patient/', views.PatientRegister.as_view(), name='register_patient'),
    path('register_doctor', views.DoctorRegister.as_view(), name='register_doctor'),
    path('appointments/', views.AppointmentsList.as_view(), name='appointments'),
    path('appointment_update/<int:pk>/', views.updateAppointment, name='appointment_update'),
    path('appointments_pending/', views.AppointmentsPendingList.as_view(), name='appointment_pending'),
    path('doctor_list/', views.DoctorList.as_view(), name='doctor_list'),
]