from flask   import Flask ,request

from flask_pymongo import PyMongo

from bson.json_util import dumps

from bson.objectid import ObjectId

from flask import jsonify,request

from werkzeug.security import  generate_password_hash,check_password_hash



app = Flask(__name__)

app.secret_key="secretkey"

app.config['MONGO_URI'] ="mongodb://localhost:27017/upcl_2"

mongo = PyMongo(app)


@app.route('/add',methods =['POST' ])
def kkumh():
    _json =request.json
    _name =_json['name']
    _Address = _json['address']
    _mobile = _json['mobile']
    _password = _json['pwd']
    _division = _json['division']
    _father_name =_json['father_name']
    _data_of_birth = _json['data']
    _aadhar = _json['aadhar']
    _bank_name = _json['bank']
    _bank_acc = _json['bank_acc']
    _ifsc_code = _json['ifcs']





    if _name and _Address and _mobile and _password  and _division and _father_name and _data_of_birth and _aadhar and _bank_name and _bank_acc and _ifsc_code and request.method =='POST' :
        _hashed_password = generate_password_hash(_password)

        id = mongo.db.registration.insert_one({'name':_name,
                                        'address':_Address,
                                        'mobile':_mobile,
                                        'pwd':_hashed_password,
                                        'division':_division,
                                        'father_name':_father_name,
                                        'data':_data_of_birth,
                                        'aadhar':_aadhar,
                                        'bank':_bank_name,
                                        'bank_acc':_bank_acc,
                                        'ifcs':_ifsc_code})




        resp = jsonify("User add successfully")

        resp._status_code = 200

        return resp

    else:
        return not_found()

@app.route('/users',methods =['GET'])
def yhth():
    users =  mongo.db.registration.find()
    resp = dumps(users)
    return resp



@app.route('/user/<id>' ,methods =['GET'])
def ghjkk(id):
    user =  mongo.db.registration.find_one({'_id ': id})
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
    app.run(host='3.112.213.255', port =5000)