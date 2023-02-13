from flask   import Flask ,request

from flask_pymongo import PyMongo

from bson.json_util import dumps

from bson.objectid import ObjectId

from flask import jsonify,request

from werkzeug.security import  generate_password_hash,   check_password_hash



app = Flask(__name__)

app.secret_key="secretkey"

app.config['MONGO_URI'] ="mongodb://localhost:27017/upcl_2"

mongo = PyMongo(app)


@app.route('/add',methods =['POST' ])
def kkumh():
    _json =request.json
    _consumer =_json['consumer']
    _references = _json['refernce']




    if  _consumer and _references and  request.method =='POST' :

        id = mongo.db.view_bill.insert_one({'consumer':_consumer,
                                                'refernce':_references})




        resp = jsonify("User add successfully")

        resp._status_code = 200

        return resp

    else:
        return not_found()



@app.route('/users',methods =['GET'])
def yhth():
    users =  mongo.db.view_bill.find()
    resp = dumps(users)
    return resp



@app.route('/user/<id>' ,methods =['GET'])
def ghjkk(id):
    user =  mongo.db.view_bill.find_one({'_id ': id})
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
    app.run(host='192.168.56.1' ,port=3000)