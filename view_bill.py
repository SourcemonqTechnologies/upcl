from flask import Flask

from flask_pymongo import PyMongo

from bson.json_util import dumps

from bson.objectid import ObjectId

from flask import jsonify,request



app = Flask(__name__)


app.config['MONGO_URI'] ="mongodb://localhost:27017/upcl"



up = PyMongo(app)


@app.route('/bill',methods =['POST'])
def add_user():
    _json =request.json
    _consumer_id =_json['consumer']
    _month= _json['month' ]
    _year =_json['year']
    if _consumer_id and _month and _year and request.method =='POST':

        id = up.db.view_bill.insert_one({'consumer': _consumer_id,'month':_month,'year':_year})
        
        resp = jsonify("User view the bill")
        
        resp._status_code = 200
        
        return resp

    else:
        return not_found()
    

@app.route('/pay')                               
def pay_users():
    users =  up.db.view_bill.find() 
    resp = dumps(users)
    return resp 


@app.route('/pay/<id>')
def user(id):
    user = up.db.veiw_bill.find_one({'_id ': ObjectId(id)}) 
    resp = dumps(user)
    return resp 






@app.route('/delete/<id>',methods=['DELETE'])
def delete_user(id):
    up.db.veiw_bill.delete_one({'_id ': ObjectId(id)}) 
    resp = jsonify("user deleted successfully")
    
    
    resp.status_code = 200
    
    return resp 



app.route('/update/<id>',methods=['PUT'])
def update_user(id):
    _id = id
    _json = request.json
    _consumer_id = _json['consumer']
    _month = _json['month']
    _year = _json["year"]
    
    if _consumer_id and _month and _year and _id and request.method =='PUT':
        
    
        up.db.veiw_bill.update_one({'_id':ObjectId(_id['$oid'])if '$oid' in _id else ObjectId(_id)},{'$set': {"consumer" :_consumer_id ,"month":_month,"year":_year }})
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
    app.run(host='0.0.0.0')