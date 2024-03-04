from datetime import datetime
import faker
from random import randint, choice
import sqlite3

NUMBER_STUDENTS = 3
NUMBER_GROUPS = 3
NUMBER_TEACHERS = 5
NUMBER_SUBJECTS= 8
NUMBER_TEACHERS = 5


def generate_fake_data(number_students, number_groups, number_teachers, number_subjects) -> tuple:
    fake = faker.Faker()

    students = [(fake.name(), randint(1, NUMBER_GROUPS)) for _ in range(number_students)]
    groups = [(f"Group {i}",) for i in range(1, number_groups + 1)]
    teachers = [(fake.name(),) for _ in range(number_teachers)]
    subjects = [(fake.word(), randint(1, NUMBER_TEACHERS)) for _ in range(number_subjects)]

    return students, groups, teachers, subjects

def prepare_data(students, groups, teachers, subjects) -> tuple:
    # Generate grades for each student in each subject
    grades = []
    for student in students:
        student_id = students.index(student) + 1
        for subject in subjects:
            subject_id = subjects.index(subject) + 1
            grade = randint(1, 10)  # Assuming grades are between 1 and 10
            grades.append((student_id, subject_id, grade))

    return students, groups, teachers, subjects, grades

def insert_data_to_db(students, groups, teachers, subjects, grades) -> None:
    with sqlite3.connect('school.db') as con:
        cur = con.cursor()

        # Insert groups
        cur.executemany("INSERT INTO groups (group_name) VALUES (?)", groups)

        # Insert teachers
        cur.executemany("INSERT INTO teachers (teacher_name) VALUES (?)", teachers)

        # Insert subjects
        cur.executemany("INSERT INTO subjects (subject_name, teacher_id) VALUES (?, ?)", subjects)

        # Insert students
        cur.executemany("INSERT INTO students (student_name, group_id) VALUES (?, ?)", students)

        # Insert grades
        cur.executemany("INSERT INTO grades (student_id, subject_id, grade) VALUES (?, ?, ?)", grades)

        con.commit()

if __name__ == "__main__":
    students, groups, teachers, subjects = generate_fake_data(NUMBER_STUDENTS, NUMBER_GROUPS, NUMBER_TEACHERS, NUMBER_SUBJECTS)
    students, groups, teachers, subjects, grades = prepare_data(students, groups, teachers, subjects)
    insert_data_to_db(students, groups, teachers, subjects, grades)