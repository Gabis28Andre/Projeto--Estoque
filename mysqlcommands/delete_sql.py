import mysql.connector
import connection_db_sql
import read_sql
from connection_db_sql import connection
from mysql.connector import Error
import pandas as pd


def delete_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Data deleted successfully")
    except Error as err:
        print(f"Error: '{err}'")
        

def dufdel():
    table = input("Qual a tabela? ")
    obj_pesquisa = input("Qual é a Coluna da tabela? ")
    item = input("Qual Item quer deletar? ")
    
    return table, obj_pesquisa, item

table, obj_pesquisa, item = dufdel()

obj_del = f'DELETE FROM {table} WHERE {obj_pesquisa} = "{item}"'

cursor = delete_query(connection, obj_del)

connection.close()