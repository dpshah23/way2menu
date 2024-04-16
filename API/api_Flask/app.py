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


@app.route('/signup',methods=['POST','GET'])
def add_restaurant():
    if Request.method=="POST":
        restaurant_name=request.form.get('restaurant_name')
        address=request.form.get('address')
        mobile=request.form.get('mobile')
        range=request.form.get('range')
        time=datetime.datetime.now()
        gstno=request.form.get('gstno')
        restaurant_id=random.randint(00000,99999)
        email=request.form.get('email')
        password=request.form.get('password')
        active=request.form.get('active')
        owner_name=request.form.get('owner_name')
        owner_age=request.form.get('owner_age')
        gender=request.form.get('owner_gender')
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

    return jsonify(data)

@app.route('/getorders',methods=['GET'])
def retriveorders():
    email="way2menu1@gmail.com"
    password="way2menu@2172987539319"

    user=auth.sign_in_with_email_and_password(email,password)
    id=request.args.get('restaurant_id')
    name=request.args.get('restaurant_name')
    print(name)
    print(id)
    id=int(id)
    ref=db.child('Orders')
    orders=ref.child(id).get(token=user['idToken'])
    print(orders)
    orders_data=orders.val()
    print(orders_data)
    if orders_data:
        
        return jsonify(orders_data, safe=False)
    else:
       
        return jsonify({"error": "No data found for the specified restaurant ID"}, status=404)


@app.route('/getresinfo',methods=['GET'])
def getresinfo():
    email="way2menu1@gmail.com"
    password="way2menu@2172987539319"
    auth=firebase.auth()
    user=auth.sign_in_with_email_and_password(email,password)

    restaurant_id=request.args.get('restaurant_id')
    orders=db.child('Orders').child(restaurant_id).get(user['idToken'])
    orders_data=orders.val()
    orders_length=len(orders_data)
    total_price=0

    for key in orders_data:
        order=orders_data[key]
        if 'price' in order:
            total_price+=order['price']

        else:
            pass

    jsonpass={
        'total_orders':orders_length,
        'total_price':total_price
    }

    return jsonify(jsonpass)


    
if __name__=="__main__":
    app.run(debug=True)