import sqlite3

conn = sqlite3.connect('student_raw_database.sqlite')
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Tables found in database:", tables)
conn.close()