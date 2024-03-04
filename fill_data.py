import faker
from random import randint
import sqlite3
import random

NUM_STUDENTS = randint(30, 50)
NUM_GROUPS = 3
NUM_SUBJECTS = randint(5, 8)
NUM_TEACHERS = randint(3, 5)
MAX_GRADES_PER_STUDENT = 20

conn = sqlite3.connect('salary.db')
cursor = conn.cursor()
fake_data = faker.Faker()
group_names = [fake_data.word() for _ in range(NUM_GROUPS)]
teacher_names = [fake_data.name() for _ in range(NUM_TEACHERS)]

for group_name in group_names:
    cursor.execute(f"INSERT INTO groups (group_name) VALUES (?)", (group_name,))
    group_id_fn = cursor.lastrowid
    for _ in range(NUM_STUDENTS // NUM_GROUPS):
        student_name = fake_data.name()
        cursor.execute("INSERT INTO students (student_name, group_id_fn) VALUES (?, ?)", (student_name, group_id_fn))

for teacher_name in teacher_names:
    cursor.execute("INSERT INTO teachers (teacher_name) VALUES (?)", (teacher_name,))
    teacher_id_fn = cursor.lastrowid
    subjects = [fake_data.word() for _ in range(NUM_SUBJECTS)]
    for subject_name in subjects:
        cursor.execute("INSERT INTO subjects (subject_name, teacher_id_fn) VALUES (?, ?)", (subject_name, teacher_id_fn))

        subject_id = cursor.lastrowid
        for student_id in range(1, NUM_STUDENTS + 1):
            num_grades = random.randint(1, MAX_GRADES_PER_STUDENT)
            for _ in range(num_grades):
                grade = random.randint(1, 100)
                data = fake_data.date_time_between(start_date="-1y", end_date="now")
                cursor.execute("INSERT INTO grades (student_id_fn, subject_id_fn, grade, data) VALUES (?, ?, ?, ?)", (student_id, subject_id, grade, data))
conn.commit()
conn.close()