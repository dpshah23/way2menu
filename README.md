# Restaurant Management System


Restaurant Booking System API
This is a Django REST Framework API for a restaurant booking system.

Setup
Install the required packages listed in requirements.txt.

Copy Code
```bash

pip install -r requirements.txt
```

Configure Firebase settings in settings.py:

python
```bash
Copy code
config = {
    'apiKey': "<YOUR_API_KEY>",
    'authDomain': "<YOUR_AUTH_DOMAIN>",
    'projectId': "<YOUR_PROJECT_ID>",
    'storageBucket': "<YOUR_STORAGE_BUCKET>",
    'databaseURL': "<YOUR_DATABASE_URL>",
    'messagingSenderId': "<YOUR_MESSAGING_SENDER_ID>",
    'appId': "<YOUR_APP_ID>",
    'measurementId': "<YOUR_MEASUREMENT_ID>"
}
```
Start the Django development server:

```bash
Copy code
python manage.py runserver
```
API Endpoints
1. /login
Method: POST
Description: Authenticate user login using email and password.
Request Body: JSON
json
Copy code
{
    "email": "user@example.com",
    "password": "password123"
}
Response: JSON
json
Copy code
{
    "auth": true
}
2. /signup
Method: GET
Description: Register a new user.
Request Parameters: email, password
3. /menu
Method: GET
Description: Retrieve menu data for a restaurant.
Request Parameters: restaurantnm, tableno, restaurant_id
Response: JSON (menu data)
4. /addmenu
Method: GET
Description: Add a new menu item.
Request Parameters: restaurant_id, restaurant_name, title, desc, price, imgurl, isspecial
Response: JSON (confirmation)
5. /add_restaurant
Method: GET
Description: Add a new restaurant.
Request Parameters: restaurant_name, address, mobile, range, gstno, email, password, active
Response: JSON (confirmation)


Feel free to expand this README with more details as needed and include any additional sections relevant to your project.





