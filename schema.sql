DROP TABLE IF EXISTS Tasks;
DROP TABLE IF EXISTS Categories;
DROP TABLE IF EXISTS Students;

CREATE TABLE Students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at DATE NOT NULL,
    metadata VARCHAR(100)
);

CREATE TABLE Categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL UNIQUE,
    metadata VARCHAR(100)
);

CREATE TABLE Tasks (
    task_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    title VARCHAR(255) NOT NULL,
    due_date DATE NOT NULL,
    created_at DATE NOT NULL,
    days_remaining INTEGER,
    metadata VARCHAR(100),

    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (category_id) REFERENCES Categories(category_id)
);

INSERT INTO Students (name, email, created_at, metadata) VALUES
('Alice', 'alice@gmail.com', '2026-01-01', 'admin'),
('Bob', 'bob@icloud.com', '2026-01-02', 'admin'),
('Charlie', 'charlie@email.com', '2026-01-03', 'admin'),
('David', 'david@email.com', '2026-01-04', 'admin'),
('Eve', 'eve@gmail.com', '2026-01-05', 'admin');

INSERT INTO Categories (name, metadata) VALUES
('Homework', 'system'),
('Exam', 'system'),
('Project', 'system'),
('Quiz', 'system'),
('Other', 'system');

INSERT INTO Tasks (student_id, category_id, title, due_date, created_at, days_remaining, metadata) VALUES
(1, 1, 'Math HW', '2026-04-30', '2026-04-01', 29, 'admin'),
(2, 2, 'Midterm', '2026-04-25', '2026-04-02', 23, 'admin'),
(3, 3, 'Final Project', '2026-05-01', '2026-04-03', 28, 'admin'),
(4, 4, 'Quiz 1', '2026-04-15', '2026-04-04', 11, 'admin'),
(2, 1, 'Science HW', '2026-04-22', '2026-04-06', 16, 'admin');