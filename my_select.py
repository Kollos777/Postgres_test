from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from models import Student, Grade, Group, Subject, Teacher, engine

Session = sessionmaker(bind=engine)
session = Session()

def select_1():
    top_students = session.query(Grade.student_id, func.avg(Grade.grade).label('average_grade')) \
        .group_by(Grade.student_id) \
        .order_by(func.avg(Grade.grade).desc()) \
        .limit(5) \
        .all()
    return top_students

def select_2(subject_id):
    top_student = session.query(Grade.student_id, func.avg(Grade.grade).label('average_grade')) \
        .filter_by(subject_id=subject_id) \
        .group_by(Grade.student_id) \
        .order_by(func.avg(Grade.grade).desc()) \
        .first()
    return top_student

def select_3(subject_id):
    avg_grade_by_group = session.query(Group.name, func.avg(Grade.grade).label('average_grade')) \
        .join(Student) \
        .filter(Grade.subject_id == subject_id) \
        .group_by(Group.name) \
        .all()
    return avg_grade_by_group

def select_4():
    avg_grade_overall = session.query(func.avg(Grade.grade).label('average_grade')).scalar()
    return avg_grade_overall

def select_5(teacher_id):
    courses_taught = session.query(Subject.name) \
        .filter_by(teacher_id=teacher_id) \
        .all()
    return courses_taught

def select_6(group_id):
    students_in_group = session.query(Student.fullname) \
        .filter_by(group_id=group_id) \
        .all()
    return students_in_group

def select_7(group_id, subject_id):
    grades_in_group = session.query(Student.fullname, Grade.grade) \
        .join(Grade) \
        .filter(Student.group_id == group_id, Grade.subject_id == subject_id) \
        .all()
    return grades_in_group

def select_8(teacher_id):
    avg_grade_by_teacher = session.query(func.avg(Grade.grade).label('average_grade')) \
        .join(Subject) \
        .filter(Subject.teacher_id == teacher_id) \
        .scalar()
    return avg_grade_by_teacher

def select_9(student_id):
    courses_attended = session.query(Subject.name) \
        .join(Grade) \
        .filter(Grade.student_id == student_id) \
        .all()
    return courses_attended

def select_10(student_id, teacher_id):
    courses_taught_to_student = session.query(Subject.name) \
        .join(Grade) \
        .filter(Grade.student_id == student_id, Subject.teacher_id == teacher_id) \
        .all()
    return courses_taught_to_student
