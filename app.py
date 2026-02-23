import streamlit as st 
from SQL_generator import generate_sql 
from Executor import run_query 
from response_builder import build_answer 
from guardrails import is_safe_query 

st.set_page_config(page_title="Student SQL Assistant") 

st.title("Student Database Assistant") 

question = st.text_input("Ask your question:") 

if st.button("Submit") and question: 

    with st.spinner("Understanding question..."):
        try:
            sql_query = generate_sql(question)  

            df = run_query(sql_query)

            if df.empty:
                st.warning("No match found")
                st.stop()

            answer = build_answer(question, df)

            st.success(answer)

        except Exception as e:
            st.error(f"Error occurred: {e}")