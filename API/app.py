import flask
from flask import *
import pyrebase

config={
    'apiKey': "AIzaSyCxSm5xlUi-gYrHNh7DqQTzwuKFbOexGRo",
    'authDomain': "way2menu-cc380.firebaseapp.com",
    'projectId': "way2menu-cc380",
    'storageBucket': "way2menu-cc380.appspot.com",
    'messagingSenderId': "7445769295",
    'appId': "1:7445769295:web:42be734ec3137d2ad94e3a",
    'measurementId': "G-8Y2N8BGR7J",
    'databaseURL':'https://way2menu-cc380-default-rtdb.asia-southeast1.firebasedatabase.app/',
}

firebase=pyrebase.initialize_app(config=config)
db=firebase.database()
auth=firebase.auth()

app=Flask(__name__)

@app.route('/login',methods=["POST","GET"])
def login():
    email=request.args.get('email')
    password=request.args.get('password')
    try:
        op=auth.sign_in_with_email_and_password(email,password)
        print(op)
    
        data={
            'auth':True
        }

    
    except Exception as e:
        data={
            'auth':False
        }
    return jsonify(data)
    


if __name__=="__main__":
    app.run(debug=True)