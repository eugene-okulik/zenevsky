import os
import mysql.connector as mysql
import dotenv
import csv

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor(dictionary=True)

select_query = '''
SELECT
s.name,
s.second_name,
g.title AS group_title,
b.title AS book_title,
s2.title AS subject_title,
l.title AS lesson_title,
m.value AS mark_value
FROM students s
JOIN books b ON b.taken_by_student_id = s.id
JOIN `groups` g ON g.id = s.group_id
JOIN marks m ON m.student_id = s.id
JOIN lessons l ON l.id = m.lesson_id
JOIN subjets s2 ON s2.id = l.subject_id
WHERE s.name IN (%s, %s, %s) AND s.second_name IN (%s, %s, %s)
'''

cursor.execute(select_query, ('Ivan', 'Petr', 'Mark', 'Petrov', 'Ivanov', 'Pavlov'))
db_data = cursor.fetchall()

db.close()

base_path = os.path.dirname(__file__)

homework_path = os.path.dirname(os.path.dirname(base_path))

eugene_file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

with open(eugene_file_path, newline='') as csv_file:
    file_data = csv.DictReader(csv_file)
    for row in file_data:
        if row not in db_data:
            print(row)
