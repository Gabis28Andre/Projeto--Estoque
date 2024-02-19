import mysql.connector
from mysql.connector import Error
import pandas as pd

# é o mesmo código do connection, but inclui o db já criado, podemos trocar

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


password = "Innov@123"
db="padaria"
connection = create_db_connection("localhost", "root", password, db) #conectando com o mysql]


