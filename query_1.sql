-- Знайти 5 студентів із найбільшим середнім балом з усіх предметів:
SELECT student_name, AVG(grade) AS avg_grade
FROM students
JOIN grades ON students.id = grades.student_id_fn
GROUP BY student_name
ORDER BY avg_grade DESC
LIMIT 5;
