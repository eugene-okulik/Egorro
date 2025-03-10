import mysql.connector as mysql


db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

query = """
INSERT INTO students (name, second_name)
VALUES ('Barry', 'Allen')
"""
cursor.execute(query)
student_id = cursor.lastrowid


query = """
INSERT INTO books (title, taken_by_student_id)
VALUES (%s, %s)
"""
cursor.executemany(
    query,[
        ('Star Wars. Episode I: The Phantom Menace', student_id),
        ('Who is the Flash?', student_id)
    ]
)


query = """
INSERT INTO `groups` (title, start_date, end_date)
VALUES ('STAR Labs', 2015, 2023)
"""
cursor.execute(query)
group_id = cursor.lastrowid


query = """
UPDATE students
SET group_id  = %s
WHERE id = %s
"""
cursor.execute(query, [group_id, student_id])


query = """
INSERT INTO subjets (title)
VALUES ('Logic')
"""
cursor.execute(query)
subject_logic_id = cursor.lastrowid


query = """
INSERT INTO subjets (title)
VALUES ('Piano')
"""
cursor.execute(query)
subject_piano_id = cursor.lastrowid


query = """
INSERT INTO lessons (title, subject_id)
VALUES ('Lesson 1: What is logic?', %s)
"""
cursor.execute(query, [subject_logic_id])
lesson_logic_01_id = cursor.lastrowid


query = """
INSERT INTO lessons (title, subject_id)
VALUES ('Lesson 2: The history of the evolution of logic', %s)
"""
cursor.execute(query, [subject_logic_id])
lesson_logic_02_id = cursor.lastrowid


query = """
INSERT INTO lessons (title, subject_id)
VALUES ('Lesson 1: Introduction', %s)
"""
cursor.execute(query, [subject_piano_id])
lesson_piano_01_id = cursor.lastrowid


query = """
INSERT INTO lessons (title, subject_id)
VALUES ('Lesson 2: How the piano works?', %s)
"""
cursor.execute(query, [subject_piano_id])
lesson_piano_02_id = cursor.lastrowid


query = f"""
INSERT INTO marks (value, lesson_id, student_id)
VALUES (%s, %s, %s)
"""
cursor.executemany(
    query, [
        (5, lesson_logic_01_id, student_id),
        (4, lesson_logic_02_id, student_id),
        (4, lesson_piano_01_id, student_id),
        (5, lesson_piano_02_id, student_id)
    ])


query = """
SELECT value
FROM marks
WHERE student_id  = %s
"""
cursor.execute(query, [student_id])
print(cursor.fetchall())


query = """
SELECT title
FROM books
WHERE taken_by_student_id  = %s
"""
cursor.execute(query, [student_id])
print(cursor.fetchall())


query = """
SELECT
s.id as 'ID',
s.name as 'Имя',
s.second_name as 'Фамилия',
s.group_id as 'ID группы',
b.title as 'Взятые книги',
g.title as 'Название группы',
g.start_date as 'Старт группы',
g.end_date as 'Окончание группы',
sj.title as 'Предмет',
l.title as 'Урок',
m.value as 'Оценка'
FROM students s
JOIN `groups` g ON s.group_id = g.id
JOIN books b ON s.id = b.taken_by_student_id
JOIN marks m ON s.id = m.student_id
JOIN lessons l ON l.id = m.lesson_id
JOIN subjets sj ON sj.id = l.subject_id
WHERE s.id = %s
"""
cursor.execute(query, [student_id])
print(cursor.fetchall())


print(f'ID студента: {student_id}')
print(f'ID группы: {group_id}')
print(f'ID Логики: {subject_logic_id}')
print(f'ID Пианино: {subject_piano_id}')
print((f'ID урока по логике 1: {lesson_logic_01_id}'))
print((f'ID урока по логике 2: {lesson_logic_02_id}'))
print((f'ID урока по пианино 1: {lesson_piano_01_id}'))
print((f'ID урока по пианино 1: {lesson_piano_02_id}'))

db.commit()
db.close()
