from django.shortcuts import render
from django.http import HttpResponse

def home(request):
     return render(request, 'homepage.html', {})

def signup(request):
     return render(request,'signup.html')

def login(request):
     return render(request,'login.html')