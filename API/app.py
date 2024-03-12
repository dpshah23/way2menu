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
    'measurementId': "G-8Y2N8BGR7J"
}

# firebase=pyrebase.initialize_app(config=config)
app=Flask(__name__)

@app.route('/',methods=["POST","GET"])
def index():
    return "hello world"

if __name__=="__main__":
    app.run(debug=True)