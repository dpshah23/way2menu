from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import pyrebase
from rest_framework.decorators import *
import json

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

@api_view(['GET','POST'])
def login(request):
    
    try:
        if request.method=="POST":
           data=request.data
        #    data_dict = json.loads(data)
           
           email = data[0][0]
           password = data[0][1]

           print(email,password)

           auth1=auth.sign_in_with_email_and_password(email,password)
           print(auth1)

           output={
               'auth': True,
           }


    except Exception as e:
        print(e)
        output={
            'auth':False
        }

    finally:
        return JsonResponse(output)