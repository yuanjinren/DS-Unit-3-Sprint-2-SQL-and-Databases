import sqlite3
import os
from dotenv import load_dotenv
import psycopg2

# connect to sqlite3 DB for RPG data
sl_connection = sqlite3.connect("rpg_db.sqlite3")
sl_cursor = sl_connection.cursor()
characters = sl_cursor.execute("SELECT * FROM charactercreator_character").fetchall()
# print(type(characters))
# print(characters)


#connect to elephantSQL-hosted postgreSQL
load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD, host=DB_HOST)
# create character table in postgres

create_character_table_query = '''
CREATE TABLE IF NOT EXISTS rpg_characters (
    character_id    SERIAL PRIMARY KEY,
    name            VARCHAR(30),
    level           INT,
    exp             INT,
    hp              INT,
    strength        INT,
    intelligence    INT,
    dexterity       INT,
    wisdom          INT
)
'''

cursor = connection.cursor()
cursor.execute(create_character_table_query)
connection.commit()

# insert character data in postgres
for character in characters:

    cursor.execute("INSERT INTO rpg_characters(character_id, name, level, exp, hp, strength, intelligence, dexterity, wisdom) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)", character)

connection.commit()
cursor.close()
connection.close()


