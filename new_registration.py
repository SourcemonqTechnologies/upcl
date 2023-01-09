from flask import Flask

from flask_pymongo import PyMongo

from bson.json_util import dumps

from bson.objectid import ObjectId

from flask import jsonify,request



app = Flask(__name__)


app.config['MONGO_URI'] ="mongodb://localhost:27017/upcl"



down = PyMongo(app)



@app.route('/nsc',methods =['POST'])
def add_user():
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
   
                
        id = down.db.new_registration.insert_one({'request_type':_Request_type,
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
    
    
    
@app.errorhandler(404)
def not_found(error =None):
    message ={
        'status':404,
        'message':"not found" + request.url
        
    }
    resp =jsonify(message)

    resp.status_code=404
    
    return resp
    




if __name__ == "__main__":
    app.run(host='0.0.0.0')