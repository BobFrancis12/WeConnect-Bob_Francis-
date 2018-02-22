from flask import Flask, render_template, flash, request,redirect, url_for, jsonify, make_response, abort
from werkzeug.security import generate_password_hash,check_password_hash
import uuid
from models import User, Business

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

review_list = []  #Review list

@app.route('/api/v1/auth/register', methods=['POST'])
def register():
    added_user=User()
    added_user.add_user()
    response = jsonify({"User created and added to list": added_user.Allusers})
    response.status.code=200
    return response

@app.route('/api/auth/login' , methods=['POST'])
def login():
    particular_user=[{ "id":1, "name":"john","password":123}]
    data = request.get_json()
    for i in particular_user:
        if i["name"]==data["name"] and i["password"]==data["password"]:
            response=jsonify({"Message":"User is logged in"})
            response.status.code=200
            return response
                    
@app.route('/api/v1/auth/logout', methods=['POST'])
def logout():
    response=jsonify({"Message":"User has been logged out"})
    response.status.code=200
    return response


@app.route('/api/v1/auth/reset-password', methods=['POST'])
def resetpassword():
    particular_user = [{"id": 1, "name": "john", "password": 123}]
    data = request.get_json()
    for i in particular_user:
        if i ["name"]==data["name"]:
            i["password"]=data["password"]
            response= jsonify({"Password has been reset"})
            response.status.code=200
            return response

@app.route('/api/v1/businesses/<int:businessId>', methods=['PUT'])
def buzupdate(businessId):
    business_list=[{
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

    for i in business_list:
        if i["id"] == businessId :
            i["name"]=data["name"]
            i["category"]=data["category"]
            i["location"]=data["location"]
            response = jsonify({"Business has been updated":b})
            response.status.code=200
            return response
             
@app.route('/api/v1/businesses/<int:businessId>', methods=['DELETE'])
def buzremove(businessId):
    business_list = [{
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
   
    for i in business_list:
        if i["id"]== businessId :
            business_list.remove(i)
            response=jsonify({"Message":"The Business has been deleted"})
            response.status.code=200
            return response



@app.route('/api/v1/businesses', methods=['GET'])
def Allbuz():
    particular_business= Business()
    response = jsonify(
        {"A list of all businesses": particular_business.business})
    response.status.code=200
    return response


@app.route('/api/v1/businesses/<int:businessId>', methods=['GET'])
def Onebuz(businessId):
    business_list = [{
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
    for i in business_list:
        if i["id"]== businessId :    
            
            response=jsonify({"Business":i})
            response.status.code=200
            return response

@app.route('/api/v1/businesses/<int:businessId>/reviews', methods=['POST'])
def buzreviews(businessId):
    particular_business = Business()
    for i in particular_business.business:
            if i["id"]==businessId:
                data = request.get_json()
                new_review={"id":businessId ,"name":data["review"],"Review":data["review"]}
                review_list.append( new_review)

    
    response=jsonify({"Review has been added":review_list})
    response.status.code=200
    return response

@app.route('/api/v1/businesses/<int:businessId>/reviews', methods=['GET'])
def Onebuzreviews(businessId):
    
    response=jsonify({"All Reviews":review_list})
    response.status.code=200
    return response



if __name__ == "__main__":
    app.run()
