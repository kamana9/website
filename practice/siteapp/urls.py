from django.urls import path,include
from .views import index,article,member,detail,addarticle,addmember


urlpatterns = [
    path('',index,name="index"),
    path('article/',article,name="article"),
    path('member/',member,name="member"),
    path('detail/<int:id>/',detail,name="detail"),
    path('addarticle/',addarticle,name="addarticle"),
    path('addmember/',addmember,name="addmember"),
]
