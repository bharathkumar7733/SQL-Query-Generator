def generate_sql(user_input):

    user_input = user_input.lower()

    if "all students" in user_input:
        return "SELECT * FROM students"

    elif "cse students" in user_input:
        return "SELECT * FROM students WHERE department='CSE'"

    elif "ece students" in user_input:
        return "SELECT * FROM students WHERE department='ECE'"

    elif "mech students" in user_input:
        return "SELECT * FROM students WHERE department='MECH'"

    elif "marks greater than" in user_input:
        marks = user_input.split("greater than")[1].strip()
        return f"SELECT * FROM students WHERE marks > {marks}"

    elif "marks less than" in user_input:
        marks = user_input.split("less than")[1].strip()
        return f"SELECT * FROM students WHERE marks < {marks}"

    elif "top students" in user_input:
        return "SELECT * FROM students ORDER BY marks DESC LIMIT 3"

    elif "lowest marks" in user_input:
        return "SELECT * FROM students ORDER BY marks ASC LIMIT 3"

    elif "average marks" in user_input:
        return "SELECT AVG(marks) FROM students"

    elif "total students" in user_input:
        return "SELECT COUNT(*) FROM students"

    elif "students sorted by marks" in user_input:
        return "SELECT * FROM students ORDER BY marks DESC"

    else:
        return "Query not understood"