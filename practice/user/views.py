from django.shortcuts import render
from .models import Student,Teacher
from .forms import StudentForm,TeacherForm

def new(request):
    context={}
    form=StudentForm(request.POST)

    if form.is_valid():
        form.save()

    context['form']=form

    return render(request,"user/login.html",context)

def register(request):
    context={}
    form=TeacherForm(request.POST)

    if form.is_valid():
        form.save()

    context['form']=form

    return render(request,"user/register.html",context)
