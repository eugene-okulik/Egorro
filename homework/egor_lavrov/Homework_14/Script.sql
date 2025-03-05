INSERT INTO students (name, second_name, group_id)
VALUES ('Barry', 'Allen', 3071)

INSERT INTO books (title, taken_by_student_id)
VALUES ('Star Wars. Episode I. The Phantom Menace', 4770), ('Who is the Flash?', 4770)

INSERT INTO `groups` (title)
VALUES ('STAR Labs')

INSERT INTO subjets (title)
VALUES ('Logic'), ('Piano')

INSERT INTO lessons (title, subject_id)
VALUES ('Lesson 1: What is logic?', 5043),
('Lesson 2: The history of the evolution of logic', 5043),
('Lesson 1: Introduction', 5044),
('Lesson 2: How the piano works?', 5044)

INSERT INTO marks (value, lesson_id, student_id)
VALUES 
(5, 9111, 4770),
(4, 9112, 4770),
(4, 9113, 4770),
(5, 9114, 4770)

SELECT value
FROM marks
WHERE student_id  = 4770

SELECT title
FROM books
WHERE taken_by_student_id  = 4770

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
WHERE s.id = 4770