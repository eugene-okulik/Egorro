import os
import csv
import mysql.connector as mysql
import dotenv

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

with open(file_path, newline='') as csv_file:
    file_data = csv.DictReader(csv_file)
    data = []
    for row in file_data:
        data.append(row)

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor(dictionary=True)

for row in data:
    name = row['name']
    second_name = row['second_name']
    group_title = row['group_title']
    book_title = row['book_title']
    subject_title = row['subject_title']
    lesson_title = row['lesson_title']
    mark_value = row['mark_value']

    query = """
    SELECT
    s.name as 'Имя',
    s.second_name as 'Фамилия',
    g.title as 'Название группы',
    b.title as 'Взятые книги',
    sj.title as 'Предмет',
    l.title as 'Урок',
    m.value as 'Оценка'
    FROM students s
    JOIN `groups` g ON s.group_id = g.id
    JOIN books b ON s.id = b.taken_by_student_id
    JOIN marks m ON s.id = m.student_id
    JOIN lessons l ON l.id = m.lesson_id
    JOIN subjets sj ON sj.id = l.subject_id
    WHERE s.name = %s
    AND s.second_name = %s
    AND g.title = %s
    AND b.title = %s
    AND sj.title = %s
    AND l.title = %s
    AND m.value = %s
    """

    cursor.execute(query, [name, second_name, group_title, book_title, subject_title, lesson_title, mark_value])
    result = cursor.fetchall()

    if result == []:
        print('\nВ базе данных отсутствует запись:')
        for key in row:
            print(f'{key} : {row[key]}')
            