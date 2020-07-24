import os
import sqlite3
import pandas as pd

DB_FILEPATH = os.path.join(os.path.dirname(__file__),'rpg_db.sqlite3')
connection = sqlite3.connect(DB_FILEPATH)
cursor = connection.cursor()
def get_data(query, connection):
    cursor = connection.cursor()
    result = cursor.execute(query).fetchall()

    columns = list(map(lambda x: x[0], cursor.description))

    df = pd.DataFrame(data=result, columns=columns)
    return df

df1 = get_data('SELECT COUNT(character_id) AS Total_Characters FROM charactercreator_character',connection)
print("Character in total is as follows: ")
print(df1.head())

query2 = """
SELECT
    *
FROM
    (SELECT COUNT(DISTINCT character_ptr_id) AS Cleric FROM charactercreator_cleric)
    ,(SELECT COUNT(DISTINCT character_ptr_id) AS Fighter FROM charactercreator_fighter)
    ,(SELECT COUNT(DISTINCT character_ptr_id) AS Mage FROM charactercreator_mage)
    ,(SELECT COUNT(DISTINCT mage_ptr_id) AS Necromancer FROM charactercreator_necromancer)
    ,(SELECT COUNT(DISTINCT character_ptr_id) AS Thief FROM charactercreator_thief);
"""

df2 = get_data(query2, connection)
print("Number of characters in each subclass is as follows: ")
print(df2)

df3 = get_data('SELECT COUNT(item_id) AS Total_Item FROM armory_item',connection)
print("Number of total item is as follows: ")
print(df3.head())

df4 = get_data('SELECT COUNT(item_ptr_id) AS Weapon_Item_Number FROM armory_weapon',connection)
print("Number of weapon items is as follows: ")
print(df4.head())

query5 = """
SELECT 
(Total_Item - Weapon_Item) AS Non_Weapon_Item_Number
FROM
(select COUNT(item_ptr_id) AS Weapon_Item FROM armory_weapon),
(SELECT COUNT(item_id) AS Total_Item FROM armory_item)
"""

df5 = get_data(query5,connection)
print("Number of non-weapon items is as follows: ")
print(df5)

df6 = get_data('select character_id, count(item_id) AS Item_Number from charactercreator_character_inventory group by character_id limit 20', connection)
print("Number of items each character has is as follows: ")
print(df6)

query7 = """
SELECT 
inventory.character_id, COUNT(weapon.item_ptr_id) AS Weapon_Number
FROM charactercreator_character_inventory AS inventory left JOIN armory_weapon AS weapon where
inventory.item_id = weapon.item_ptr_id
group BY inventory.character_id
limit 20
"""
df7 = get_data(query7, connection)
print("Number of weapons each character has is as follows: ")
print(df7)

query8 = """
SELECT 
 AVG(Item_Number) AS Average_Item_Number
FROM
 (select count(item_id) AS Item_Number from charactercreator_character_inventory group by character_id)
 """
df8 = get_data(query8, connection)
print("Number of items each character have on average: ")
print(df8)

query9 = """
SELECT 
 AVG(Weapon_Number) AS Average_Weapon_Number
 FROM
 (SELECT 
inv.character_id, COUNT(weapon.item_ptr_id) AS Weapon_Number
FROM charactercreator_character cha
LEFT JOIN charactercreator_character_inventory AS inv on cha.character_id = inv.character_id
LEFT JOIN armory_weapon AS weapon on inv.item_id = weapon.item_ptr_id
GROUP BY inv.character_id)
"""
df9 = get_data(query9, connection)
print("Number of weapons each character have on average: ")
print(df9)
