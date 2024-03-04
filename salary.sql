CREATE TABLE students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_name VARCHAR(255) UNIQUE NOT NULL,
                group_id_fn INTEGER,
                FOREIGN KEY (group_id_fn) REFERENCES groups(id)
                ON DELETE CASCADE
                ON UPDATE CASCADE
                );

CREATE TABLE groups (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                group_name VARCHAR(255) UNIQUE NOT NULL
                );

CREATE TABLE teachers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                teacher_name VARCHAR(255) UNIQUE NOT NULL
                );

CREATE TABLE subjects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                subject_name VARCHAR(255) UNIQUE NOT NULL,
                teacher_id_fn INTEGER,
                FOREIGN KEY (teacher_id_fn) REFERENCES teachers(id)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE
                );

CREATE TABLE grades (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id_fn INTEGER,
                subject_id_fn INTEGER,
                grade INTEGER,
                data timestamp,
                FOREIGN KEY (student_id_fn) REFERENCES students(id),
                FOREIGN KEY (subject_id_fn) REFERENCES subjects(id)
                );
