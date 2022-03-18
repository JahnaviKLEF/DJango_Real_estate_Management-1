from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('home/', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('about', views.aboutus, name='about'),
    path('services', views.services, name='services'),
    path('Apartment', views.Apartment, name='Apartment'),
    path('Profile', views.Profile, name='Profile'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('changepassword', views.changepassword, name='changepassword'),
    path('checkout', views.checkout, name='checkout'),
    
    path('contact', views.contact, name='contact'),
    path('reset_password', auth_views.PasswordResetView.as_view(), name='reset_password'),
    
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
]
