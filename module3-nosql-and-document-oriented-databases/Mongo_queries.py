import sqlite3
import pymongo
import os
from dotenv import load_dotenv

# connect to sqlite3 DB for RPG data
sl_connection = sqlite3.connect("/Users/Tinaren/Desktop/LambdaSchool/Unit3/Unit3_SC2/Assignment1/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/rpg_db.sqlite3")
sl_cursor = sl_connection.cursor()
characters = sl_cursor.execute("SELECT * FROM charactercreator_character").fetchall()

characters_dicts = []
for character in characters:
    d = {
        'char_id': character[0],
        'name': character[1],
        'level': character[2],
        'exp': character[3],
        'hp': character[4],
        'strength': character[5],
        'intelligence': character[6],
        'dexterity': character[7],
        'wisdom': character[8]
    }
    characters_dicts.append(d)

# connect to MongoDB
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

# create MongoDB database
db = client.rpg_database
print("----------------")
print("DB:", type(db), db)

# create collection(table) in MongoDB database
collection = db.rpg_characters

# insert all records to the table
collection.insert_many(characters_dicts)

# check how many records are there
print(collection.count_documents({}))



