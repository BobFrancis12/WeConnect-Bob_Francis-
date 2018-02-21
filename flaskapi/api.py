from flask import Flask, render_template, flash, request,redirect, url_for, jsonify, make_response
from werkzeug.security import generate_password_hash,check_password_hash
import uuid


# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

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
            "category"="telecommunication",
            "location"="Bugolobi"
        }]

    def add_business(self):
        data = request.get_json()
        new_business={ "id":str(uuid.uuid4()), "name":data["name"],"category":data["category"],"location":data["location"]}
        self.business.append(new_business)  

    def get_business(id):

        return [x for x in business if x['id'] == id]


    def get_all_business(id):
        return [self.business=[]]

    def delete_business(id):
        data1 = get_business(id) 
        return self.business.remove(data)
        

@app.route('/api/v1/auth/register', methods=['POST'])
def register():
    x=User()
    x.add_user()
    return jsonify({"User created and added to list":x.Allusers})

@app.route('/api/auth/login' , methods=['POST'])
def login():
    return ''
    
@app.route('/api/v1/auth/logout', methods=['POST'])
def logout():
    return ''

@app.route('/api/v1/auth/reset-password', methods=['POST'])
def resetpassword():
    
    return ''

@app.route('/api/v1/businesses', methods=['POST'])
def buzregister():
    return ''

@app.route('/api/v1/businesses/<int:>', methods=['PUT'])
def buzupdate():
    return ''

@app.route('/api/v1/businesses/<int:>', methods=['DELETE'])
def buzremove():
    return ''


@app.route('/api/v1/businesses', methods=['GET'])
def Allbuz():
    return ''

@app.route('/api/v1/businesses/<int:>', methods=['GET'])
def Onebuz():
    return ''

@app.route('/api/v1/businesses/<int:>/reviews', methods=['POST'])
def buzreviews():
    return ''

@app.route('/api/v1/businesses/<int:>/reviews', methods=['GET'])
def Onebuzreviews():
    return ''








if __name__ == "__main__":
    app.run()