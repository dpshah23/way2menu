from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import pyrebase
from rest_framework.decorators import *
import json
from rest_framework.authentication import TokenAuthentication
import secrets
from rest_framework.permissions import IsAuthenticated
import datetime
import random

# Create your views here.

from rest_framework.parsers import BaseParser

class PlainTextParser(BaseParser):
    media_type = 'text/plain'

    def parse(self, stream, media_type=None, parser_context=None):
        text = stream.read().decode('utf-8')
        return text


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
    print("hello")
   
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
    restaurant_name=request.GET['restaurantnm']
    tableno=request.GET['tableno']
    restaurant_id=request.GET['restaurant_id']
    menu_ref = db.child("menus")
    menu_snapshot = menu_ref.child(restaurant_id).get(token=user['idToken'])
    menu_data = menu_snapshot.val()


    return JsonResponse(menu_data)


@api_view(['GET'])
def addmenu(request):
    email="way2menu1@gmail.com"
    password="way2menu@2172987539319"
    auth=firebase.auth()
    user=auth.sign_in_with_email_and_password(email,password)
    restaurant_id=request.GET['restaurant_id']
    restaurnant_name=request.GET['restaurant_name']
    title=request.GET['title']
    desc=request.GET['desc']
    price=request.GET['price']
    imgurl=request.GET['imgurl']
    isspecial=request.GET['isspecial']

    data={
        "title":title,
        "description":desc,
        "price":price,
        "imgurl":imgurl,
        "special":isspecial
    }

    db=firebase.database()

    addmenudata=db.child('menus').child(restaurant_id).child(title).set(data,token=user['idToken'])

    data={
        'pushed':True,
        'title':title,
    }

    return JsonResponse(data)


@api_view(['POST'])
def add_restaurant(request):
    restaurant_name=request.get('restaurant_name')
    address=request.get('address')
    mobile=request.get('mobile')
    range=request.get('range')
    time=datetime.datetime.now()
    gstno=request.get('gstno')
    restaurant_id=random.randint(00000,99999)
    email=request.get('email')
    password=request.get('password')
    active=request.get('active')
    owner_name=request.get('owner_name')
    owner_age=request.get('owner_age')
    gender=request.get('owner_gender')
    time=str(time)

    data={
        'restaurant_name':restaurant_name,
        'address':address,
        "mobile":mobile,
        "range":range,
        "gstno":gstno,
        "email":email,
        "password":password,
        "active":active,
        "time":time,
        "owner_name":owner_name,
        "owner_age":owner_age,
        "gender":gender
        
    }
    userstatus=False
    if active==True:
        auth=firebase.auth()
        createuser=auth.create_user_with_email_and_password(email,password)
        userstatus=True

    email="way2menu1@gmail.com"
    password="way2menu@2172987539319"
    auth=firebase.auth()
    user=auth.sign_in_with_email_and_password(email,password)
    db=firebase.database()
    data_pushed=db.child("restaurant").child(restaurant_id).set(data,token=user['idToken'])
    data={
        "pushed":True,
        'active':active,
        'user_created':userstatus
    }

    return JsonResponse(data)
