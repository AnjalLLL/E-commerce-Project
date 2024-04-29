from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def home(request):
  return render(request,"home.html")

def signup(request):
  return render(request,"signup.html")

def signin(request):
  return render(request,"sign-in.html")