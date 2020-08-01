import sqlite3
import pymongo
import os
from dotenv import load_dotenv

# connect to sqlite3 DB for RPG data
sl_connection = sqlite3.connect("/Users/Tinaren/Desktop/LambdaSchool/Unit3/Unit3_SC2/Assignment1/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/rpg_db.sqlite3")
sl_cursor = sl_connection.cursor()
characters = sl_cursor.execute("SELECT * FROM charactercreator_character").fetchall()
inventory = sl_cursor.execute("SELECT * FROM charactercreator_character_inventory").fetchall()
cleric = sl_cursor.execute("SELECT * FROM charactercreator_cleric").fetchall()
mage = sl_cursor.execute("SELECT * FROM charactercreator_mage").fetchall()
thief = sl_cursor.execute("SELECT * FROM charactercreator_thief").fetchall()
fighter = sl_cursor.execute("SELECT * FROM charactercreator_fighter").fetchall()
necromancer = sl_cursor.execute("SELECT * FROM charactercreator_necromancer").fetchall()
armory_item = sl_cursor.execute("SELECT * FROM armory_item").fetchall()
armory_weapon = sl_cursor.execute("SELECT * FROM armory_weapon").fetchall()
characters_dicts = []
inventory_dicts = []
cleric_dicts = []
mage_dicts = []
thief_dicts = []
fighter_dicts = []
necromancer_dicts = []
armory_item_dicts = []
armory_weapon_dicts = []
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

for row in inventory:
    d = {
        'id': row[0],
        'character_id': row[1],
        'item_id': row[2]
    }
    inventory_dicts.append(d)

for row in cleric:
    d = {
        'character_ptr_id': row[0],
        'using_shield': row[1],
        'mana': row[2]
    }
    cleric_dicts.append(d)

for row in mage:
    d = {
        'character_ptr_id': row[0],
        'has_pet': row[1],
        'mana': row[2]
    }
    mage_dicts.append(d)

for row in thief:
    d = {
        'character_ptr_id': row[0],
        'is_sneaking': row[1],
        'energy': row[2]
    }
    thief_dicts.append(d)

for row in fighter:
    d = {
        'character_ptr_id': row[0],
        'using_shield': row[1],
        'rage': row[2]
    }
    fighter_dicts.append(d)

for row in necromancer:
    d = {
        'mage_ptr_id': row[0],
        'talisman_charged': row[1]
    }
    necromancer_dicts.append(d)

for row in armory_item:
    d = {
        'item_id': row[0],
        'name': row[1],
        'value': row[2],
        'weight': row[3]
    }
    armory_item_dicts.append(d)

for row in armory_weapon:
    d = {
        'item_ptr_id': row[0],
        'power': row[1]
    }
    armory_weapon_dicts.append(d)

# connect to MongoDB
load_dotenv()

DB_USER = os.getenv("Mongo_User", default="OOPS")
DB_PASSWORD = os.getenv("Mongo_Password", default="OOPS")
CLUSTER_NAME = os.getenv("Mongo_Cluster_name", default="OOPS")


connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"

client = pymongo.MongoClient(connection_uri)

# create or connect to MongoDB database
db = client.rpg_database
# print("----------------")
# print("DB:", type(db), db)

# create collection(table) in MongoDB database
collection = db.rpg_characters
collection1 = db.rpg_characters_inventory
collection2 = db.rpg_cleric
collection3 = db.rpg_fighter
collection4 = db.rpg_mage
collection5 = db.necromancer
collection6 = db.thief
collection7 = db.armory_item
collection8 = db.armory_weapon


# insert all records to the table
collection.insert_many(characters_dicts)
collection1.insert_many(inventory_dicts)
collection2.insert_many(cleric_dicts)
collection3.insert_many(fighter_dicts)
collection4.insert_many(mage_dicts)
collection5.insert_many(necromancer_dicts)
collection6.insert_many(thief_dicts)
collection7.insert_many(armory_item_dicts)
collection8.insert_many(armory_weapon_dicts)


# check how many records are there
# print(collection.count_documents({}))



