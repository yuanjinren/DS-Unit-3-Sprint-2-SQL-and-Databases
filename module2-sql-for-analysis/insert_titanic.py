import os
import pandas as pd
from dotenv import load_dotenv
import psycopg2

df_titanic = pd.read_csv('titanic.csv')
results = df_titanic.values.tolist()

# connect to elephantSQL-hosted postgreSQL
load_dotenv()
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD, host=DB_HOST)

cursor = connection.cursor()
# CREATE TYPE gender as ENUM ('male', 'female');

create_titanic_table_query = '''
CREATE TABLE IF NOT EXISTS Titanic (
    ID              SERIAL PRIMARY KEY,
    Survived        INT,
    Pclass          INT,
    Name            VARCHAR,
    Sex             gender,
    Age             INT,
    SiblingsSpousesAboard     INT,
    ParentsChildrenAboard     INT,
    Fare            DECIMAL
)
'''
cursor.execute(create_titanic_table_query)
connection.commit()


for result in results:
    cursor.execute("INSERT INTO Titanic (survived, pclass, name, sex, age, siblingsspousesaboard, parentschildrenaboard, fare) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", result)


connection.commit()
cursor.close()
connection.close()