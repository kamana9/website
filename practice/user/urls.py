from django.urls import path,include
from .views import new,teacher,register,login_page,logout_view

urlpatterns =[
    path('new/',new,name="new"),
    path('register/',register,name="register"),
    path('teacher/',teacher,name="teacher"),
    path('login_page/',login_page,name="login_page"),
    path('logout/',logout_view,name="logout")
]