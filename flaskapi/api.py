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



@app.route('/api/v1/auth/register', methods=['POST'])
def register():
    x=User()
    x.add_user()
    return jsonify({"User created and added to list":x.Allusers})

@app.route('/api/auth/login' , methods=['POST'])
def login():
    y=User()
    y.add_user()
    data = request.get_json()
    for i in y.Allusers:
        hashed_password = generate_password_hash(data["password"], method="sha256")
        if i["name"]==data["name"] and i["password"]==hashed_password:
            return jsonify({"Message":"User is logged in"})

   
            
        
@app.route('/api/v1/auth/logout', methods=['POST'])
def logout():
    return jsonify({"Message":"User has been logged out"})


@app.route('/api/v1/auth/reset-password', methods=['POST'])
def resetpassword():
    x=User()
    x.Allusers
    data = request.get_json()
    for i in x.Allusers:
        if i ["name"]==data["name"]:
            i["password"]=data["password"]

    return jsonify({"Password has been reset"})

@app.route('/api/v1/businesses', methods=['POST'])
def buzregister():
    b=Business()
    b.add_business()
    return jsonify({"Business has been created and added to the list":b.business})


@app.route('/api/v1/businesses/<int:id>', methods=['PUT'])
def buzupdate(id):
    b=Business()
    data = request.get_json()
    
    for i in b.business:
        if i["id"]== id :
             i["name"]=data["name"]
             i["category"]=data["category"]
             i["location"]=data["location"]
             
             

    return jsonify({"Business has been updated":b.business})

@app.route('/api/v1/businesses/<int:id>', methods=['DELETE'])
def buzremove(id):
    b=Business()
   
    for i in b.business:
        if i["id"]== id :
            del(i)
            return jsonify({"Message":"The Business has been deleted"})


    return jsonify({"Message":"The Business has been deleted"})


@app.route('/api/v1/businesses', methods=['GET'])
def Allbuz():
    b=Business()
    return jsonify({"A list of all businesses":b.business})


@app.route('/api/v1/businesses/<int:id>', methods=['GET'])
def Onebuz():
    b=Business()
    for i in b.business:
        if i["id"]== id :
            z=i
    return jsonify({"Business":z})

@app.route('/api/v1/businesses/<int:id>/reviews', methods=['POST'])
def buzreviews(id):
    y=User()
    for i in y.Allusers:
            if i["id"]==id:
                data = request.get_json()
                new_review={"id":id ,"name":data["review"],"Review":data["review"]}
                k.append( new_review)

    
    return jsonify({"Review has been added":k})

@app.route('/api/v1/businesses/<int:id>/reviews', methods=['GET'])
def Onebuzreviews(id):
    
    return jsonify({"All Reviews":k})



if __name__ == "__main__":
    app.run()