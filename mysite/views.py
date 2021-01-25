from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')

def contact(request):
    return render(request,'contact-us.html')

# def shop(request):
#     return render(request,'shop.html')

# def cart(request):
#     return render(request,'cart.html')

# def account(request):
#     return render(request,'my-account.html')

# def login(request):
#     return render(request,'login.html')

# def Signup(request):
#     return render(request,'signup.html')