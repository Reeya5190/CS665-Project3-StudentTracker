from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()


class Student(db.Model):
    __tablename__ = "Students"

    student_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    created_at = db.Column(db.Date, nullable=False, default=date.today)
    metadata = db.Column(db.String(100))

    tasks = db.relationship("Task", backref="student", cascade="all, delete-orphan")


class Category(db.Model):
    __tablename__ = "Categories"

    category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    metadata = db.Column(db.String(100))

    tasks = db.relationship("Task", backref="category")


class Task(db.Model):
    __tablename__ = "Tasks"

    task_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("Students.student_id"), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("Categories.category_id"), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.Date, nullable=False, default=date.today)
    days_remaining = db.Column(db.Integer)
    metadata = db.Column(db.String(100))