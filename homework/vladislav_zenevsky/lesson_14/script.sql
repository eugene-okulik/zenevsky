INSERT INTO students (name, second_name) VALUES ('Vladislav', 'Zenevsky');

SELECT * FROM students s WHERE second_name = 'Zenevsky';

INSERT INTO books (title, taken_by_student_id) VALUES ('The Catcher in the Rye', 3740);

INSERT INTO books (title, taken_by_student_id) VALUES ('To Kill a Mockingbird', 3740);

INSERT INTO books (title, taken_by_student_id) VALUES ('Brave New World', 3740);

SELECT * FROM books b WHERE taken_by_student_id = 3740;

INSERT INTO `groups` (title, start_date, end_date) VALUES ('Writers', 'Dec 2024', 'Dec 2025');

SELECT * FROM `groups` WHERE title = 'Writers';

UPDATE students SET group_id = 2370 WHERE id = 3740;

INSERT INTO subjets (title) VALUES ('Creative Writing');

INSERT INTO subjets (title) VALUES ('Literary Analysis');

INSERT INTO subjets (title) VALUES ('Narrative Techniques');

SELECT * FROM subjets WHERE title IN ('Creative Writing', 'Literary Analysis', 'Narrative Techniques');

INSERT INTO lessons (title, subject_id) VALUES ('Developing Unique Characters', 3628);

INSERT INTO lessons (title, subject_id) VALUES ('Crafting Compelling Dialogues', 3628);

INSERT INTO lessons (title, subject_id) VALUES ('Deconstructing Symbolism in Classic Literature', 3629);

INSERT INTO lessons (title, subject_id) VALUES ('Comparative Analysis of Literary Movements', 3629);

INSERT INTO lessons (title, subject_id) VALUES ('Exploring Nonlinear Storytelling', 3630);

INSERT INTO lessons (title, subject_id) VALUES ('Mastering the Use of Perspective and Voice', 3630);

SELECT * FROM lessons l WHERE l.subject_id IN (3628, 3629, 3630);

INSERT INTO marks (value, lesson_id, student_id) VALUES ('5', 7128, 3740);

INSERT INTO marks (value, lesson_id, student_id) VALUES ('5', 7129, 3740);

INSERT INTO marks (value, lesson_id, student_id) VALUES ('4', 7130, 3740);

INSERT INTO marks (value, lesson_id, student_id) VALUES ('3', 7131, 3740);

INSERT INTO marks (value, lesson_id, student_id) VALUES ('4', 7132, 3740);

INSERT INTO marks (value, lesson_id, student_id) VALUES ('5', 7133, 3740);

SELECT * FROM marks m WHERE student_id = 3740;

SELECT * FROM books b WHERE taken_by_student_id = 3740;

SELECT * 
FROM students s 
JOIN books b ON b.taken_by_student_id = s.id 
JOIN `groups` g ON g.id = s.group_id 
JOIN marks m ON m.student_id = s.id 
JOIN lessons l ON l.id = m.lesson_id 
JOIN subjets s2 ON s2.id = l.subject_id 
WHERE s.id = 3740;
