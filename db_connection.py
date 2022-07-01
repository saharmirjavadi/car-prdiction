import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv('.env')


class DatabaseOperation:
    def __init__(self) -> None:
        self.cnx = mysql.connector.connect(user=os.getenv('DB_USER'),
                                           password=os.getenv('DB_PASSWORD'),
                                           host=os.getenv('DB_HOST'))
        self.cursor = self.cnx.cursor()

    def execute_query(self, query):
        self.cursor.execute(query)

    def create_table(self):
        self.cursor.execute('CREATE DATABASE IF NOT EXISTS %s' % os.getenv('DB_NAME'))
        self.cursor.execute('USE %s' % os.getenv('DB_NAME'))
        self.cursor.execute('CREATE TABLE IF NOT EXISTS cars (name VARCHAR(255),place VARCHAR(255), output VARCHAR(255), year VARCHAR(255) ,price VARCHAR(255))')
        self.cursor.execute('DELETE FROM cars')

    def inset_data(self, kwargs):
        self.execute_query('insert into cars VALUES(\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')' % (
            kwargs["name"], 
            kwargs["place"], 
            kwargs["output"], 
            kwargs["year"], 
            kwargs["price"]))
        self.cnx.commit()
        self.close_connection()

    def close_connection(self):
        self.cursor.close()
        self.cnx.close()
