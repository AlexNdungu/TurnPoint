from django.shortcuts import render

# Create your views here.

#The Intoduction Page
def Intro(request):
    return render(request, 'Intro.html')

#The Inheriting Page
def Inherit(request):
    return render(request,'inherit.html')    

#The Preaching page
def Preach(request):
    return render(request, 'preach.html')   

#The Presentation page
def Present(request):
    return render(request, 'present.html')   

#The Contact Page 
def Contact(request):
    return render(request, 'contact.html')      

#The Offering And Tithe page
def Offer(request):
    return render(request, 'offer.html')   

#The Register page
def Register(request):
    return render(request, 'register.html')    

#The Login page
def Login(request):
    return render(request, 'login.html')        

#The Admin Inheritance page
def AdmInh(request):
    return render(request, 'Admin/inherAd.html')      

#The Dashboard page
def Dashboard(request):
    return render(request, 'Admin/dash.html')    