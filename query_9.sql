-- Знайти список курсів, які відвідує певний студент
SELECT DISTINCT subjects.subject_name
FROM subjects
JOIN grades ON subjects.id = grades.subject_id_fn
JOIN students ON grades.student_id_fn = students.id
WHERE students.id = 1;