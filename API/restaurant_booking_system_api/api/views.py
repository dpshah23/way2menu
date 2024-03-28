from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import pyrebase
from rest_framework.decorators import *
import json
from rest_framework.authentication import TokenAuthentication
import secrets
from rest_framework.permissions import IsAuthenticated


# Create your views here.

config={
    'apiKey': "AIzaSyCxSm5xlUi-gYrHNh7DqQTzwuKFbOexGRo",
    'authDomain': "way2menu-cc380.firebaseapp.com",
    'projectId': "way2menu-cc380",
    'storageBucket': "way2menu-cc380.appspot.com",
    'databaseURL':'https://way2menu-cc380-default-rtdb.asia-southeast1.firebasedatabase.app/',
    'messagingSenderId': "7445769295",
    'appId': "1:7445769295:web:42be734ec3137d2ad94e3a",
    'measurementId': "G-8Y2N8BGR7J"
}

firebase=pyrebase.initialize_app(config=config)
db=firebase.database()
auth=firebase.auth()

@api_view(['POST'])

def login(request):
   
    output = {'auth': False}
    
    try:
        if request.method=="POST":
           email=request.data.get('email')
           password=request.data.get('password')

           print(email,password)

           auth1=auth.sign_in_with_email_and_password(email,password)
           print(auth1)

           
           output={
               
               'auth': True,
           }


    except Exception as e:
        
        print(e)
       
       

    finally:
        return JsonResponse (output)

@api_view(['GET'])
def signup(request):
    if request.method=='GET':
        email=request.get('email')
        password=request.get('password')


    pass


@api_view(['GET'])
def menu(request):
    email="way2menu1@gmail.com"
    password="way2menu@2172987539319"
    auth=firebase.auth()
    user=auth.sign_in_with_email_and_password(email,password)
    restaurant_name=request.get('restaurantnm')
    tableno=request.get('tableno')
    restaurant_id=request.get('restaurant_id')
    menu= db.child("menus").child('restaurant_id').order_by_child("restaurant_id").equal_to(restaurant_id).get(token=user['idToken'])
    data=menu.val()


    return JsonResponse(data)


@api_view(['GET'])
def addmenu(request):
    email="way2menu1@gmail.com"
    password="way2menu@2172987539319"
    auth=firebase.auth()
    user=auth.sign_in_with_email_and_password(email,password)
    restaurant_id=request.get('restaurant_id')
    restaurnant_name=request.get('restaurant_name')
    title=request.get('title')
    desc=request.get('desc')
    price=request.get('price')
    imgurl=request.get('imgurl')
    isspecial=request.get('isspecial')

    data={
        "title":title,
        "description":desc,
        "price":price,
        "imgurl":imgurl,
        "special":isspecial
    }

    db=firebase.database()

    addmenudata=db.child('menus').child(restaurant_id).child(title).set(data,token=user['idToken'])


@api_view(['GET'])
def add_restaurant(request):
    pass
