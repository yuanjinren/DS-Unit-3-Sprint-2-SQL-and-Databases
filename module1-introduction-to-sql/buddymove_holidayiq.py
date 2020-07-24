import os
import pandas as pd
from IPython.display import display
import sqlite3
from sqlalchemy import create_engine

# Load the data
df = pd.read_csv('buddymove_holidayiq.csv')
display(df.head())
display(df.shape)
display(df.isnull().sum())

# Create a connection and use to_sql to insert the data into a new table
connection = sqlite3.connect("buddymove_holidayiq.sqlite3")
df.to_sql("buddymove_holidayiq", con=connection, if_exists='replace', index=False)

cursor = connection.cursor()

# def get_data(query, connection):
#     cursor = connection.cursor()
#     result = cursor.execute(query).fetchall()

#     columns = list(map(lambda x: x[0], cursor.description))

#     df = pd.DataFrame(data=result, columns=columns)
#     return df

# df1 = get_data("SELECT COUNT('User Id') AS Total_Rows FROM buddymove_holidayiq", connection)
# display(df1.head())
query1 = "SELECT COUNT('User Id') FROM buddymove_holidayiq"
result1 = cursor.execute(query1).fetchone()
display('Total_Rows',result1)

query2 = "SELECT COUNT('User Id') FROM buddymove_holidayiq where Nature >= 100 and Shopping >=100"
result2 = cursor.execute(query2).fetchone()
display('Total_Users',result2)

query3 = "SELECT AVG(Sports), AVG(Religious),AVG(Nature), AVG(Theatre), AVG(Shopping), AVG(Picnic) FROM buddymove_holidayiq"
result3 = cursor.execute(query3).fetchall()
for row in result3:
    display('Sports',row[0])
    display('Religious',row[1])
    display('Nature',row[2])
    display('Theatre',row[3])
    display('Shopping',row[4])
    display('Picnic',row[5])

