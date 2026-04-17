import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Dark@559",
    database="rl"
)
if conn.is_connected():
    print("connected")