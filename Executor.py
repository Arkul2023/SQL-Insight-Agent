from db import get_engine
import pandas as pd

def run_query(query: str):
    engine = get_engine()
    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
    return df

if __name__ == "__main__":
    try:
        test_query = "select * from Student_Marks;"
        df = run_query(test_query)

        print("Database connection Successful")
        print(df)

    except Exception as e:
        print("Error")
        print(e)
