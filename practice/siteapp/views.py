from django.shortcuts import render
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
    #members=Members.objects.get(name="raj")
    context={
        'members':members
    }
    return render (request,'siteapp\member.html',context)

def detail(request,id):
    article=Article.objects.filter(id=id).first()
    context={
        'article':article
    }
    return render(request,'siteapp\detail.html',context)
    