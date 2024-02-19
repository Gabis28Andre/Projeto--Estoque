import mysql.connector
import connection_db_sql
from connection_db_sql import connection
from mysql.connector import Error
import pandas as pd


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

create_database_query = "CREATE DATABASE padaria" #criando o banco de dados
cursor = create_database(connection, create_database_query)



cursor.close()