import mysql.connector
import connection_db_sql
from connection_db_sql import connection
from mysql.connector import Error
import pandas as pd


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


create_adm_table = """
CREATE TABLE adm (
adm_id INT PRIMARY KEY,
first_name VARCHAR(40) NOT NULL,
last_name VARCHAR(40) NOT NULL,
language_1 VARCHAR(3) NOT NULL,
language_2 VARCHAR(3),
dob DATE,
tax_id INT UNIQUE,
phone_no VARCHAR(20)
);
"""

execute_query(connection, create_adm_table) # Execute our defined query
