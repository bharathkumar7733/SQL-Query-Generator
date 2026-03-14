import sqlite3

def run_query(sql):

    conn = sqlite3.connect("college.db")

    cursor = conn.cursor()

    cursor.execute(sql)

    rows = cursor.fetchall()

    conn.close()

    return rows