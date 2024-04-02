import pyrebase
config={
    "apiKey": "AIzaSyCxSm5xlUi-gYrHNh7DqQTzwuKFbOexGRo",
    "authDomain": "way2menu-cc380.firebaseapp.com",
    "projectId": "way2menu-cc380",
    "storageBucket": "way2menu-cc380.appspot.com",
    "databaseURL":"https://way2menu-cc380-default-rtdb.asia-southeast1.firebasedatabase.app/",
    "messagingSenderId": "7445769295",
    "appId": "1:7445769295:web:42be734ec3137d2ad94e3a",
    "measurementId": "G-8Y2N8BGR7J"
}

firebase=pyrebase.initialize_app(config)

db=firebase.database()
auth=firebase.auth()
email="way2menu1@gmail.com"
password="way2menu@2172987539319"
auth=firebase.auth()
user=auth.sign_in_with_email_and_password(email,password)

orders=db.child('Orders').child(75275).get(user['idToken'])
orders_data=orders.val()
print(len(orders_data))
total_price=0

for key in orders_data:
    order=orders_data[key]
    if 'price' in order:
        total_price+=order['price']

    else:
        print("price Not found")

print("total price : ",total_price)

