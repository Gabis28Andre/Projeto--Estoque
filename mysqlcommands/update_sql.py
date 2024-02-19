import mysql.connector
import connection_db_sql
from connection_db_sql import connection
from mysql.connector import Error
import pandas as pd


def update_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Update successfully \n")
        
    except Error as err:
        print(f"Error: '{err}'")
        

def info_query(connection, query):
    cursor = connection.cursor()
    solve = None
    try:
        cursor.execute(query)
        solve = cursor.fetchall()
        print("Info successfully \n")
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



def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        print("Read successfully \n")
        return result
    except Error as err:
        print(f"Error: '{err}'")

q1 = 'SELECT * FROM padaria.produto' # objeto de pesquisa
results = read_query(connection, q1)
valor = 1

for result in results:
    print(f"Item: {result} \n")

def defupd():
    
    nome_produto = input("Qual é o nome do produto que deseja alterar?")
    
    typeitem = input("Qual item deseja atualizar? ")
    
    upitem = int(input(f"Digite o valor que vai ser atualizado: "))
    
    return typeitem, upitem, nome_produto

typeitem, upitem, nome_produto = defupd()



obj_update = f'UPDATE {table} SET {typeitem} = {upitem} WHERE nome_produto = "{nome_produto}"' 

cursor = update_query(connection, obj_update)

connection.close()