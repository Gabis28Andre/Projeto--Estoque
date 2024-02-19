import mysql.connector
import connection_db_sql
from connection_db_sql import connection
from mysql.connector import Error
import pandas as pd



def info_query(connection, query):
    cursor = connection.cursor()
    solve = None
    try:
        cursor.execute(query)
        solve = cursor.fetchall()
        print("Info successfully")
        return solve
    except Error as err:
        print(f"Error: '{err}'")

table = input("Qual o nome da tabela? ")
q1 = f'DESCRIBE {table}' # objeto de pesquisa
coluns = info_query(connection, q1)

# Exibir as informações sobre as colunas
print("Colunas da tabela:")
for solve in coluns:
    print(solve[0])  #O nome da coluna está na primeira posição de cada tupla retornada


# Fechar cursor e conexão
connection.close()