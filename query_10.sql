-- Список курсів, які певний студент читає певному викладачу:
SELECT DISTINCT subject_name
FROM subjects
JOIN grades ON subjects.id = grades.subject_id_fn
JOIN students ON students.id = grades.student_id_fn
WHERE students.id = 1 AND subjects.teacher_id_fn = 1;
