import base64
from flask   import Flask ,request

from flask_pymongo import PyMongo

from bson.json_util import dumps

from bson.objectid import ObjectId

from flask import jsonify,request

from flask import make_response


app                      =    Flask(__name__)


app.secret_key           =   "secretkey"

app.config['MONGO_URI']  =  "mongodb://localhost:27017/upcl_2"

mongo = PyMongo(app)



@app.route('/image/<image_id>')
def retrieve_image(image_id):
    image = mongo.db.images.find_one({'_id': ObjectId('63dd16af283408c60c1c57f8')})
    if not image:
        return "Image not found", 404

    image_data = image['image']
    encoded_image = base64.b64encode(image_data).decode('utf-8')
    response = make_response(encoded_image)
    response.headers['Content-Type'] = 'image/jpeg'
    return response

if __name__=="__main__":
    app.run(host='127.0.0.1' ,port=8000)
