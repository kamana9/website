from django.urls import path,include
from .views import new,register

urlpatterns =[
    path('new/',new,name="new"),
    path('register/',register,name="register")
]