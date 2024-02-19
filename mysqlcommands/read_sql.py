import mysql.connector
import connection_db_sql
from connection_db_sql import connection
from mysql.connector import Error
import pandas as pd


def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        print("Read successfully")
        return result
    except Error as err:
        print(f"Error: '{err}'")

q1 = 'SELECT * FROM padaria.produto' # objeto de pesquisa
results = read_query(connection, q1)

for result in results:
    print(result)
    

connection.close()