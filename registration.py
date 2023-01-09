from flask          import Flask

from flask_pymongo  import PyMongo

from bson.json_util import dumps

from bson.objectid  import ObjectId

from flask          import jsonify,request




app = Flask(__name__)


app.secret_key="secretkey"

app.config['MONGO_URI'] ="mongodb://localhost:27017/upcl"

rigth = PyMongo(app)



@app.route('/input',methods =['POST'])
def add_user():
    _json =request.json
    _name =_json['name']
    _email = _json['email']
    _moblie_number = _json["mobile"]
    
    
    if _name and _email and _moblie_number and  request.method =='POST':
        
        id = rigth.db.registration.insert_one({'name':_name,"email":_email,"mobile":_moblie_number})
        
        resp = jsonify("User add successfully")
        
        resp._status_code = 200
        
        return resp
        
    else:
        return not_found()
    
    



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