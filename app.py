from flask import Flask, request, render_template
from sql_generator import generate_sql
from execute_query import run_query

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():

    results = []
    sql = ""

    if request.method == "POST":

        user_query = request.form["query"]

        sql = generate_sql(user_query)

        if sql != "Query not understood":
            results = run_query(sql)

    return render_template("index.html", results=results, sql=sql)

import os

if __name__ == "__main__":
    app.run(debug=True)
