from django.urls import path
from .views import *
urlpatterns = [
    path('login/',login,name='login'),
    path('signup',signup,name="signup"),
    path('getmenu',menu,name="getmenu"),
    path('addmenu',addmenu,name="addmenu"),
    path('addrestaurant',add_restaurant,name="add_restaurant"),
    path('getorders',retriveorders,name="getorders"),
    path('getresinfo',resinfo,name="getresinfo")
    
]
