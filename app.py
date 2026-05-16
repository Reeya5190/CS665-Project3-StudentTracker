from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Student, Category, Task
from datetime import datetime, date

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tracker.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "student-task-secret"

db.init_app(app)


@app.before_request
def create_tables():
    db.create_all()

    if Category.query.count() == 0:
        categories = [
            Category(name="Homework", metadata="system"),
            Category(name="Exam", metadata="system"),
            Category(name="Project", metadata="system"),
            Category(name="Quiz", metadata="system"),
            Category(name="Other", metadata="system")
        ]
        db.session.add_all(categories)
        db.session.commit()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/students")
def students():
    all_students = Student.query.all()
    return render_template("students.html", students=all_students)


@app.route("/add-student", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        name = request.form["name"].strip()
        email = request.form["email"].strip()

        if not name:
            flash("Student name cannot be empty.")
            return redirect(url_for("add_student"))

        if not email:
            flash("Email cannot be empty.")
            return redirect(url_for("add_student"))

        existing_student = Student.query.filter_by(email=email).first()
        if existing_student:
            flash("Email already exists.")
            return redirect(url_for("add_student"))

        student = Student(
            name=name,
            email=email,
            created_at=date.today(),
            metadata="created_by_user"
        )

        db.session.add(student)
        db.session.commit()

        flash("Student added successfully.")
        return redirect(url_for("students"))

    return render_template("add_student.html")


@app.route("/delete-student/<int:student_id>")
def delete_student(student_id):
    student = Student.query.get_or_404(student_id)

    db.session.delete(student)
    db.session.commit()

    flash("Student deleted successfully.")
    return redirect(url_for("students"))


@app.route("/tasks")
def tasks():
    all_tasks = Task.query.all()
    return render_template("tasks.html", tasks=all_tasks)


@app.route("/add-task", methods=["GET", "POST"])
def add_task():
    students = Student.query.all()
    categories = Category.query.all()

    if request.method == "POST":
        title = request.form["title"].strip()
        student_id = request.form["student_id"]
        category_id = request.form["category_id"]
        due_date_input = request.form["due_date"]

        if not title:
            flash("Task title cannot be empty.")
            return redirect(url_for("add_task"))

        if not student_id or not category_id:
            flash("Student and category are required.")
            return redirect(url_for("add_task"))

        due_date = datetime.strptime(due_date_input, "%Y-%m-%d").date()
        today = date.today()

        if due_date < today:
            flash("Due date cannot be in the past.")
            return redirect(url_for("add_task"))

        days_remaining = (due_date - today).days

        try:
            task = Task(
                title=title,
                student_id=student_id,
                category_id=category_id,
                due_date=due_date,
                created_at=today,
                days_remaining=days_remaining,
                metadata="created_by_user"
            )

            db.session.add(task)
            db.session.commit()

            flash("Task added successfully.")
            return redirect(url_for("tasks"))

        except Exception:
            db.session.rollback()
            flash("Transaction failed. Task was not added.")
            return redirect(url_for("add_task"))

    return render_template("add_task.html", students=students, categories=categories)


@app.route("/edit-task/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    students = Student.query.all()
    categories = Category.query.all()

    if request.method == "POST":
        title = request.form["title"].strip()
        due_date_input = request.form["due_date"]

        if not title:
            flash("Task title cannot be empty.")
            return redirect(url_for("edit_task", task_id=task_id))

        due_date = datetime.strptime(due_date_input, "%Y-%m-%d").date()
        today = date.today()

        task.title = title
        task.student_id = request.form["student_id"]
        task.category_id = request.form["category_id"]
        task.due_date = due_date
        task.days_remaining = (due_date - today).days
        task.metadata = "updated_by_user"

        db.session.commit()

        flash("Task updated successfully.")
        return redirect(url_for("tasks"))

    return render_template(
        "edit_task.html",
        task=task,
        students=students,
        categories=categories
    )


@app.route("/delete-task/<int:task_id>")
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)

    db.session.delete(task)
    db.session.commit()

    flash("Task deleted successfully.")
    return redirect(url_for("tasks"))


@app.route("/dashboard")
def dashboard():
    total_students = Student.query.count()
    total_tasks = Task.query.count()
    total_categories = Category.query.count()

    avg_days = db.session.query(db.func.avg(Task.days_remaining)).scalar()

    tasks_by_category = (
        db.session.query(Category.name, db.func.count(Task.task_id))
        .join(Task, Category.category_id == Task.category_id)
        .group_by(Category.name)
        .all()
    )

    return render_template(
        "dashboard.html",
        total_students=total_students,
        total_tasks=total_tasks,
        total_categories=total_categories,
        avg_days=avg_days,
        tasks_by_category=tasks_by_category
    )


if __name__ == "__main__":
    app.run(debug=True)