from SQL_model import question_to_sql


def generate_sql(question: str) -> str:

    sql = question_to_sql(question)

    sql = sql.strip().replace("\n", " ")

    # If model omitted SELECT, add it back safely
    if not sql.lower().startswith("select"):
        sql = "SELECT " + sql

    # Basic protection against dangerous queries
    forbidden = ["insert", "update", "delete", "drop", "alter", "truncate"]

    if any(word in sql.lower() for word in forbidden):
        raise ValueError("Dangerous SQL detected")

    return sql
