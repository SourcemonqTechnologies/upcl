import pymongo
from bson import Binary
#  path of the image in folder
file_path = r"C:\Users\Sourcemonq\unwanted\Desktop\project\upcl_2\discomBill.jpg"

try:
    # Read the image into memory
    with open(file_path, "rb") as image:
        binary_data = Binary(image.read())
except FileNotFoundError:
    print(f"The file {file_path} could not be found")
    binary_data = None

if binary_data:
    # Connect to the MongoDB client
    client = pymongo.MongoClient("mongodb+srv://tree:tree@cluster0.8hhaxuz.mongodb.net/?retryWrites=true&w=majority")

    # Select the database and collection
    db = client["upcl"]
    col = db["images"]

    # Insert the image into the collection
    col.insert_one({"image": binary_data})
    print("Image was successfully inserted into the collection")
else:
    print("The image could not be inserted into the collection")
