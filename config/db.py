import mysql.connector

BASE = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='blog',
    port=3306
)