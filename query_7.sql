-- Знайти оцінки студентів у окремій групі з певного предмета
SELECT student_name, grade 
FROM students
JOIN grades ON students.id = grades.student_id_fn
WHERE group_id_fn = 1 AND subject_id_fn = 1