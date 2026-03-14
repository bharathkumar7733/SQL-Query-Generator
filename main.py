from sql_generator import generate_sql
from execute_query import run_query

while True:

    user_input = input("Ask your query: ")

    sql_query = generate_sql(user_input)

    print("Generated SQL:", sql_query)

    if sql_query != "Query not understood":

        results = run_query(sql_query)

        for row in results:
            print(row)

    else:
        print("Try another query")