from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def home(request):
  return render(request,"home.html")

def signup(request):
  return render(request,"signup.html")

def signin(request):
  return render(request,"sign-in.html")

def termsandcondition(request):
  return render(request,"termsandcondition.html")

def about(request):
  return render(request,"about.html")

def disclaimer(request):
  return render(request,"disclaimer.html")


def privacy_policy(request):
  return render(request,"privacy_policy.html")


