# SQL-Insight-Agent
SQL-Insight-Agent is an AI-powered natural language interface for relational databases that allows users to query data using plain English instead of writing SQL. 
The system translates user questions into safe, executable SQL queries, retrieves results in real time, and returns human-readable responses. 
It supports both schema-level exploration (tables, columns, structure) and analytical queries (aggregations, rankings, filters), making databases accessible to non-technical users while maintaining accuracy and security.

SQL Insight Agent is an AI-powered Natural Language to SQL (Text-to-SQL) system that enables users to query relational databases using plain English. The system leverages the NumbersStation/nsql-350M model to translate user queries into executable SQL statements and returns structured, human-readable responses.

The solution is designed for scalable enterprise environments where non-technical stakeholders need secure, real-time access to structured data.

**Tech Stack

Python
Hugging Face Transformers
PostgreSQL
SQLAlchemy / Psycopg2
Sttreamlit
NumbersStation/nsql-350M

**Enterprise Capabilities

Scalable architecture
Clear separation of concerns
Model abstraction layer (can replace with larger LLMs)
Ready for integration with RAG pipelines
Suitable for internal BI assistants

**Use Cases

Business Intelligence Assistants
Internal Data Query Chatbots
Self-service analytics platforms
Database exploration for non-technical teams
