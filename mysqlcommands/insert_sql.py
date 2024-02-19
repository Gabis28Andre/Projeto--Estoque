import mysql.connector
import connection_db_sql
from connection_db_sql import connection
from mysql.connector import Error
import pandas as pd


def insert_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Data created successfully")
    except Error as err:
        print(f"Error: '{err}'")



#CREATE

def obterdados():
    nome_produto = input("Nome do produto: ")
    valor = float(input("Valor: "))
    descricao = input("Descricao: ")
    qtd = int(input("Qual a qtd do produto? "))
    estoque_minimo = 1
    estoque_maximo = 100
    return nome_produto, qtd, valor, descricao, estoque_minimo, estoque_maximo

nome_produto, qtd, valor, descricao, estoque_minimo, estoque_maximo = obterdados()

dat = f'INSERT INTO produto (nome_produto, qtd, valor, descricao, estoque_minimo, estoque_maximo) VALUES ("{nome_produto}", {qtd}, {valor},"{descricao}", {estoque_minimo}, {estoque_maximo})'


#EXECUÇÃO
cursor = insert_query(connection, dat)
connection.commit() #usa quando edita, e se usa depois do execute

#FINALIZAÇÃO
connection.close()