from flask         import Flask

from flask_pymongo import PyMongo

from bson.json_util import dumps

from bson.objectid import ObjectId

from flask import jsonify,request

from werkzeug.security import  generate_password_hash,check_password_hash


app = Flask(__name__)


app.secret_key="secretkey"

app.config['MONGO_URI'] ="mongodb://localhost:27017/upcl"

mongo = PyMongo(app)


#========     =======  =======  =========   =======     login         +++++++++   ++++++    ++++++    ++++++   +++++++=    ++++++++
@app.route('/add',methods =['POST' ,'GET'])
def kkumh():
    _json =request.json
    _name =_json['name']
    _password = _json['pwd']
    
    if _name and _password and request.method =='POST':
        _hashed_password = generate_password_hash(_password)
        
        id = mongo.db.login.insert_one({'name':_name,'pwd':_hashed_password})
        
        resp = jsonify("User add successfully")
        
        resp._status_code = 200
        
        return resp
        
    else:
        return not_found()
    
    
@app.route('/users')
def yhth():
    users =  mongo.db.connect.find() 
    resp = dumps(users)
    return resp 



@app.route('/user/<id>')
def ghtf(id):
    user =  mongo.db.login.find_one({'_id ': ObjectId(id)}) 
    resp = dumps(user)
    return resp 




@app.route('/delete/<id>',methods=['DELETE'])
def delete_user(id):
    mongo.db.login.delete_one({'id': ObjectId(id)}) 
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
    
    
        mongo.db.login.update_one({'_id':ObjectId(_id['$oid'])  if '$oid' in _id else ObjectId(_id)},{'$set': {"name" : _name,"pwd":_hashed_password }})
        resp = jsonify("user updated successfully")
    
    
        resp.status_code = 200
    
        return resp 
    
    else:
        return not_found



# +++++++++++++++++++++++++++=++ for the new connection(new registration)+++++++++++++++++++++++++++++++++++++++++

@app.route('/nsc',methods =['POST' ,'GET'])
def fgfhg():
    _json =request.json
    _Request_type =_json['request_type']
    _service =_json['service']
    _Divsion_office = _json['division']
    _sub_division_office = _json['sub_division']
    _main_category = _json['main_category']
    _category_of_supply = _json['category']
    _purpose =_json['purpose']
    _plot_size = _json['plot_size']
    _supply_voltage = _json['supply']
    _applied_load = _json['applied']
    _built_up_area = _json['area']
    _prepaid_postpaid = _json['prepaid']
    _Name = _json['name']
    _father_husband =_json['father']
    _house_plot = _json['house']
    _colony_area = _json['area']
    _Residence_phone =_json['residence']
    _Email= _json['email']
    _Data_of_brith =_json['data']
    _street_name= _json['street']
    _District = _json['district']
    _mobile_nummber = _json['mobile']
    _fax_number = _json['fax']
    _website = _json['website']    
            
       
    if _Request_type and _service and _Divsion_office and _sub_division_office and _main_category and _category_of_supply and _purpose and _plot_size and _supply_voltage and _applied_load and  _built_up_area and _prepaid_postpaid and _Name and _father_husband and _house_plot and  _colony_area and  _Residence_phone and _Email and _Data_of_brith and _street_name and _District and _mobile_nummber and  _fax_number and _website and  request.method =='POST':
                
        id = mongo.db.new_registration.insert_one({'request_type':_Request_type,
                                        'service':_service ,
                                        "Divsion" :_Divsion_office,
                                        "sub_division":_sub_division_office,
                                        "main_category":_main_category,
                                        "category": _category_of_supply , 
                                        'purpose' :_purpose,                                                           
                                        'plot_size':_plot_size,
                                        'supply':_supply_voltage ,
                                        'applied':_applied_load ,
                                        'area':_built_up_area,
                                        'prepaid':_prepaid_postpaid ,
                                        'name':_Name ,
                                        'father' :_father_husband ,
                                        'house':_house_plot ,
                                        'area': _colony_area,  
                                        'residence':_Residence_phone, 
                                        'email':_Email})    
        
        resp = jsonify("User add successfully")
        
        resp._status_code = 200
        
        return resp
        
    else:
        return not_found()
    


# +++++++++++++++++++++++++++++++ registration  +++++++++++++++++++++++++++++++++++++++++++++

@app.route('/input',methods =['POST' ,'GET'])
def uhjj():
    _json =request.json
    _name =_json['name']
    _email = _json['email']
    _moblie_number = _json["mobile"]
    
    
    if _name and _email and _moblie_number and  request.method =='POST':
        
        id = mongo.db.registration.insert_one({'name':_name,"email":_email,"mobile":_moblie_number})
        
        resp = jsonify("User add successfully")
        
        resp._status_code = 200
        
        return resp
        
    else:
        return not_found()




# ========================= view bill =========================================

@app.route('/bill',methods =['POST'])
def jhuh():
    _json =request.json
    _consumer_id =_json['consumer']
    _month= _json['month' ]
    _year =_json['year']
    if _consumer_id and _month and _year and request.method =='POST':

        id = mongo.db.view_bill.insert_one({'consumer': _consumer_id,'month':_month,'year':_year})
        
        resp = jsonify("User view the bill")
        
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
    app.run(host="0.0.0.0", port='2000' )  