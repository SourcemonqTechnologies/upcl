from flask import Flask

from flask_pymongo import PyMongo

from bson.json_util import dumps

from bson.objectid import ObjectId

from flask import jsonify,request

from werkzeug.security import  generate_password_hash,check_password_hash


app = Flask(__name__)


app.secret_key="secretkey"

app.config['MONGO_URI'] ="mongodb://localhost:27017/sourcemonq"

mongo = PyMongo(app)



@app.route('/add',methods =['POST'])
def add_user():
    _json =request.json
    _name =_json['name']
    _password = _json['pwd']
    
    if _name and _password and request.method =='POST':
        _hashed_password = generate_password_hash(_password)
        
        id = mongo.db.connect.insert_one({'name':_name,'pwd':_hashed_password})
        
        resp = jsonify("User add successfully")
        
        resp._status_code = 200
        
        return resp
        
    else:
        return not_found()
    
    
@app.route('/users')
def users():
    users =  mongo.db.connect.find() 
    resp = dumps(users)
    return resp 



@app.route('/user/<id>')
def user(id):
    user =  mongo.db.connect.find_one({'_id ': ObjectId(id)}) 
    resp = dumps(user)
    return resp 




@app.route('/delete/<id>',methods=['DELETE'])
def delete_user(id):
    mongo.db.connect.delete_one({'id': ObjectId(id)}) 
    resp = jsonify("user deleted successfully")
    
    
    resp.status_code = 200
    
    return resp 

app.route('/update/<id>',methods=['PUT'])
def update_user(id):
    _id = id
    _json = request.json
    _name = _json['name']
    _password = _json['pwd']
    
    if _name and _password and _id and request.method =='PUT':
        _hashed_password = generate_password_hash(_password)
    
    
        mongo.db.connect.update_one({'_id':ObjectId(_id['$oid'])  if '$oid' in _id else ObjectId(_id)},{'$set': {"name" : _name,"pwd":_hashed_password }})
        resp = jsonify("user updated successfully")
    
    
        resp.status_code = 200
    
        return resp 
    
    else:
        return not_found


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
    app.run(host='0.0.0.0')                          #this is crud api