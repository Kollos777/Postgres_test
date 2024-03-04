-- Знайти середній бал у групах з певного предмета:
SELECT group_name, AVG(grade) AS avg_grade
FROM groups
JOIN students ON groups.id = students.group_id_fn
JOIN grades ON students.id = grades.student_id_fn
WHERE subject_id_fn = 1
GROUP BY group_name;