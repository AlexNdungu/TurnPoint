from django.urls import path

#Import Views

from . import views

urlpatterns = [
    path('',views.Intro, name='intro'),

    #Inheritance page
    path('inherit/',views.Inherit, name='inherit'),

    #Preachings page
    path('Preachings/',views.Preach, name='preachings'),

    #Presentation page
    path('Presentation/',views.Present, name='presentation'),

    #Contact page
    path('Contact/',views.Contact, name='contact'),

    #Offerings page
    path('Offerings/',views.Offer, name='offerings'),

    #Register page
    path('Register/',views.Register, name='register'),

    #Login page
    path('Login/',views.Login, name='login'),


    #Admin Panel
    path('AdmInh/',views.AdmInh, name='admInh'),

    #Dashboard Panel
    path('Dashboard/',views.Dashboard, name='dashboard'),
]
