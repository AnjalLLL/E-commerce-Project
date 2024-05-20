from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.template import loader
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django import forms

def home(request):
  products = Products.objects.all()
  context = {'products': products}
  return render(request,"home.html")

def signup(request):
  if request.method == "POST":
    full_name = request.POST.get("name")
    email = request.POST.get("email")
    gender = request.POST.get("Gender")
    address = request.POST.get("address")
    phone = request.POST.get("phone")
    pass1 = request.POST.get("password1")
    password = request.POST.get("password2")

    if pass1 == password:
     
      new_user = UserDetails(full_name=full_name,email=email,gender=gender,address=address,phone=phone,password=password)
      new_user.save()
      
      return redirect("dashboard")
    else:
       raise forms.ValidationError("Passwords don't match")
  else:
    return render(request,'signup.html')

 

def signin(request):
  if request.method == "POST":
    email = request.POST.get('email')
    password = request.POST.get("password")
    print(email,password)
    User = authenticate(request,email=email,password=password)
    if User is not None:
       login(request,User)
       return redirect("dashboard")  
          
  return render(request,"sign-in.html")

def termsandcondition(request):
  return render(request,"termsandcondition.html")

def about(request):
  return render(request,"about.html")

def disclaimer(request):
  return render(request,"disclaimer.html")


def privacy_policy(request):
  return render(request,"privacy_policy.html")

#after sign in 

def dashboard(request):
  return render(request,"dashboard.html")

def cart(request):
  return render(request,"cart.html")

def buying(request):
  return render(request,"product-buying.html")



