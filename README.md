**#Student Task Tracker**
##Project Description
This project is a continuation of Project 2. In Project 2, I designed the database for a Student Task Tracker system using the tables Students, Categories, and Tasks. In Project 3, I implemented the database as a full-stack Python web application.

##This application helps users manage:

-Students
-Task Categories
-Tasks
-Task Assignments
-Dashboard Summaries

The project uses a normalized relational database and provides a clean web interface for managing records.

##Technology Stack:

-Python 3
-Flask
-SQLite
-SQLAlchemy
-HTML5
-CSS3
-Bootstrap 5
-Jinja2
-Git

##Features:

-CRUD operations for students and tasks
-Category management for organizing tasks
-Relationship views between students and their tasks
-Transaction logic when adding tasks
-Server-side validation for invalid data
-Dashboard with COUNT and AVG summary queries
-Normalized relational database in Third Normal Form (3NF)

##Software Used:
-VS Code for editing the project
-Python 3 to run the application
-Terminal to run commands
-Git for version control
-GitHub to upload the repository
-Chrome or Safari to view the application
-DB Browser for SQLite to inspect the database visually

##Installation Instructions:

-Open the folder in VS Code.
-Open a terminal in the project folder.
-Create a virtual environment:
-python3 -m venv venv
-Activate the virtual environment:
-source venv/bin/activate
-Install dependencies:
-pip install -r requirements.txt
-Run the application:
-python3 app.py
-Open your browser at:
http://127.0.0.1:5000/

##Database Setup:
This application uses SQLite and automatically creates the database the first time the application runs.
To review the final schema separately, use:
schema.sql

##Main Pages:
/
Home page
/students
View all students
/add-student
Add a new student
/tasks
View all tasks
/add-task
Add a new task
/dashboard
View dashboard summaries

##Usage Notes:
-Add students before creating tasks.
-Categories are automatically created when the application starts.
-A task must belong to a valid student and category.
-Empty task titles are not allowed.
-Duplicate student emails are not allowed.
-Tasks with invalid due dates are blocked.

##Relationship Information:
-One student can have many tasks.
-One category can have many tasks.
-Each task belongs to one student and one category.

##Dashboard Features

###The dashboard displays:
-Total students
-Total tasks
-Total categories
-Average days remaining
-Tasks grouped by category

##Data Validation
The application includes server-side validation to prevent invalid data.
-Examples include:
-Empty student names are not allowed
-Empty task titles are not allowed
-Duplicate emails are not allowed
-Invalid due dates are rejected

##Transaction Logic:
The application uses transaction handling when adding tasks.
If a task insertion fails, the database automatically rolls back the transaction to maintain data integrity.

