-- Знайти середній бал, який ставить певний викладач зі своїх предметів
SELECT AVG(grade) AS avg_grade
FROM subjects
JOIN grades ON subjects.id = grades.subject_id_fn
WHERE teacher_id_fn = 1;