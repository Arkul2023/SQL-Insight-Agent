from Executor import run_query
from SQL_generator import generate_sql

def build_answer(question, dataframe):

    if dataframe.shape[0] == 1:
        row = dataframe.iloc[0]
        return ", ".join(str(v) for v in row.values)

    return dataframe.to_string(index=False)


if __name__ == "__main__":
    try:

        question = "Tell me students name who scored highest in maths?"

        sql = generate_sql(question)

        df = run_query(sql)

        answer = build_answer(question, df)

        print("Final Answer:", answer)

    except Exception as e:
        print("Error:", e)