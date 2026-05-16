# 3rd Normal Form Report

## Project 2 Reference

This Project 3 application directly continues Project 2. The original Project 2 database design used the following entities:

- Students
- Categories
- Tasks

---

# Original Functional Dependencies

Below are the key functional dependencies used in the design.

## Students

- `student_id -> name, email, created_at, metadata`
- `email -> student_id`

## Categories

- `category_id -> name, metadata`

## Tasks

- `task_id -> student_id, category_id, title, due_date, created_at, days_remaining, metadata`

---

# Anomaly Identification

A single large unnormalized table for the entire student task tracking system would create several problems.

## Update Anomaly

If student information appeared in multiple task rows, updating a student email or name would require changes in many places.

## Insertion Anomaly

If task and category information were stored together with student details in one large table, it would be difficult to add a new category or student before any tasks existed.

## Deletion Anomaly

If the last task belonging to a category were deleted from a combined table, important category information could also be lost.

---

# Decomposition Steps

To remove redundancy and preserve data integrity, the design was decomposed into smaller relations.

## Step 1: Separate Student Data

All student-specific attributes were placed into the `Students` table.

## Step 2: Separate Category Data

All category-specific attributes were placed into the `Categories` table.

## Step 3: Separate Task Data

Task-specific attributes were placed into the `Tasks` table, with `student_id` and `category_id` used as foreign keys.

---

# Why the Final Schema Is in 3NF

The final schema satisfies Third Normal Form because:

- each table has a primary key
- every non-key attribute depends on the whole key
- there are no repeating groups
- there are no transitive dependencies between non-key attributes inside the same table
- relationship data is separated using foreign keys

---

# Final Relational Schema

## Students

`Students(student_id, name, email, created_at, metadata)`

## Categories

`Categories(category_id, name, metadata)`

## Tasks

`Tasks(task_id, student_id, category_id, title, due_date, created_at, days_remaining, metadata)`

---

# Relationship Information

- One student can have many tasks.
- One category can have many tasks.
- Each task belongs to one student and one category.

The relationship between Students and Tasks is one-to-many.  
The relationship between Categories and Tasks is one-to-many.

---

# Final Notes

This final schema is the schema used by Python in Project 3. It is a direct continuation of the Project 2 ERD and preserves the original Student Task Tracker subject while improving implementation readiness, reducing redundancy, and maintaining data integrity.