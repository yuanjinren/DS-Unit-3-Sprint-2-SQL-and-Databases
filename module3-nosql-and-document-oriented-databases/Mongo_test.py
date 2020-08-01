import sqlite3
import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("Mongo_User", default="OOPS")
DB_PASSWORD = os.getenv("Mongo_Password", default="OOPS")
CLUSTER_NAME = os.getenv("Mongo_Cluster_name", default="OOPS")


connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("----------------")
print("URI:", connection_uri)

client = pymongo.MongoClient(connection_uri)
print("----------------")
print("CLIENT:", type(client), client)

db = client['test']
collection = db['test']

# post1 = {'_id':0, 'name':'Tina'}
# post2 = {'_id':1, 'name':'Tim'}

# collection.insert_many([post1, post2])
#collection.update_one({'_id':1}, {'$set':{'sex':'male'}})
db1 = client['sample_airbnb']
collection1 = db1['listingsAndReviews']
count = collection1.count_documents({})
print(count)
# results = collection1.find({'name':'Ribeira Charming Duplex'})
# print(type(results))
# for result in results:
#     print(result['_id'])