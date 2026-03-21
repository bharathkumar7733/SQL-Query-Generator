# Natural Language to SQL Query Generator
https://sql-query-generator2.vercel.app/
## Project Overview

The **Natural Language to SQL Query Generator** is a Python-based web application that allows users to query a database using **plain English instead of writing SQL queries manually**.

The system converts natural language input into SQL queries, executes them on a SQLite database, and displays the results through a web interface.

This project demonstrates the integration of **Natural Language Processing concepts, SQL databases, and web application development using Flask**.

---

## Features

* Convert **English queries into SQL statements**.
* Execute SQL queries on a **SQLite database**
* Display query results in a **web interface**
* Support filtering, sorting, and analytical queries
* Simple and clean **Flask-based web application
* Beginner-friendly **rule-based NLP system**

---

## Example Queries

Users can ask questions like:

```
show all students
show cse students
show students marks greater than 80
show students marks less than 70
show top students
show average marks
show total students
```

Generated SQL example:

```
SELECT * FROM students WHERE marks > 80;
```

---

## Tech Stack

* **Python**
* **SQL**
* **SQLite**
* **Flask**
* **HTML / CSS**

---

## Project Architecture

```
User Input (Browser)
        ↓
Flask Web Application
        ↓
Natural Language Processing Logic
(sql_generator.py)
        ↓
Generated SQL Query
        ↓
Database Execution
(SQLite)
        ↓
Results Displayed in Browser
```

---

## Project Structure

```
sql-query-generator
│
├── app.py
├── sql_generator.py
├── execute_query.py
├── database_setup.py
│
├── templates
│     └── index.html
│
├── college.db
└── README.md
```

---

## How to Run the Project

### Step 1: Clone the Repository

```
git clone https://github.com/your-username/sql-query-generator.git
```

### Step 2: Navigate to the Project Folder

```
cd sql-query-generator
```

### Step 3: Install Required Libraries

```
pip install flask pandas nltk
```

### Step 4: Create the Database

```
python database_setup.py
```

### Step 5: Run the Flask Application

```
python app.py
```

### Step 6: Open in Browser

```
http://127.0.0.1:5000
```

---

## Challenges Faced

* Understanding different natural language query formats
* Extracting numeric values from user input
* Handling invalid queries gracefully

---

## Limitations

* Uses **rule-based NLP**, so it cannot understand complex sentences
* Currently supports only a **single database table**
* Limited query patterns

---

## Future Improvements

* Integrate **AI-based Text-to-SQL models**
* Support **multiple database tables**
* Add **voice-based queries**
* Improve UI with modern frontend frameworks
* Deploy the application online

---

## Learning Outcomes

Through this project, I learned:

* How to integrate **Python with SQL databases**
* How to build **web applications using Flask**
* Basic concepts of **Natural Language Processing**
* How backend logic interacts with databases

---

## Author

**Bharath Kumar**

Computer Science Student
Interested in **AI, Web Development, and Software Engineering**

---
