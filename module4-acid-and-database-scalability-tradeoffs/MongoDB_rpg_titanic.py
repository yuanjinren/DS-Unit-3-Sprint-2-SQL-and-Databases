import sqlite3
import pymongo
import psycopg2
import os
from dotenv import load_dotenv

def rpg_queries():
    load_dotenv()

    DB_USER = os.getenv("Mongo_User", default="OOPS")
    DB_PASSWORD = os.getenv("Mongo_Password", default="OOPS")
    CLUSTER_NAME = os.getenv("Mongo_Cluster_name", default="OOPS")

    connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"

    client = pymongo.MongoClient(connection_uri)

    db = client['rpg_database']
    collection = db['rpg_characters']
    collection1 = db.rpg_characters_inventory
    collection2 = db.rpg_cleric
    collection3 = db.rpg_fighter
    collection4 = db.rpg_mage
    collection5 = db.necromancer
    collection6 = db.thief
    collection7 = db.armory_item
    collection8 = db.armory_weapon

    result1 = collection.count_documents({})
    print("Character in total is as follows: ")
    print(result1)

    result2 = collection2.count_documents({})
    print("Cleric class in total is as follows: ")
    print(result2)

    result3 = collection3.count_documents({})
    print("Fighter class in total is as follows: ")
    print(result3)

    result4 = collection4.count_documents({})
    print("Mage class in total is as follows: ")
    print(result4)

    result5 = collection5.count_documents({})
    print("Necromancer class in total is as follows: ")
    print(result5)

    result6 = collection6.distinct('character_ptr_id')
    print("Thief class in total is as follows: ")
    print(len(result6))

    result7 = collection7.count_documents({})
    print("Number of total item is as follows: {}".format(result7))

    result8 = collection8.count_documents({})
    print("Number of weapon items is: {}".format(result8))

    print("Number of non-weapon items is: {} ".format(result7 - result8))

    # result9 = collection1.distinct('item_id')
    # for result in result9:
    #      print(result)
    # result9 = collection1.aggregate([
    #     { '$group':{
    #         '_id' : "$character_id",
    #         'total_items': {'$sum': "$item_id"}}}
    # ])
    #print(result9[:20])
    # result9 = collection1.aggregate([
    #     {'$group': { '_id': "$character_id", 'item':"$item_id"}},
    #     {'$count': {'total': "$item_id"}
    # ])
    
    # for result in result9:
    #     print(result)
    
'''

How many Items does each character have? (Return first 20 rows)
How many Weapons does each character have? (Return first 20 rows)
On average, how many Items does each Character have?
On average, how many Weapons does each character have?
'''
def titanic_queries():
    # connect to elephantSQL-hosted postgreSQL
    load_dotenv()
    DB_NAME_PSY = os.getenv("DB_NAME_PSY")
    DB_USER_PSY = os.getenv("DB_USER_PSY")
    DB_PASSWORD_PSY = os.getenv("DB_PASSWORD_PSY")
    DB_HOST_PSY = os.getenv("DB_HOST_PSY")

    connection = psycopg2.connect(dbname=DB_NAME_PSY, user=DB_USER_PSY,password=DB_PASSWORD_PSY, host=DB_HOST_PSY)

    cursor = connection.cursor()
    
    cursor.execute('SELECT COUNT(id) from titanic where survived = 1')
    result1 = cursor.fetchone()
    print('{} passengers survived'.format(result1))

    cursor.execute('SELECT COUNT(id) from titanic where survived = 0')
    result2 = cursor.fetchone()
    print('{} passengers died'.format(result2))

    cursor.execute('SELECT pclass, COUNT(id) from titanic group by pclass')
    result3 = cursor.fetchall()
    print('Passengers were in each class are: ')
    print(result3)

    cursor.execute('SELECT pclass, COUNT(survived) AS Died from titanic where survived = 0 group by pclass')
    result4 = cursor.fetchall()
    print('Passengers died in each class are: ')
    print(result4)

    cursor.execute('SELECT pclass, COUNT(survived) AS Survived from titanic where survived = 1 group by pclass')
    result5 = cursor.fetchall()
    print('Passengers survived in each class are: ')
    print(result5)

    query = """
    SELECT * FROM
    (SELECT avg(age) from titanic where survived=1) AS Average_Age_Survived,
    (SELECT avg(age) from titanic where survived=0) AS Average_Age_Died
    """
    cursor.execute(query)
    result6 = cursor.fetchall()
    print('The average age of survivors vs nonsurvivors were: {}'.format(result6))

    cursor.execute('SELECT pclass, avg(age) from titanic group by pclass')
    result7 = cursor.fetchall()
    print('The average age of Passengers in each class were: ')
    print(result7)
    
    cursor.execute('SELECT pclass, avg(fare) from titanic group by pclass')
    result8 = cursor.fetchall()
    print('The average fare of Passengers in each class were: ')
    print(result8)

    cursor.execute('SELECT pclass, avg(fare) from titanic where survived=1 group by pclass')
    result9 = cursor.fetchall()
    print('The average fare of Passengers in each class by survivals were: ')
    print(result9)

    cursor.execute('SELECT pclass, avg(siblingsspousesaboard) AS Average_Sibling_Spouse from titanic where survived=1 group by pclass')
    result10 = cursor.fetchall()
    print('The average siblings/spouses/aboard in each class by survivals were: ')
    print(result10)

    cursor.execute('SELECT pclass, avg(siblingsspousesaboard) AS Average_Sibling_Spouse from titanic group by pclass')
    result11 = cursor.fetchall()
    print('The average siblings/spouses/aboard in each class were: ')
    print(result11)

    cursor.execute('SELECT pclass, avg(parentschildrenaboard) AS Average_Parents_Children from titanic where survived=1 group by pclass')
    result12 = cursor.fetchall()
    print('The average parents/children aboard in each class by survivals were: ')
    print(result12)

    cursor.execute('SELECT pclass, avg(parentschildrenaboard) AS Average_Parents_Children from titanic group by pclass')
    result13 = cursor.fetchall()
    print('The average parents/children aboard in each class were: ')
    print(result13)

if __name__ == "__main__":
    rpg_queries()
    titanic_queries()
