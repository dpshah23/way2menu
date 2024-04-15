import flask
from flask import *
import pyrebase
import datetime
import random

# App Initialization
app=Flask(__name__)

# Firebase Auth And Database Initialization
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


@app.route('/login',methods=["POST","GET"])
def login():
    output = {'auth': False}
    try:
        if request.method=="POST":
           email=request.form.get('email')
           password=request.form.get('password')

           print(email,password)

           auth1=auth.sign_in_with_email_and_password(email,password)
           print(auth1)

           
           output={
               
               'auth': True,
           }


    except Exception as e:
        
        print(e)
       
       

    finally:
        return jsonify(output)
    
@app.route('/getmenu',methods=['GET'])
def menu():
    email="way2menu1@gmail.com"
    password="way2menu@2172987539319"
    auth=firebase.auth()
    user=auth.sign_in_with_email_and_password(email,password)
    restaurant_name=request.args.get('restaurantnm')
    tableno=request.args.get('tableno')
    restaurant_id=request.args.get('restaurant_id')
    menu_ref = db.child("menus")
    menu_snapshot = menu_ref.child(restaurant_id).get(token=user['idToken'])
    menu_data = menu_snapshot.val()


    return jsonify(menu_data)

@app.route('/addmenu',methods=['GET','POST'])
def addmenu():
    if Request.method=="POST":
        email="way2menu1@gmail.com"
        password="way2menu@2172987539319"
        auth=firebase.auth()
        user=auth.sign_in_with_email_and_password(email,password)
        restaurant_id=request.form.get('restaurant_id')
        restaurnant_name=request.GET['restaurant_name']
        title=request.form.get('title')
        desc=request.form.get('desc')
        price=request.form.get('price')
        imgurl=request.form.get('imgurl')
        isspecial=request.form.get('isspecial')

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

    return jsonify(data)

    
if __name__=="__main__":
    app.run(debug=True)