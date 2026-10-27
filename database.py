import sqlite3
import pandas as pd
import numpy as np
import os

def create_database():
    db_path = 'students.db'
    
    # Connects to SQLite (creates 'students.db' in the current folder if it doesn't exist)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create the raw student table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students_raw (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            stu_hours REAL,
            attendance REAL,
            eng REAL,
            isl REAL,
            maths REAL,
            statistics REAL,
            linear_algebra REAL,
            total_marks REAL
        )
    ''')
    
    # Check if table already has data
    cursor.execute("SELECT COUNT(*) FROM students_raw")
    count = cursor.fetchone()[0]
    
    if count == 0:
        # Generate 500 realistic raw student records
        np.random.seed(42)
        n_rows = 500
        
        stu_hours = np.random.randint(5, 45, n_rows)
        attendance = np.random.randint(50, 100, n_rows)
        eng = np.random.randint(40, 95, n_rows)
        isl = np.random.randint(40, 95, n_rows)
        maths = np.random.randint(40, 95, n_rows)
        statistics = np.random.randint(40, 95, n_rows)
        linear_algebra = np.random.randint(40, 95, n_rows)
        total_marks = eng + isl + maths + statistics + linear_algebra
        
        df = pd.DataFrame({
            'stu_hours': stu_hours,
            'attendance': attendance,
            'eng': eng,
            'isl': isl,
            'maths': maths,
            'statistics': statistics,
            'linear_algebra': linear_algebra,
            'total_marks': total_marks
        })
        
        df.to_sql('students_raw', conn, if_exists='append', index=False)
        print("✔ Successfully created 'students.db' and populated 500 raw student records!")
    else:
        print("✔ 'students.db' already exists and contains data.")
        
    conn.close()

if __name__ == '__main__':
    create_database()