from django.shortcuts import render,redirect
from .models import Article,Member

# Create your views here.
def index(request):
    return render(request,'siteapp\index.html')

def article(request):
    articles=Article.objects.all()
    context={
        'articles':articles
    }
    return render(request,'siteapp\Article.html',context)
  


def member(request):
    members=Member.objects.all()
    # members=Member.objects.get(name="raj")
    context={
        'members':members
    }
    return render (request,'siteapp\member.html',context)

def addarticle(request):
    members=Member.objects.all()
    context={
        'members':members
    }
    if request.method=='POST':
        title=request.POST.get('title')
        description=request.POST.get('description')
        authorid=request.POST.get('authorid')
        files=request.FILES
        image=files.get("image")
        author=Member.objects.get(id=authorid)
        ins=Article(title=title,description=description,image=image,author=author)
        ins.save()
        return render(request, 'siteapp:index')
    else:
        return render(request,'siteapp/Addarticle.html',context)    

def detail(request,id):
    article=Article.objects.filter(id=id).first()
    context={
        'article':article
    }
    return render(request,'siteapp/detail.html',context)

def addmember(request):
    if request.method=='POST':
        n=request.POST.get('name')
        d=request.POST.get('explain')
        a=request.POST.get('age')
        f=request.FILES
        image=f.get("image")

        a=Member(name=n,desc=d,age=a,image=image)
        a.save()
        return render(request, 'siteapp\index.html')
    else:
        return render(request,'siteapp\Addmember.html')    

def detail(request,id):
    m=Member.objects.filter(id=id).first()
    context={
        'members':m
    }
    return render(request,'siteapp\detail.html',context)
