from django.shortcuts import render,redirect
from .models import Student,Teacher
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login,authenticate,logout
from .forms import StudentForm,TeacherForm

def new(request):
    context={}
    form=StudentForm(request.POST)

    if form.is_valid():
        form.save()

    context['form']=form

    return render(request,"user/student.html",context)

def teacher(request):
    context={}
    form=TeacherForm(request.POST)

    if form.is_valid():
        form.save()

    context['form']=form

    return render(request,"user/teacher.html",context)

def register(request):
    if request.user.is_authenticated:
        return redirect('siteapp:index')
    if request.method=='POST':
        errors={}
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm=request.POST.get('confirm_password')

        if password!=confirm:
            errors['password']='Password and confirm password dont match'

        existingemail=User.objects.filter(email=email).first()
        if existingemail:
            errors['email']='Email already exists'
        

        existinguser=User.objects.filter(username=username).first()
        if existinguser:
            errors['username']='Username already exists'



        if len(errors)>0:
            return render(request,'user/register.html',context={'errors':errors})
        else:
            hashed_password=make_password(password)
            user=User(username=username,email=email,password=hashed_password)
            user.save()
            return redirect('siteapp:index')
    else:
        return render(request, "user/register.html")      

def login_page(request):
    if request.user.is_authenticated:
        return redirect('siteapp:index')

    if request.method=="POST":
        errors={}
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username)
        hashed_password=make_password(password)

        user=authenticate(request, username=username,password=hashed_password)
        if user is not None:
            login(request,user)
            return redirect('siteapp:index')
        else:
            errors['top']='Wrong credentials'
            return render(request,'user/login.html',context={'errors':errors})

    else:
        return render(request,'user/login.html')

def logout_view(request):
    logout(request)
    return redirect('siteapp:index')