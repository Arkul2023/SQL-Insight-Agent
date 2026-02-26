from sqlalchemy import create_engine, text

# Replace with your credentials
DB_USER = "postgres"
DB_PASSWORD = "newpassword123"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "Student"

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)

def get_engine():
    return engine

if __name__ == "__main__":
    try:
        with engine.connect() as conn:
            # simple query without aliases
            result = conn.execute(text("SELECT * FROM Student_Marks"))
            print("Query executed successfully!")
            for row in result:
                print(row)

    except Exception as e:
        print("Query failed:")
        print(e)

