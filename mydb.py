# Importing library for mysql
import mysql.connector

# Create an instance for the database
dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password123'
)

# Prepare a cursor object
cursorObject = dataBase.cursor()

# Create database
cursorObject.execute("CREATE DATABASE crm_db_practice")

print("All Done")