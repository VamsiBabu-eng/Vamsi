import mysql.connector

dbc = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Dark@559",
    database="d12_pdbc"
)

cursor_ = dbc.cursor()
cursor_.execute("USE d12_pdbc")

# Create table
cursor_.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    course VARCHAR(100),
    password VARCHAR(100)
)
""")


# Insert
cursor_.execute(
    "INSERT INTO students (name, email, course, password) VALUES (%s, %s, %s, %s)",
    ("vamsi", "vamsi@gmail.com", "Data Science", "pass123")
)

dbc.commit()

# Fetch
cursor_.execute("SELECT * FROM students")
for i in cursor_.fetchall():
    print(i)

cursor_.close()
dbc.close()