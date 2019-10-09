import mysql.connector
def get_connection():
    db=mysql.connector.connect(host="localhost",user="root",password="Password@123",database="luminar")
    return db