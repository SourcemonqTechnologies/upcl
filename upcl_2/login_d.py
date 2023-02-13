from flask   import Flask ,request

from flask_pymongo import PyMongo

from bson.json_util import dumps

from bson.objectid import ObjectId

from flask import jsonify,request

from werkzeug.security import  generate_password_hash,check_password_hash



app = Flask(__name__)

app.secret_key="secretkey"

app.config['MONGO_URI'] ="mongodb://localhost:27017/upcl"

mongo = PyMongo(app)


@app.route('/add',methods =['POST' ,'GET'])
def kkumh():
    _json =request.json
    _name =_json['name']
    _password = _json['pwd']

    if _name and _password and request.method =='POST' :
        _hashed_password = generate_password_hash(_password)

        id = mongo.db.loginD.insert_one({'name':_name,'pwd':_hashed_password})

        resp = jsonify("User add successfully")

        resp._status_code = 200

        return resp

    else:
        return not_found()



@app.route('/users',methods =['GET'])
def yhth():
    users =  mongo.db.loginD.find()
    resp = dumps(users)
    return resp



@app.route('/user/<id>' ,methods =['GET'])
def ghjkk(id):
    user =  mongo.db.loginD.find_one({'_id ': id})
    resp = dumps(user)
    return resp




@app.errorhandler(404)
def not_found(error =None):
    message ={
        'status':404,
        'message':"not found" + request.url

    }
    resp =jsonify(message)

    resp.status_code=404

    return resp


if __name__=="__main__":
    app.run(host='127.0.0.1' ,port=8000)