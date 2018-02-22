from flask import Flask, render_template, flash, request,redirect, url_for, jsonify, make_response, abort
from werkzeug.security import generate_password_hash,check_password_hash
import uuid
from api.models import User, Business

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

k = []  #Review list

@app.route('/api/v1/auth/register', methods=['POST'])
def register():
    x=User()
    x.add_user()
    p = jsonify({"User created and added to list":x.Allusers})
    p.status.code=200
    return p

@app.route('/api/auth/login' , methods=['POST'])
def login():
    y=[{ "id":1, "name":"john","password":123}]
    data = request.get_json()
    for i in y:
        if i["name"]==data["name"] and i["password"]==data["password"]:
            p=jsonify({"Message":"User is logged in"})
            p.status.code=200
            return p
                    
@app.route('/api/v1/auth/logout', methods=['POST'])
def logout():
    p=jsonify({"Message":"User has been logged out"})
    p.status.code=200
    return p


@app.route('/api/v1/auth/reset-password', methods=['POST'])
def resetpassword():
    x=[{ "id":1, "name":"john","password":123}]
    data = request.get_json()
    for i in x:
        if i ["name"]==data["name"]:
            i["password"]=data["password"]
            p = jsonify({"Password has been reset"})
            p.status.code=200
            return p

@app.route('/api/v1/businesses/<int:businessId>', methods=['PUT'])
def buzupdate(businessId):
    b=[{
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
    data = request.get_json()

    for i in b:
        if i["id"] == businessId :
            i["name"]=data["name"]
            i["category"]=data["category"]
            i["location"]=data["location"]
            p = jsonify({"Business has been updated":b})
            p.status.code=200
            return p
             
@app.route('/api/v1/businesses/<int:businessId>', methods=['DELETE'])
def buzremove(businessId):
    b=[{
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
   
    for i in b:
        if i["id"]== businessId :
            b.remove(i)
            p=jsonify({"Message":"The Business has been deleted"})
            p.status.code=200
            return p



@app.route('/api/v1/businesses', methods=['GET'])
def Allbuz():
    b=Business()
    p=jsonify({"A list of all businesses":b.business})
    p.status.code=200
    return p


@app.route('/api/v1/businesses/<int:businessId>', methods=['GET'])
def Onebuz(businessId):
    b=[{
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
    for i in b:
        if i["id"]== businessId :    
            z=i
            p=jsonify({"Business":z})
            p.status.code=200
            return p

@app.route('/api/v1/businesses/<int:businessId>/reviews', methods=['POST'])
def buzreviews(businessId):
    y=User()
    for i in y.Allusers:
            if i["id"]==businessId:
                data = request.get_json()
                new_review={"id":businessId ,"name":data["review"],"Review":data["review"]}
                k.append( new_review)

    
    p=jsonify({"Review has been added":k})
    p.status.code=200
    return p

@app.route('/api/v1/businesses/<int:businessId>/reviews', methods=['GET'])
def Onebuzreviews(businessId):
    
    p=jsonify({"All Reviews":k})
    p.status.code=200
    return p



if __name__ == "__main__":
    app.run()