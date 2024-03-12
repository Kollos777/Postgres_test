from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Group, Teacher, Subject, Grade
from random import randint, choice

engine = create_engine('postgresql+psycopg2://postgres:272100@localhost:5432/postgres')
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

# for _ in range(30, 51):
#     student = Student(name=fake.name())
#     session.add(student)

# groups = ['Group A', 'Group B', 'Group C']
# for group_name in groups:
#     group = Group(name=group_name)
#     session.add(group)

# for _ in range(3, 6):
#     teacher = Teacher(name=fake.name())
#     session.add(teacher)

# subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'History', 'Literature', 'Computer Science', 'Art']
# for subject_name in subjects:
#     teacher_id = randint(1, 3)
#     subject = Subject(name=subject_name, teacher_id=teacher_id)
#     session.add(subject)

# students = session.query(Student).all()
# subjects = session.query(Subject).all()
# for student in students:
#     for subject in subjects:
#         grade = randint(1, 10)
#         grade_record = Grade(student_id=student.id, subject_id=subject.id, grade=grade)
#         session.add(grade_record)

session.commit()
