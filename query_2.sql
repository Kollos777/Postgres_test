-- Знайти студента із найвищим середнім балом з певного предмета:
SELECT student_name, AVG(grade) AS avg_grade
FROM students
JOIN grades ON students.id = grades.student_id_fn
WHERE subject_id_fn = 1
GROUP BY student_name
ORDER BY avg_grade DESC
LIMIT 1;