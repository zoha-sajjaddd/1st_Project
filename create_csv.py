import pandas as pd

# Define the expanded, high-performing and balanced student data
data = {
    'stu_hours': [45, 48, 42, 38, 36, 33, 30, 25, 22, 18, 15, 10, 5],
    'attendance': [100, 100, 98, 96, 95, 92, 90, 85, 82, 78, 75, 60, 50],
    'eng': [98, 100, 95, 90, 85, 82, 80, 75, 70, 65, 60, 50, 40],
    'isl': [95, 98, 92, 88, 85, 80, 78, 75, 72, 68, 65, 55, 45],
    'maths': [98, 100, 96, 92, 90, 88, 85, 75, 72, 68, 65, 50, 40],
    'statistics': [96, 99, 94, 90, 88, 85, 82, 78, 75, 65, 60, 52, 42],
    'linear_algebra': [98, 99, 95, 91, 87, 84, 80, 72, 70, 65, 62, 50, 40],
    'total_marks': [485, 496, 472, 449, 435, 419, 405, 380, 361, 331, 312, 257, 207],
    'grade': ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'D', 'D', 'F', 'F']
}

# Convert to DataFrame and save as CSV
df = pd.DataFrame(data)
df.to_csv('additional_data.csv', index=False)
print("✔ Successfully created the expanded 'additional_data.csv'!")