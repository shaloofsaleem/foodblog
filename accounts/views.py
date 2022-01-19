
from django.contrib.auth import authenticate
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User

# Create your views here.

def register(request):
    if request.method=="POST":
        username=request.POST['username']
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['pwd']
        password2=request.POST['confirm']

        myuser=User.objects.create_user(username,email,password)
        myuser.save()
        myuser.first_name=name

        messages.success(request,"your Accout has been created")
        return redirect('login')
    return render(request,'register.html')





def login(request):
    if request.method =="post":
        username=request.POST['username']
        password=request.POST['pwd']
        authenticate(username=username,password=password)



    return render(request,'login.html')    