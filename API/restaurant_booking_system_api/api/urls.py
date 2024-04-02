from django.urls import path
from .views import *
urlpatterns = [
    path('login/',login,name='login'),
    path('getmenu',menu,name="getmenu"),
    path('addmenu',addmenu,name="addmenu"),
    path('signup/',add_restaurant,name="add_restaurant"),
    path('getorders',retriveorders,name="getorders"),
    path('getresinfo',resinfo,name="getresinfo")
    
]
