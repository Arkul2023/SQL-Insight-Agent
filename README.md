# SQL-Insight-Agent
SQL-Insight-Agent is an AI-powered natural language interface for relational databases that allows users to query data using plain English instead of writing SQL. 
The system translates user questions into safe, executable SQL queries, retrieves results in real time, and returns human-readable responses. 
It supports both schema-level exploration (tables, columns, structure) and analytical queries (aggregations, rankings, filters), making databases accessible to non-technical users while maintaining accuracy and security.

Designed and implemented a modular Text-to-SQL agent pipeline that translates natural language queries into executable SQL statements using the NumbersStation/nsql-350M model.

Engineered an end-to-end architecture integrating model inference, schema grounding, secure query execution, and structured response generation over a PostgreSQL database.

Currently working on improving the Agent to make it scalable and ready for business use cases.

**Tech Stack

1) Python
2) Hugging Face Transformers
3) PostgreSQL
4) SQLAlchemy / Psycopg2
5) Streamlit
6) NumbersStation/nsql-350M

