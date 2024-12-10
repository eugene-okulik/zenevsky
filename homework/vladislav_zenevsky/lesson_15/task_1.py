import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

insert_query = "INSERT INTO students (name, second_name) VALUES (%s, %s)"
cursor.execute(insert_query, ('Polina', 'Shalina'))
student_id = cursor.lastrowid

insert_query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
cursor.executemany(
    insert_query, [
        ('The Lord of the Rings', student_id),
        ('Pride and Prejudice', student_id),
        ('The Alchemist', student_id)
    ]
)

insert_query = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
cursor.execute(insert_query, ('Pro Writers', 'Jun 2020', 'Jul 2050'))
group_id = cursor.lastrowid

update_query = f"UPDATE students SET group_id = {group_id} WHERE id = {student_id}"
cursor.execute(update_query)

insert_values = [('Scriptwriting',), ('Poetry and Poetics',), ('Editing and Publishing',)]
insert_query = "INSERT INTO subjets (title) VALUES (%s)"
subject_id_list = []
for value in insert_values:
    cursor.execute(insert_query, value)
    subject_id_list.append(cursor.lastrowid)
subject_1, subject_2, subject_3 = subject_id_list

insert_values = [
    ('Writing Dialogue for Film and Television', subject_1),
    ('Structuring a Three-Act Screenplay', subject_1),
    ('Exploring Modern Poetic Forms', subject_2),
    ('Analyzing the Use of Metaphor and Symbolism in Poetry', subject_2),
    ('Manuscript Editing Techniques', subject_3),
    ('Fundamentals of Digital Publishing and Layout Design', subject_3)
]
insert_query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
lessons_id_list = []
for value in insert_values:
    cursor.execute(insert_query, value)
    lessons_id_list.append(cursor.lastrowid)
lesson_1, lesson_2, lesson_3, lesson_4, lesson_5, lesson_6 = lessons_id_list

insert_query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
cursor.executemany(
    insert_query, [
        ('5', lesson_1, student_id),
        ('4', lesson_2, student_id),
        ('5', lesson_3, student_id),
        ('4', lesson_4, student_id),
        ('5', lesson_5, student_id),
        ('4', lesson_6, student_id),
    ]
)

cursor.execute(f"SELECT * FROM marks WHERE student_id = {student_id}")
print(cursor.fetchall())

cursor.execute(f"SELECT * FROM books WHERE taken_by_student_id = {student_id}")
print(cursor.fetchall())

select_query = f'''
SELECT *
FROM students s
JOIN books b ON b.taken_by_student_id = s.id
JOIN `groups` g ON g.id = s.group_id
JOIN marks m ON m.student_id = s.id
JOIN lessons l ON l.id = m.lesson_id
JOIN subjets s2 ON s2.id = l.subject_id
WHERE s.id = {student_id};
'''

cursor.execute(select_query)
print(cursor.fetchall())

db.commit()

db.close()
