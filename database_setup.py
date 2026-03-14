import sqlite3

# connect to database
conn = sqlite3.connect("college.db")

cursor = conn.cursor()

# create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    marks INTEGER
)
""")

# insert data
students = [
(1,"Rahul","CSE",85),
(2,"Anita","ECE",78),
(3,"Kiran","CSE",92),
(4,"Meena","MECH",67),
(5,"Arjun","CSE",74)
]

cursor.executemany("INSERT INTO students VALUES(?,?,?,?)", students)

conn.commit()
conn.close()

print("Database created successfully!")