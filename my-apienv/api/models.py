from flask import Flask, render_template, flash, request,redirect, url_for, jsonify, make_response
from werkzeug.security import generate_password_hash,check_password_hash
import uuid


# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

k = []  #Review list
class User():
    def __init__(self):
        self.Allusers=[]
    
    def add_user(self):
        data = request.get_json()
        hashed_password = generate_password_hash(data["password"], method="sha256")
        new_user={ "id":str(uuid.uuid4()), "name":data["name"],"password":hashed_password}
        self.Allusers.append(new_user)


class Business():
    def __init__(self):
        self.business=[{
            "id" : "1",
            "name":"Airtel",
            "category":"Telecommunication",
            "location":"Bugolobi"
        },
        {
            "id" : "2",
            "name":"Global",
            "category":"Transport",
            "location":"Kireka"
        }]

    def add_business(self):
        data = request.get_json()
        new_business={ "id":str(uuid.uuid4()), "name":data["name"],"category":data["category"],"location":data["location"]}
        self.business.append(new_business)  

if __name__ == "__main__":
    app.run()